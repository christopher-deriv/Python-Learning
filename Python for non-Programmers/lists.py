fav_movies = ["Sandlot", "The Lego Movie", "Dune"]

print(len(fav_movies))

# lists start with 0 (think like elevator floors) so wen you want to reference something keep that in mind
print(fav_movies[0])

fav_movies.append("Iron Man")

print(len(fav_movies))

print(fav_movies)

fav_movies.insert(1,"Batman")

print(fav_movies)

del(fav_movies[3])

print(fav_movies)