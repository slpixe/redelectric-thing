AREA_TYPES = [
    ('Film', 'Film'),
    ('TV', 'TV'),
    ('OAV', 'OAV')
]
a = {}
b = {}
k = 0

for areas in AREA_TYPES:
    print(areas[0])
    k += 1
    a[areas] = k
    b += a[areas]
    print(a[areas])

 



# a = {}
# k = 0
# while k < 10:
#     <dynamically create key> 
#     key = ...
#     <calculate value> 
#     value = ...
#     a[key] = value 
#     k += 1



#     AREA_TYPES