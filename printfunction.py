#my journey with list [] -> tuple(), list[], set{}, dictionary{'K':'V'} other that qq,ordered dictionary, name tuples
# no one can beat me
# I am invincible
#features - ordered , mutable, anydata types , no fix size, unhashble

def auto_convertion(value):
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    if value.isdigit() or value.startswith('-') and value[1:].isdigit():
        return int(value)

    try:
        return float(value)
    except ValueError:
        pass

    return value
busket = []
i = 0
while True:
    user = (input(""))
    if user == "":
        break
    busket.append(auto_convertion(user))
    print(type(busket[i]))
    i +=1
print(busket[1][1:])