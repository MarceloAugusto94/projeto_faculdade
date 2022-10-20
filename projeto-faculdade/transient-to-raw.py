# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Notebook para transformação de origem do dado que está em formato csv para formato parquet. Formato este recomendado para análises.

# COMMAND ----------

path = 'dbfs:/mnt/adlsprojetofaculdade/transient/uf_tipo.csv'

df = (spark
     .read
     .option('header', 'true')
     .csv(path))

df.display()

# COMMAND ----------

df.printSchema()
