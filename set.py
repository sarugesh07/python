x={"a","b","c"}
y={"f","d","a","b","c"}
z=x.issubset(y)
print(z)
x={"f","d","a","b","c"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)
x={"a","b","c"}
y={"f","d","a","b","c"}
z=x.isdisjoint(y)
print(z)
