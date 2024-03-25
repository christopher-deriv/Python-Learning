#Something to keep in mind is when setting a variable even if it's in a for you are still setting a variable just as if you were doing number = 2

for number in range(10):
    print("Hello")

fav_movies = ["Sandlot", "The Lego Movie", "Dune"]

for movie in fav_movies:
    print(movie)

#Loop 40 times and print the number of the loop times 2. Ex. 2,4,6,8
    
for number in range(40):
    print((number+1)*2)