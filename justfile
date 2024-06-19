set shell := ["bash", "-uc"]

python_version := "3.9"

remote_url := "https://raw.githubusercontent.com/shapediver/OpenApiSpecifications"
remote_tag_prefix := "gb_v2"
remote_file_name := "geometry_backend_v2.yaml"

spec_file := "oas_spec.yaml"
target_dir := "./out"

# Executes the 'build' recipe.
default: build

# Creates a virtual environment and installs the package and its dependencies.
setup:
    # Check Python version.
    # Run `pyenv install -v {{python_version}}` to install globally.
    command -v python{{python_version}}

    # Creates a virtual environment for Python.
    python{{python_version}} -m venv './.venv'

    # Update pip.
    .venv/bin/python{{python_version}} -m pip install --upgrade pip

    # Install dependencies.
    .venv/bin/python{{python_version}} -m pip install -e . \
      -r 'requirements.txt' \
      -r 'requirements_dev.txt'

# Removes the virtual environment and all build artifacts
reset: clean
    rm -rf './.venv'
    find . -type d -path './src/*' -name '__pycache__' -exec rm -rf {} \; || :
    find . -type d -path './tests/*' -name '__pycache__' -exec rm -rf {} \; || :

# Builds the Python package.
[no-exit-message]
build:
    tox -e build

# Removes Python build artifacts.
clean:
    tox -e clean

# Run all Python tests.
[no-exit-message]
test:
    tox

# Run all pre-commit hooks.
[no-exit-message]
check:
    pre-commit run --all-files

# Release the Python package with the specified version.
release version:
    # Stop when repo is dirty
    test -z "$(git diff --shortstat)"

    # Update sdk version number.
    sed -i \
      's/_sdk_version = ".*"/_sdk_version = "{{version}}"/' \
      "./src/shapediver/geometry_api_v2/sd_client.py"

    # Build package and docs.
    rm -rf './dist'
    tox -e docs

    # Commit and tag.
    git add -A .
    git commit -m "Publish v{{version}}"
    git tag -a "v{{version}}" -m "Publish v{{version}}"

    # Build the package - the package version is taken from the Git tag.
    tox -e build

    # Publish to test registry and then to PyPI.
    tox -e publish
    tox -e publish -- --repository pypi


# Generate the Python client from the OpenAPI specification.
generate version:
    # Ensure that the generator is installed.
    command -v openapi-generator-cli

    # Stop when repo is dirty
    test -z "$(git diff --shortstat)"

    # Fetch the requested version of the specification.
    curl -f \
      "{{remote_url}}/{{remote_tag_prefix}}%40{{version}}/{{remote_file_name}}" \
      -o "{{spec_file}}"

    # Generate the Python client.
    mkdir -p "{{target_dir}}"
    openapi-generator-cli generate \
        --package-name "shapediver.geometry_api_v2.client" \
        --generate-alias-as-model \
        -i "{{spec_file}}" \
        -g python \
        -o "{{target_dir}}" || { \
            rm -rf "{{target_dir}}"; \
            exit 1; \
        }

    # Replace old client with new one.
    rm -rf "src/shapediver/geometry_api_v2/client/" || :
    cp -r "{{target_dir}}/shapediver/geometry_api_v2/client" "src/shapediver/geometry_api_v2/"

    just _update-deps

    # Clean up.
    rm -rf "{{target_dir}}"

    # Commit changes.
    git add -A .
    git commit -m "Generate spec version {{version}}"

# Updates dependencies.
_update-deps:
    #!/usr/bin/env bash
    src="{{target_dir}}/requirements.txt"
    dist="requirements.txt"

    # Delete old dependencies.
    start=$(grep -Fn 'AUTO-GENERATED CODE: START' "${dist}" | cut -f1 -d:)
    end=$(grep -Fn 'AUTO-GENERATED CODE: END' "${dist}" | cut -f1 -d:)
    sed -i "$(($start + 1)),$(($end - 1))d" "${dist}"

    # Insert new dependencies.
    deps="$(cat "${src}")"
    while IFS= read -r line; do
        sed -i "/AUTO-GENERATED CODE: END/i \ ${line}" "${dist}"
    done <<< "${deps}"
