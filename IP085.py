def sum_integers(data):
    sum = 0
    if isinstance(data,int): return data
    if isinstance(data,(list,tuple)):
        for i in data:
            sum += sum_integers(i)
    return sum
print(sum_integers([[(4,3)],(((45,[9]))),[(42)],[1,6,8]]))
print(sum_integers(["a",([[2]],[["b"]]),40,[[2.2]]]))
print(sum_integers((1,2,[3],[[4]])))
print(sum_integers(["hello","world"]))