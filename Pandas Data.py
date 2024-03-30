
from pandas import *

#Reading data files
data=read_csv("pokemon_data.csv")
print(data.head(4))
datatext=read_csv("pokemon_data.txt", delimiter="\t")
print(datatext.head(4))
data_excel=read_excel("pokemon_data.xlsx")
print(data_excel.head(4))

#Reading parts of file
print(f'{data.columns}') #Reads Headers of the columns
print(f'{data["Name"]}') #Reads the whole column
print(f'{data[["Name","Type 1","HP"]]}') #Reads multiple columns
print(f'{data.iloc[0]}') #Reads the whole row
print(f'{data.iloc[1:5]}') #Reads multiple rows
print(f'{data.iloc[2,1]}') #Reads a cell
print(f'{data.loc[data["Type 1"]=="Psychic"]}') #Reads a column satisfying the given criteria
print(f'{data.describe()}') #Reads the file and returns statistics of the data
print(f'{data.sort_values(["Type 1","HP"])}') #Sorts the given column

# Making changes in the data
data["Total"]=data["HP"]+data["Attack"]+data["Defense"]+data["Sp. Atk"]+data["Sp. Def"]+data["Speed"]
print(data.head(5))
data=data.drop(columns=["Total"])
print(data.head(5))
data["Totals"]=data.iloc[:,4:10].sum(axis=1)
cols=list(data.columns.values)
data=data[cols[0:10]+[cols[-1]]+cols[10:12]]
print(data.head(5))

# Saving the changes
data.to_csv("pokemon_data_with_totals.csv")
data.to_excel("pokemon_data_with_totals.xlsx", index=False)
data.to_csv("pokemon_data_with_totals.txt", index=False, sep="\t")

# Filtering Data
fil=data.loc[(data["Legendary"]== True) & (data["Type 1"] == "Fire")]
fil.reset_index(drop=True, inplace=True)

print(fil)

from re import *
fg=data.loc[data["Name"].str.contains("^pi[a-z]*", flags=I)]
fg.reset_index(drop=True, inplace=True)
Mega=data.loc[data["Name"].str.contains("Mega")]
Mega.reset_index(drop=True, inplace=True)
print(Mega)
print(fg)

#Connditional changes
data.loc[data["Type 1"]=="Fire", "Legendary"]=True
#Multiple assignation also works
#testt=data.loc[data["Type 1"]=="Grass", ["Totals", "Generation"]]=[1000,0]

data.loc[data["Generation"]==1, "Region"]="Kanto"
data.loc[data["Generation"]==2, "Region"]="Johto"
data.loc[data["Generation"]==3, "Region"]="Hoenn"
data.loc[data["Generation"]==4, "Region"]="Sinnoh"
data.loc[data["Generation"]==5, "Region"]="Unova"
data.loc[data["Generation"]==6, "Region"]="Kalos"
colms=list(data.columns.values)
data=data[colms[0:12]+[colms[-1]]+colms[12:13]]

print(data)
data.to_csv("pokemon_data_with_regions.csv")


# Aggregate Statistics
print(data.groupby(["Type 1"]).sum())
data['count']=1
print(data.groupby(["Type 1"]).count()['count'])
print(data.groupby(["Region"]).count()['count'])
print(data.groupby(["Type 2"]).count()['count'])
print(data.groupby(["Type 1","Type 2", "Region"]).count()['count'])

#Working with large amounts of data
new=DataFrame(columns=colms)
for i in read_csv("pokemon_data_with_regions.csv", chunksize=5):
    print(i)

