# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Notebook para tratamento dos dados. Limpeza, tipagem.. 

# COMMAND ----------

dbutils.fs.ls('/mnt/adlsprojetofaculdade/raw/uf_tipo')

# COMMAND ----------

df_trusted = spark.sql('''


with groupby 
as
(
  select 
     sigla_uf
    ,ano
    ,mes
    ,automovel
    ,bonde
    ,caminhao
    ,caminhaotrator
    ,caminhonete
    ,camioneta
    ,chassiplataforma
    ,ciclomotor
    ,microonibus
    ,motocicleta
    ,motoneta
    ,onibus
    ,quadriciclo
    ,reboque
    ,semireboque
    ,sidecar
    ,outros
    ,tratoresteira
    ,tratorrodas
    ,triciclo
    ,utilitario
    ,total 
  from default.uf_tipo_raw
  group by 
     sigla_uf
    ,ano
    ,mes
    ,automovel
    ,bonde
    ,caminhao
    ,caminhaotrator
    ,caminhonete
    ,camioneta
    ,chassiplataforma
    ,ciclomotor
    ,microonibus
    ,motocicleta
    ,motoneta
    ,onibus
    ,quadriciclo
    ,reboque
    ,semireboque
    ,sidecar
    ,outros
    ,tratoresteira
    ,tratorrodas
    ,triciclo
    ,utilitario
    ,total 
  order by 
     sigla_uf
    ,ano
    ,mes
)

select 
  sigla_uf,
  sum(total) as total,
  ano, 
  mes
from groupby
group by 
  sigla_uf,
  ano,
  mes
order by 
  mes,
  ano,
  total desc
  
''')

df_trusted.display()

# COMMAND ----------

path_trusted = '/mnt/adlsprojetofaculdade/trusted/uf_tipo'
trusted_delta_table = 'uf_tipo_trusted'

# COMMAND ----------

df_trusted.write.option("overwriteSchema", "true").mode("overwrite").format('delta').saveAsTable(trusted_delta_table, path = path_trusted)
