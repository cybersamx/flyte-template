# Flyte Project Template

This project serves as a starter template for any [Flyte](https://flyte.org) project.

## Setup

Instructions for setting up the project and tools (including `flyte`) needed to compile and run the project. 

### Set up Local Flyte

1. Optionally use `pyenv` to manage different versions of python on your machine.

   ```shell
   brew install pyenv
   # Follow the post-install instructions for pyenv
   pyenv install --list   # List of available python versions to install
   pyenv install 3.11.9
   pyenv global 3.11.9
   ```

1. Go to the root directory of this flyte project and create a virtual environment.

   ```shell
   python -m venv .venv
   source .venv/bin/activate
   ```

1. Install `make`.

   ```shell
   brew install make
   ```

1. Install the tools and packages.

   ```shell
   make install
   ```
   
### Run Flyte Workflow Locally

1. Run the workflow locally.

   ```shell
   make run
   ```

### Run Tests

1. Run the unit tests.

   ```shell
   make test
   ```

### Future Work

* Consider using `poetry` instead of `make`.
* Right now, the tools needed by this project are installed in the virtual environment. Consider installing to the user directory.
* Separate the installation of packages from the installation of tools.
