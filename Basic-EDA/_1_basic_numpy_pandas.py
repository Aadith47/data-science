import pandas as pd

import numpy as np

from pathlib import Path

df = pd.read_csv("student-data.csv")

def data_summary(df):
    rows = df.shape[0],
    data_quality = df.isnull().sum()
    duplicates = df.duplicated().sum()
    about_data = df.describe()


    pass_count = pd.crosstab(df["studytime"], (df["passed"]))
    avg_passed = df.groupby("passed")["studytime"].mean()
    failed = df.groupby("passed")["absences"].mean()["no"]

    return 

print(data_summary(df))

def outlier_summary(series):
    s = series.dropna().astype(float)
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    outliers = s[(s < lower) | (s > upper)]

    return dict(count=len(s), min=s.min(), q1=q1, median=s.median(), q3=q3, max=s.max(), iqr=iqr, outlier_count=len(outliers), outlier_top=outliers.sort_values(ascending=False).head(10).to_list())

def data_summary(df):
    rows = df.shape[0],
    columns = df.shape[1],
    columns_name = list(df.columns),
    missing_values = df.isnull().sum()
    missing_value_percentage = (missing_values / len(df) * 100)

    return dict(Rows=rows,Columns = columns, Column_Names = columns_name, Missing_Value_Percentage = missing_value_percentage,  )



df = pd.read_csv("student-data.csv")

print("To print few colums")
print(df.head())

print("To find the missing values")
print(df.info())

print("Missing values")
print(df.isnull().sum())

print("Average minimum maximum median standard deviation")
print(df.describe())

print("Total pass and fails count")
print(df["passed"].value_counts())

print("Student who may need financial assistance")
result1 = np.where(((df["Mjob"] == "at_home") | (df["Fjob"] == "at_home")) & (df["paid"] == "no"),"Yes","No")
print(pd.Series(result1).value_counts())

print("Student who spend most of the time alone")
result2 = np.where(((df["Mjob"] != "at_home") & (df["Fjob"] != "at_home")) & (df["passed"] == "no"),"Yes","No")
print(pd.Series(result2).value_counts())

print("Mental health")
result3 = np.where((df["activities"] == "no") & (df["health"] < 2),"Yes","No")
print(pd.Series(result3).value_counts())

print("Student who have higher absence due to travel time")
result4 = np.where((df["traveltime"] >= 3) & (df["absences"] > 7),"Yes","No")
print(pd.Series(result4).value_counts())

print("Failures due to absences")
result8 = np.where((df["absences"] > 7) & (df["passed"] == "no"), "Yes", "No")
print(pd.Series(result8).value_counts())

print("student is study is effective or not")
result5 = np.where((df["studytime"] >= 2) & (df["traveltime"] < 2), "Effective" , "Not Effective")
print(pd.Series(result5).value_counts())

print("Students who need to be physically more active")
result6 = np.where(df["freetime"] > 2 & (df["internet"] == "yes") & (df["activities"] == "no"), "Need to be active", "Active Enough" )
print(pd.Series(result6).value_counts())

print("Need guidance")
result7= np.where((df["studytime"] >= 2) & (df["passed"] == "no"), "Need Guidance", "On Track")
print(pd.Series(result7).value_counts())
