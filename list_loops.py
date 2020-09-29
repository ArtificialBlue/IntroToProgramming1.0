#Lists and Loops Tutorial

songs = ["ROCKSTAR", "Do It", "For The Night"]

#First Item of List
print(songs[0])

#Last Item of List
print(songs[-1])

#print out "Do It" and "For The Night" using a list slice on the songs list
print(songs[1:3])

#update the last element in the songs list with a new song of your choice
songs[-1] = "Mr.Blue Sky"
print(songs)

#add three songs of your choice to your songs list 
#delete one of the elements in your songs list 
songs.append("Don't Stop Me Now")
songs.append("Blinding Lights")
songs.append("Hug All Ur Friends")

songs.remove("Do It")
print(songs)

animals = ["Puffer fish","Gold fish","Sea horse"]
animals.append("Starfish")
print(animals[2])
animals.remove(animals[0])
for i in animals:
    print i



