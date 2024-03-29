#%%
"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from playsound import playsound
import os
from google.oauth2 import service_account
from google.cloud import texttospeech

def speak(words):
    # Instantiates a client
    file_name = os.path.join(os.path.dirname(__file__), 'calhacks-2019-f94792042bb7.json')
    credentials = service_account.Credentials.from_service_account_file('calhacks-2019-f94792042bb7.json')
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=words)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    playsound('output.mp3')
    os.remove("output.mp3")


