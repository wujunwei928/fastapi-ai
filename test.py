import asyncio
import time

import ollama
import whisper


def test_whisper():
    t1 = time.time()
    model = whisper.load_model("small")
    t2 = time.time()
    print(f"Model loaded in {t2 - t1:.2f} seconds")

    result = model.transcribe("data/test_en.mp3", verbose=False)
    t3 = time.time()
    print(f"Transcribed in {t3 - t2:.2f} seconds")
    print(result)

    result = model.transcribe("data/test.mp3", verbose=False, initial_prompt="使用简体中文输出")
    t4 = time.time()
    print(f"Transcribed in {t4 - t3:.2f} seconds")
    print(result)

    print(whisper.available_models())


def test_ollama():
    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": "what is your name?",
            },
        ],
    )
    print(response["message"]["content"])


async def chat():
    message = {"role": "user", "content": "Why is the sky blue?"}

    client = ollama.AsyncClient(host="http://localhost:11434", timeout=1000)
    # OLLAMA_HOST

    response = await client.chat(model="phi3", messages=[message])
    print(response)


asyncio.run(chat())
