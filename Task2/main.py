import pandas as pd
import matplotlib.pyplot as plt

var1 = pd.read_excel(r"C:\Users\iveda\Desktop\Internship\Task 2\Unemployment in India.xlsx")

# print(var1) 
# print(var1.columns) 
# print(var1.head(10)) 
# print(var1['Region'])  

var1['Labor Force'] = var1['Estimated Employed'] / (var1['Estimated Labour Participation Rate (%)'] / 100)

var1['Number of Unemployed'] = var1['Labor Force'] - var1['Estimated Employed']

var1['Calculated Unemployment Rate (%)'] = (var1['Number of Unemployed'] / var1['Labor Force']) * 100

regions = var1['Region'].unique()

for region in regions:
    region_data = var1[var1['Region'] == region]
    
    plt.figure(figsize=(14, 8))
    plt.plot(region_data['Date'], region_data['Estimated Unemployment Rate (%)'], label='Estimated Unemployment Rate', linestyle='--')
    plt.plot(region_data['Date'], region_data['Calculated Unemployment Rate (%)'], label='Calculated Unemployment Rate', linestyle='-')
    
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.title(f'Estimated vs. Calculated Unemployment Rate Over Time for {region}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.show()
