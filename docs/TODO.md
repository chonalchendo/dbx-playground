# Project Checklist 

- [x] Upload data to s3 bucket
- [ ] Add logging to extraction job
- [ ] Create autloader script to load data from s3 bucket to databricks bronze layer
- [ ] Build out silver and gold datasets using dbt
- [ ] Use gold layer data to build a dataset for model development
- [ ] Build an ML model using PySpark
- [ ] Register the model in Mlflow
- [ ] Create an endpoint to generate batch predictions
- [ ] Create an inference payload for monitoring