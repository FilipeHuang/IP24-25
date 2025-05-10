def comb(k,planets,lst_mid,final_lst):
        if len(lst_mid) == k: return final_lst.append(lst_mid)
        for i in planets:
            comb(k,planets,lst_mid+[i],final_lst)
def weekends(k, planets):
    final_lst = []
    comb(k,planets,[],final_lst)
    return final_lst

output = weekends(2, ["earth", "neptune"])
print(sorted(output))

print()

output = weekends(3, ["earth", "mars", "saturn"])
print("output is of type", type(output))
print("output has size:", len(output))
for x in sorted(output): print(x)