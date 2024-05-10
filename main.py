import fitz
from gtts import gTTS
from playsound import playsound
import os

def extract_text_from_pdf(pdf_file: str) -> [str]:
    pdf_text = []
    with fitz.open(pdf_file) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text = page.get_text()
            pdf_text.append(text)
    return pdf_text

def text_to_speech(text_list):
    for text in text_list:
        # Create a gTTS object
        tts = gTTS(text=text, lang='en')

        # Save the audio file
        tts.save("output.mp3")

        # Play the audio file
        playsound("output.mp3")

        # Delete the audio file after playing
        os.remove("output.mp3")

def process(file_name):
    texts = extract_text_from_pdf(file_name)
    text_to_speech(texts)

process("sample2.pdf")