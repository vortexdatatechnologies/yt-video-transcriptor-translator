from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator

def transcribe_video(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
        except:
            print("No se encontraron subtítulos en inglés o español para este video.")
            return

    # Abre el archivo en modo de escritura. Se creará si no existe.
    with open('transcripcion.txt', 'w', encoding='utf-8') as f:
        for entry in transcript:
            # Escribe cada línea de la transcripción en el archivo.
            f.write(entry['text'] + ' ')

    # Abre el archivo de transcripción y lee su contenido
    with open('transcripcion.txt', 'r', encoding='utf-8') as f:
        transcript_text = f.read()

    # Fragmenta el texto en fragmentos de 4000 caracteres
    fragments = [transcript_text[i:i+4000] for i in range(0, len(transcript_text), 4000)]

    # Traduce cada fragmento y escribe la traducción en el archivo de traducción
    with open('traduccion.txt', 'w', encoding='utf-8') as f:
        for fragment in fragments:
            translation = GoogleTranslator(source='en', target='es').translate(fragment)
            f.write(translation)

transcribe_video('JRXTyUu4yC8')
