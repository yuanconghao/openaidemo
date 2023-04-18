import whisper
import zhconv
import time

time1 = time.time()
model = whisper.load_model("small")
time2 = time.time()
print("model load cost: ", time2 - time1)

result = model.transcribe("./data/svm_30.mp3")
time3 = time.time()
print("model audio convert: ", time3 - time2)

# print the recognized text
text = zhconv.convert(result["text"], 'zh-hans')
print(text)
time4 = time.time()
print("model text convert: ", time4 - time3)