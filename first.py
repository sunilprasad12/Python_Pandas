import pandas as pd
import matplotlib.pyplot as plt

file_name = "Sunil_4.xlrd"
df = pd.read_excel(file_name)
#print(df)

df_country_number = df.loc[(df['country'] == 'India') & (df['number'] == 43)]
df_country_number = df.sort_values(by=['number'])

# This two lines for line graph
#df_country_number.plot(x='country', y='number')
#plt.show()

# this lines for bar graph
df_country = df.groupby(['country']).sum()
df_country['number'].plot.bar()
plt.show()
