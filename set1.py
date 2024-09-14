a={x for x in 'ryacti' if x in 'abc'}
print(a)

a.update([4,5],{1,2,3})
print(a)
a.discard(5)
print(a)
a.remove(4)
print(a)
