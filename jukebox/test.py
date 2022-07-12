from sample import run

def test(talk_more=False):
    print("test")
    if talk_more: 
      print("Hello, how are you?")

run(model='1b_lyrics', name='sample_1b', levels=3, sample_length_in_seconds=20, total_sample_length_in_seconds=180, sr=44100, n_samples=3, hop_fraction=(0.5,0.5,0.125))
# test(talk_more=True);

