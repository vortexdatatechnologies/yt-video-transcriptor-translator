# YouTube subtitle transcriber and translator

This Python script allows you to transcribe and translate the subtitles of YouTube videos. It uses the YouTube Transcript API to get the subtitles and the Google Translate API for the translation. It separates the script every 4000 characters and then concatenates it, this is due to API limitations.

## Characteristics
- Gets the English or Spanish subtitles for a given YouTube video ID.
- Writes the transcript to a text file.
- Splits the transcript into 4000 character fragments for translation.
- Translates each fragment from English to Spanish using Google Translate.
- Writes the translation to a separate text file.

## Requirements
- Library `youtube_transcript_api` (install with `pip install youtube_transcript_api`).
- deep_translator library (install with `pip install deep_translator`).
- Python 3.6 or higher.

## Use
1. Install the required libraries by executing the following commands:
   
***pip install youtube_transcript_api***

***pip install deep_translator***


2. Replace the `video_id` parameter in the `transcribe_video` function call with the ID of the YouTube video (almost always found at the end of the link, if you don't do some research on it) that you want to transcribe and translate.

<img src='https://github.com/vortexdatatechnologies/yt-video-transcriptor-translator/assets/139167026/b426aad0-9102-4c4c-957b-e662b5ae15a5'>

3. Execute the script.
4. The transcription will be saved in a file named `transcription.txt`, and the translation will be saved in `translation.txt`.

Feel free to customize the code and add more functionality according to your needs.

**Note:** Be sure to comply with the terms of service of YouTube API and translation service provider when using this script.
