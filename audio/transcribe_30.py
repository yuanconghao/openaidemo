import whisper
import zhconv
import time

time1 = time.time()
# tiny base small medium large
#model = whisper.load_model("small", in_memory=True)
model = whisper.load_model("small", in_memory=True)
time2 = time.time()
print("model load cost: ", time2 - time1)

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("./data/svm_30.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")
time3 = time.time()
print("model data preprocess: ", time3 - time2)

# decode the audio
options = whisper.DecodingOptions(fp16 = False, language='zh', without_timestamps=True)
result = whisper.decode(model, mel, options)
time4 = time.time()
print("model audio convert: ", time4 - time3)

# print the recognized text
text = zhconv.convert(result.text, 'zh-hans')
print(text)
time5 = time.time()
print("model text convert: ", time5 - time4)
