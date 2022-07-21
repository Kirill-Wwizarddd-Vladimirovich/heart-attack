===============================================================================
heart-attack
===============================================================================

Pet project. Heart atattack analyzis

Getting Started:
-------------------------------------------------------------------------------

- Configure `poetry` (should be done once globally):

.. code::

    poetry config virtualenvs.in-project false
    poetry config virtualenvs.path <conda-install-path>/envs

- Create and activate virtual environment for development:

.. code::

    conda env create -f devenv.yaml
    conda activate heart-attack-denv

- Install dependencies with `poetry`:

.. code::

    poetry install

- After installing dependencies we recommend updating their versions:

.. code::

    poetry update

- `poetry update` can be also used for 

- Install src package in development mode (to solve the import problem, then
  you can use `import src` inside jupyter notebook):

.. code::

    conda-develop .

- Set environment variables **(in the root directory!)**. Create and fill out
  in the file `.env` like sample `.env.example`.

- To add package or make package production one (packages for data science are
  in `dev` section) use:

.. code::

    poetry add <package>

- More about Poetry commands you can read on their `documentation page`_.


Project Organization
-------------------------------------------------------------------------------

.. code::

   ├── README.rst          <- The top-level readme for developers.
   │
   ├── pyproject.toml      <- File with metadata for project, dependencies info.
   │
   ├── data
   │   ├── external        <- Data from third party sources.
   │   ├── interim         <- Intermediate data that has been transformed.
   │   ├── processed       <- The final, canonical data sets for modeling.
   │   └── raw             <- The original, immutable data dump.
   │
   ├── docs                <- Technical documentation.
   │
   ├── models              <- Trained and serialized models, model predictions,
   │                          or model summaries.
   │
   ├── notebooks           <- Jupyter notebooks. Naming convention is a number
   │                          (for ordering), the creator's initials, and a
   │                          short `-` delimited description, e.g.
   │                          `001.001-jqp-initial-data-exploration`.
   │
   ├── references          <- Data dictionaries, manuals, and all other
   │                          explanatory materials.
   │
   ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
   │   └── figures         <- Generated graphics and figures to be used in
   │                          reporting.
   │
   ├── service             <- Source code for Web API wrapper for resulting
   │   │                      model.
   │   │
   │   ├── __init__.py     <- Makes service a Python package.
   │   │
   │   ├── config.py       <- `pydantic.BaseSettings` for storing environment
   │   │                      variables.
   │   │
   │   ├── dependencies.py <- `DeclarativeContainer` with basic dependencies
   │   │                      for Web API - fake `model` and `config`.
   │   │
   │   ├── main.py         <- Entrypoint with function factory for `FastAPI`.
   │   │
   │   ├── api             <- `FastAPI` endpoints, ETL scripts and API 
   │   │                      contracts.
   │   │
   │   └── model           <- Types for model and `prediction` function.
   │
   ├── src                 <- Source code for use in this project.
   │   ├── __init__.py     <- Makes src a Python package.
   │   │
   │   ├── data            <- Scripts to download or generate data.
   │   │
   │   ├── features        <- Scripts to turn raw data into features for
   │   │                      modeling.
   │   │
   │   ├── models          <- Scripts to train models and then use trained
   │   │                      models to make predictions.
   │   │
   │   └── reports         <- Scripts to create exploratory reports and results
   │                          oriented visualizations.
   │
   ├── workflow            <- Snakemake workflow storage.
   │   ├── envs            <- Conda environments for snakemake rules.
   │   │   └── default.yaml
   │   │
   │   ├── rules           <- Rules as modules.
   │   │   └── clean.smk
   │   │
   │   ├── scripts         <- Support functions for using in snakemake
   │   │                      workflow.
   │   │
   │   ├── config.yaml     <- Parameters for workflow in yaml format.
   │   │
   │   └── Snakefile       <- Entrypoint of the workflow (it will be
   │                          automatically discovered when running snakemake
   │                          from the root of above structure).
   │
   └── .env.example        <- Example of file for environment variables, like
                              MinIO access or Postgresql credentials. It is
                              necessary to create an `.env` file based on it.

.. _documentation page:
.. _poetry_cli: https://python-poetry.org/docs/cli/
