songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations",
         "Blinding Lights", "Fast", "Everybody Dies in Their Nightmares",
         "Snowchild"]
playcounts = [78, 29, 44, 21, 89, 5, 100, 63, 105, 95]

# Turned pairs into a list
pairs = list(zip(songs, playcounts))

# Sorts songs by 5 most played at the value
top_5_pairs = sorted(list(zip(songs, playcounts)),
                     key=lambda song: song[1])[-5:]

# Reverses the list to show top 5 songs from most to least played
top_5_pairs.reverse()

plays = {key: value for key, value in pairs}

# print(plays)

# Added songs with how many times they are streamed
plays["Purple Haze"] = 1
plays["Respect"] = 94
plays["Until I Bleed Out"] = 200
plays["Starstuck"] = 45
plays["Love Like Whoa"] = 85

library = {"The Best Songs": plays, "Sunday Feelings": {}}

# print(library)


# Formatting for printing top 5 streamed songs
print(f"Your Top 5 Most Played Songs Are: {top_5_pairs}")
