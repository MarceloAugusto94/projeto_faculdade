# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Notebook para transformação de origem do dado que está em formato .csv para formato .parquet. Formato este recomendado para análises.

# COMMAND ----------

# DBTITLE 1,path do caminho dos dados na camada transient do data lake
path = 'dbfs:/mnt/adlsprojetofaculdade/transient/uf_tipo.csv'

# COMMAND ----------

# DBTITLE 1,leitura do dado .csv como um dataframe 
df = (spark
     .read
     .option('header', 'true')
     .csv(path))

# COMMAND ----------

# DBTITLE 1,display para visualização do dataframe
df.display()

# COMMAND ----------

# DBTITLE 1,volumetria
df.count()

# COMMAND ----------

# DBTITLE 1,caminho usado para salvar o novo formato .parquet na camada raw do data lake e nome da tabela
path_raw = 'dbfs:/mnt/adlsprojetofaculdade/raw/uf_tipo'
raw_delta_table = 'uf_tipo_raw'

# COMMAND ----------

# DBTITLE 1,escrita no data lake em formato .parquet
 df.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(raw_delta_table, path = path_raw)

# COMMAND ----------

dbutils.fs.ls('dbfs:/mnt/adlsprojetofaculdade/raw')
