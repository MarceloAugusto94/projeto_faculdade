# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Notebook para aplicação de regras de negócio e merge..

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ANÁLISE DE TOTAL DOS ÚLTIMOS 3 ANOS POR MÊS E ESTADOS

# COMMAND ----------

df_refined = spark.sql('''


    select 
    *
    from default.uf_tipo_trusted
    where ano in ('2019', '2020', '2021')
    order by 
    mes,
    ano,
    total desc
    
    
''')

df_refined.display()

# COMMAND ----------

path_refined = '/mnt/adlsprojetofaculdade/refined/uf_tipo'
refined_delta_table = 'uf_tipo_refined'

# COMMAND ----------

df_refined.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(refined_delta_table, path = path_refined)

# COMMAND ----------

dbutils.fs.ls('dbfs:/mnt/adlsprojetofaculdade/refined')
