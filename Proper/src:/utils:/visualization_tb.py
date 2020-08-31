
top = data.host_id.value_counts()[:10]
f,top1 = plt.subplots(figsize=(16,5))
top1 = sns.barplot(x = top.index,y=top.values,palette="muted")
plt.show()


f,ax = plt.subplots(figsize=(15,6))
ax = sns.countplot(data.neighbourhood_group,palette="muted")
plt.show()

f,rt = plt.subplots(figsize=(12,5))
rt = sns.countplot(data.room_type,palette="plasma")
plt.show()


graf = data[data.room_type == "Entire home/apt"][["neighbourhood_group","price"]]
apt = graf.groupby("neighbourhood_group").mean()
sns.distplot(apt)
plt.show()


gf2 = data[data.room_type=="Private room"]['minimum_nights']
f,minnight = plt.subplots(figsize=(19,5))
minnight = sns.swarmplot(y= gf2.index,x= gf2.values)
plt.xlabel("minimum_nights")
plt.show()

f,ll = plt.subplots(figsize=(16,8))
ll = sns.scatterplot(y=data.latitude,x=data.longitude,hue=data.neighbourhood_group,palette="coolwarm")
plt.show()