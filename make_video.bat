set odbpath=%1
set moviename=%2
set ffmpeg="ffmpeg.exe"
echo Y | call %ffmpeg% -framerate 30 -i "%odbpath%\\images\img-%%3d.png" -preset slow -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 4500k -minrate 4500k -maxrate 9000k -bufsize 9000k -vf tpad=stop_mode=clone:stop_duration=1  "%odbpath%\%moviename%.mp4"

