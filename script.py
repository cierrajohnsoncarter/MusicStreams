songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations",
         "Blinding Lights", "Fast", "Everybody Dies in Their Nightmares",
         "Snowchild"]
playcounts = [78, 29, 44, 21, 89, 5, 100, 63, 105, 95]

pairs = list(zip(songs, playcounts))

plays = {key: value for key, value in pairs}

# print(plays)

# Songs with how many times they are streamed
plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

# print(library)


def top_5_songs():
    print(pairs.sort())


#print(f"Your Top 5 Most Played Songs Are:{top_5}")
