# Project Setup
## Checklist
- Sign up to Databricks free edition
- Set up project with uv
- Download dbt-core and create dbt project
- Link the dbt project to databricks
- Set up Dev Container
- Create Justfile for common CLI commands
- Install prek for pre-commit checks
- Install Rust based sqruff
- Create terraform area to set up databricks infrastructure
- Create branching strategy - create new branch when building a new feature
- Create two github actions workflows: ci.yaml and cd.yaml, run when creating a pull request into main/master branch.
- Build out bronze, silver, and gold layers of the dbt project
- Add dbt tests to the silver and gold layers
- Build a workflow to automate the injestion of raw data into bronze source and to orchestrate new models into databricks
- Use the gold layer data to build a machine learning model - use the experiment, tune, train, evaluate, explain, promote workflow
- Add code to this repository in the src/ area
- Deploy model to mlflow model registry
- Build a workflow to automate the training and deploying of a new challenger model to Mlflow registry
- Attach champion model to databricks serving endpoint.
- Set up monitoring of model endpoint.

## Notes
- The checklist can be revised based on any databricks courses I take that could be useful to this project.
