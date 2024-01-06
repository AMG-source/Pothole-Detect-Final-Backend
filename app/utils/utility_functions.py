from moviepy.editor import VideoFileClip

def avi_to_mp4(input_file, output_file):
    try:
        # Load the AVI video file
        video_clip = VideoFileClip(input_file)

        # Write the video clip to a new MP4 file
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
        
        print(f"Conversion successful. MP4 file saved at: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")