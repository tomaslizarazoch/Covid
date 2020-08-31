data.dtypes

data.isnull().sum()

data.columns

data.drop(['id','host_name','last_review','number_of_reviews'], inplace = True , axis = 1)
data.head(5)

# Exploremo las localidades de New York

data.neighbourhood_group.unique()