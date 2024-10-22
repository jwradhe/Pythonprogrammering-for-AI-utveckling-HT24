import pandas as pd

countryData = {
    "Country": ['Sweden', 'Finland', 'Norway', 'Denmark', 'Germany'],
    "Population": ['10622058','5619156','5590842','5984890','84408410'],
    "Size(km2)": ['450295','338462','385207','42952','357592'],
    "Continent": ['Europa','Europa','Europa','Europa','Europa']
}

df = pd.DataFrame(countryData)

print(df)