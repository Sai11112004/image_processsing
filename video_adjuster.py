import subprocess
import os

def adjust_video_dimensions(input_path, output_path, width=None, height=None):
    try:
        probe_cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height',
            '-of', 'csv=s=x:p=0',
            input_path
        ]
        
        result = subprocess.run(probe_cmd, capture_output=True, text=True)
        original_width, original_height = map(int, result.stdout.strip().split('x'))
        
        if width and height:
            new_width = width
            new_height = height
        elif width:
            new_width = width
            new_height = int((width / original_width) * original_height)
        elif height:
            new_height = height
            new_width = int((height / original_height) * original_width)
        else:
            print("Please specify either width or height")
            return
        
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale={new_width}:{new_height}',
            '-c:a', 'copy',
            '-y',
            output_path
        ]
        
        subprocess.run(ffmpeg_cmd, check=True)
        
        print(f"Video resized successfully!")
        print(f"Original dimensions: {original_width}x{original_height}")
        print(f"New dimensions: {new_width}x{new_height}")
        print(f"Saved to: {output_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during video processing: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")

input_video = "video_sampl1.mp4"
output_video = "resized_video.mp4"
width = 426
height = 240

adjust_video_dimensions(input_video, output_video, width, height)
