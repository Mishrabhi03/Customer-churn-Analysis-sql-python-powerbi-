import pandas as pd
df=pd.read_csv(r"C:\customer churn analysis project\sql_output.csv")
print(df.head())
print(df.info())

df['ChurnFlag']=df['Churn'].map({'Yes':1,'No':0})

df['TenureBucket']=pd.cut(
    df['tenure'],
    bins=[0,12,24,48,72],
    labels=['0-1 years','1-2 years','2-4 years','4-6 years']
)

df['ChargeBucket'] = pd.cut(
    df['MonthlyCharges'],
    bins=[0, 35, 70, 120],
    labels=['Low', 'Medium', 'High']
)

contract_churn = (
    df.groupby('Contract')['ChurnFlag']
    .mean()
    .reset_index()
)

contract_churn['ChurnRate'] = (contract_churn['ChurnFlag'] * 100).round(2)
print(contract_churn)


tenure_churn = (
    df.groupby('TenureBucket')['ChurnFlag']
    .mean()
    .reset_index()
)

tenure_churn['ChurnRate'] = (tenure_churn['ChurnFlag'] * 100).round(2)
print(tenure_churn)


final_cols = [
    'customerID',
    'gender',
    'SeniorCitizen',
    'tenure',
    'TenureBucket',
    'Contract',
    'MonthlyCharges',
    'ChargeBucket',
    'TotalCharges',
    'Churn'
]

final_df = df[final_cols]
final_df.to_csv("final_churn.csv", index=False)

print("final_churn.csv created successfully")
