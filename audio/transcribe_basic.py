import whisper

model = whisper.load_model("small")
result = model.transcribe("qinghuaci.mp3")
print(result["text"])