with open("Prob045.in.txt") as f:
    f.readline()
    lines = f.readlines()
    while lines:
        n = int(lines.pop(0))
        print(n)
        artists = {}
        for j in range(n):
            (song, artist) = lines.pop(0).split("-")
            if artist.replace("The ", "") in artists:
                artists[artist.replace("The ", "")].append(song)
            else:
                artists[artist.replace("The ", "")] = [song]
        artists = {key:artists[key] for key in sorted(artists)}
        for artist in artists:       
            for song in sorted(artists[artist]):
                print(song + "-" + artist)
            


            