import whisper

model = whisper.load_model("small")
result = model.transcribe("test_en.mp3")
print(result)
