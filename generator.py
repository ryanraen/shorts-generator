import subprocess
import whisper

output_dir = "data/"

# EXTRACT AUDIO FILE
def extract_audio(video_path):
    output_audio_path = output_dir + "test_video_audio.wav"

    # ffmpeg audio extraction command
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_audio_path
    ]

    # run command
    failure = subprocess.call(command)
    if failure:
        print("Audio extraction failed.")
    else:
        print("Audio successfully extracted to " + output_audio_path)
        
# EXTRACT TRANSCRIPT FROM AUDIO
def extract_transcript(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    # result['segments'] gives timestamps + text
    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        print(f"[{start:.2f} - {end:.2f}] {text}")

    return result['segments']
        
# test
# extract_audio("data/test_video.webm")

# print(extract_transcript("data/test_video_audio.wav"))
