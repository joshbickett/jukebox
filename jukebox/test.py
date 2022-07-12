from sample import run


info = { "artist": "The Beatles", "genre": "Rock", "lyrics": "Once upon a time I found a dime, it was quite find for a kid that's nine"}
run(model='1b_lyrics', name='sample_1b', levels=3, sample_length_in_seconds=20, total_sample_length_in_seconds=180, sr=44100, n_samples=3, hop_fraction=(0.5,0.5,0.125), song_info=info)


