//one line python
print(reduce(lambda x,y : x+ y, [x for x in range(1,1000) if ((x%3==0) or (x%5==0))]))

