import subprocess
import os

def compress_video(input_path, output_path, crf=28):
    try:
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libx264',
            '-crf', str(crf),
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '128k',
            '-y',
            output_path
        ]
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Video compressed successfully! Saved to: {output_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during compression: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")

input_video = "video_sampl1.mp4"
filename= os.path.splitext(input_video)[0]
output_video = f"{filename}compressed_video.mp4"
crf = 30

compress_video(input_video, output_video, crf)
