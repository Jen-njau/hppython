# name="Jane"
# for i in name:
#     if i !=0:
#         print(i)

fruits=("Mangoes","Oranges","Apples")
try:
    for i in range(5):
        print(f"the index and element from the list is {i, fruits[i]}")
except:
    print("index out of range")

nambari=(3,4,5,7)
if len(nambari)>3:
    raise Exception(f"length of the given list must be less or equal to 3 but is {len(nambari)}")

