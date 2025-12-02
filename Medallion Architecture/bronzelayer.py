# Databricks notebook source
df = spark.read.table("modified_financial_reporting_5000_v_2")
display(df)



# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FinanceETL").getOrCreate()

# Load CSV into DataFrame
bronze_df = spark.read.format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("modified_financial_reporting_5000_v_2")


# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog workspace;
# MAGIC
# MAGIC
# MAGIC
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Gross Profit` to Gross_Profit;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Operating Expense` to Operating_Expense;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Interest Expense` to Interest_Expense;
# MAGIC ALTER TABLE`default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Tax Expense` to Tax_Expense;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Net Income` to Net_Income;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Assets` to Total_Assets;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Liabilities` to Total_Liabilities;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Total Equity` to Total_Equity;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Operations` to Cash_Flow_Operations;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Investing` to Cash_Flow_Investing;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Cash Flow Financing` to Cash_Flow_Financing;
# MAGIC ALTER TABLE `default`.`modified_financial_reporting_5000_v_2`
# MAGIC RENAME COLUMN `Net Change in Cash` to Net_Change_in_Cash

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog `workspace`; select * from `default`.`modified_financial_reporting_5000_v_2` limit 100;

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("finance_bronze")

# COMMAND ----------

