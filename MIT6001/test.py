from pp3 import intSet

w1=intSet()
w2=intSet()

for i in range(2,5):
    w1.insert(i)
    w2.insert(i)
    
print(w1.intersect(w2))