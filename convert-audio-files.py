from pydub import AudioSegment

def convert_ogg_to_wav(ogg_file, wav_file):
    """Converts an OGG file to WAV format."""

    audio = AudioSegment.from_ogg(ogg_file)
    audio.export(wav_file, format="wav")


def main():
    ogg_file = "your_audio_file.ogg"
    wav_file = "output_audio_file.wav"
    convert_ogg_to_wav(ogg_file, wav_file)


if __name__ == "__main__":
    main()
