import inflect

x = inflect.engine()
suma = 0
for y in range(1, 1001):
    r = x.number_to_words(y)
    r = r.replace(" ", "")
    r = r.replace("-", "")
    suma += len(r)
print(suma)



