# imports ----------------------------------
from gtts import gTTS
from langdetect import detect
from io import BytesIO
# ------------------------------------------

async def make_voice(text: str) -> BytesIO: # making voice from text
    bytes_io: BytesIO = BytesIO()
    gTTS(text=text, lang=detect(text)).write_to_fp(bytes_io)
    bytes_io.seek(0)
    return bytes_io