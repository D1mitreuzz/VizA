import lyricsgenius

genius = Genius()
artist = genius.search_artist("Fox Stevenson", max_songs=5, 
                                                    sort="title", include_features=True)
print(artist.songs)
