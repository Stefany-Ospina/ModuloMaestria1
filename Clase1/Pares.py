app=[1,9,5,0,20,-4,12,16,7]
app
suma=12
for i in range(len(app)):
  for j in range(i+1,len(app)):
    if app[i]+app[j]==suma:
      print(app[i],app[j])
