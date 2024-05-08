# vim: set ft=make :

# Creates a virtual environment and installs the package and its dependencies.
setup:
    command -v python3.9
    python3.9 -m venv './.venv'
    .venv/bin/python3.9 -m pip install -e . -r 'requirements.txt' -r 'requirements_dev.txt'

# Removes the virtual environment and all build artifacts
reset:
    just clean
    rm -rf './.venv'
    find . -type d -path './src/*' -name '__pycache__' -exec rm -rf {} \; || :
    find . -type d -path './tests/*' -name '__pycache__' -exec rm -rf {} \; || :

# Builds the Python package.
build:
    tox -e build

# Removes Python build artifacts.
clean:
    tox -e clean

# Run all Python tests.
test:
    tox
