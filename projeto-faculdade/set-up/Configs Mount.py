# Databricks notebook source
# DBTITLE 1,LEITURA DOS ARQUIVOS DO DATALAKE
dbutils.fs.ls('/mnt/adlsprojetofaculdade/transient/')

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list('projeto-faculdade-scope')

# COMMAND ----------

storage_account_name = 'adlsprojetofaculdade'
container_name = 'transient'
client_id = dbutils.secrets.get(scope = 'projeto-faculdade-scope', key = 'databricks-app-secret-client-id')
tenant_id = dbutils.secrets.get(scope = 'projeto-faculdade-scope', key = 'databricks-app-tenant-id-2')
client_secret = dbutils.secrets.get(scope = 'projeto-faculdade-scope', key = 'databricks-app-secret-client-secret-2')

# COMMAND ----------

# configurações de OAuth

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
          }

# COMMAND ----------

dbutils.fs.mount(
    source = f'abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/',
    mount_point = f'/mnt/{storage_account_name}/{container_name}',
    extra_configs = configs
)
