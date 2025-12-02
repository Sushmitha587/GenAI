# Databricks notebook source
df = spark.table("gold_pnl").orderBy("year")
display(df)

# COMMAND ----------

df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "revenue", "cogs", "gross_profit"))


# COMMAND ----------

df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "revenue_yoy_pct"))



# COMMAND ----------


df = spark.table("gold_pnl").orderBy("year")
display(df.select("company", "year", "gross_profit", "operating_income", "net_income"))


# COMMAND ----------

df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "gross_margin", "operating_margin", "net_margin"))


# COMMAND ----------

df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "gross_margin_rolling3", "net_margin_rolling3"))


# COMMAND ----------

df = spark.table("gold_kpi").orderBy("year")
display(df.select("company", "year", "roa", "roe"))


# COMMAND ----------

df = spark.table("gold_kpi").orderBy("year")
display(df.select("company","year","roa","roe"))


# COMMAND ----------

df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","total_assets","total_liabilities","total_equity"))


# COMMAND ----------

df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","working_capital"))


# COMMAND ----------

df = spark.table("gold_balance_sheet").orderBy("year")
display(df.select("company","year","delta_assets","delta_liabilities","delta_equity"))


# COMMAND ----------


df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year",
                  "cash_flow_operations","cash_flow_investing","cash_flow_financing"))


# COMMAND ----------

df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year","free_cash_flow"))


# COMMAND ----------

df = spark.table("gold_cashflow").orderBy("year")
display(df.select("company","year","net_change_in_cash"))


# COMMAND ----------

df = spark.table("gold_completeness").orderBy("year")
display(df.select("company","year","completeness_pct"))


# COMMAND ----------

df = spark.table("gold_missing_years")
display(df)


# COMMAND ----------

