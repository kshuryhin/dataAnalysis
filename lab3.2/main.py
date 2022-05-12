import numpy as np
from numpy import genfromtxt

#Task 1, 2
fname = "game_sales.csv"
dtype1 = np.dtype([("NA_Sales", "f8"), ("EU_Sales", "f8"), ("JP_Sales", "f8"), ("Other_Sales", "f8"),
                   ("Critic_Score", "i4")])
dtype2 = np.dtype([("Platform", "U25")])

games = genfromtxt(fname, delimiter=",", dtype=dtype1, skip_header=True, usecols=(5, 6, 7, 8, 10))
games_names = genfromtxt(fname, delimiter=",", dtype=dtype2, skip_header=True, usecols=[1])
games1 = games[:1000]
games2 = games[1000:]

game_names1 = games_names[:1000]
game_names2 = games_names[1000:]

# print(games1)
# print(games2)


#Task 3
unique1 = np.unique(game_names1).size
unique2 = np.unique(game_names2).size

# print("Кількість унікальних платформ у першій частині " + str(unique1))
# print("Кількість унікальних платформ у другій частині " + str(unique2))

#Task 4
intersect = np.intersect1d(game_names1, game_names2)
# print("Спільні платформи " + str(intersect))

#Task 5
different = np.union1d((np.setdiff1d(game_names1, game_names2)), (np.setdiff1d(game_names2, game_names1)))
# print("Непересічні платформи " + str(different))

#Task6, 7
NA1 = 100.5
EU1 = 98.3
JP1 = 124.4

g_price1 = np.array([NA1, EU1, JP1])

NA2 = 110.7
EU2 = 99.6
JP2 = 128.2

g_price2 = np.array([NA2, EU2, JP2])

games1_cost = genfromtxt(fname, delimiter=",", skip_header=True, usecols=(5, 6, 7))
games1_cost = games1_cost[:1000]*g_price1

games2_cost = genfromtxt(fname, delimiter=",", skip_header=True, usecols=(5, 6, 7))
games2_cost = games2_cost[1000:]*g_price2

# print("Вартість у першій частині")
# print(games1_cost)
# print()
# print(print("Вартість у другій частині"))
# print(games2_cost)

#Task8
countries1 = genfromtxt(fname, delimiter=",", skip_header=True, usecols=(5, 6, 7))[:1000]
countries2 = genfromtxt(fname, delimiter=",", skip_header=True, usecols=(5, 6, 7))[1000:]

other1 = genfromtxt(fname, delimiter=",", skip_header=True, usecols=[8])[:1000]
other2 = genfromtxt(fname, delimiter=",", skip_header=True, usecols=[8])[1000:]


def count(countries, other):
    index = 0
    c = 0
    for x in countries:
        if x.sum() < other[index]:
            c += 1
        index += 1
    return c


def compare(x1, x2):
    if x1 < x2:
        print("У першій тисячі записів частка споживачів із Північної Америки, Європи та Японії більша, ніж в іншій "
              "частині записів")
    else:
        print("У першій тисячі записів частка споживачів із Північної Америки, Європи та Японії менша, ніж в іншій "
              "частині записів")


r1 = count(countries1, other1)
r2 = count(countries2, other2)

compare(r1, r2)

print("Кількість рядків першої частини, де частка з продажу у NA, EU та JP разом нижча, ніж в інших країнах " + str(r1))
print("Кількість рядків другої частини, де частка з продажу у NA, EU та JP разом нижча, ніж в інших країнах " + str(r2))
