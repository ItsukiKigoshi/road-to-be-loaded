import json

import math
import pyaudio

# Play Google Loading Sound
google_log_dict = []
with open('log/1-google/www.google.com-recording.json') as json_file:
    data = json.load(json_file)
    records = data['recording']['records']
    for record in records:
        try:
            google_log_dict.append({"type": record['type'], "startTime": record['startTime'], "endTime": record['endTime']})
        except:
            print("Time is not found: ",record['type'])

print(f'{google_log_dict=}')

# Create Audio
PyAudio = pyaudio.PyAudio

bitrate = 16000
frequency = 500
length = 1

bitrate = max(bitrate, frequency+100)

num_of_frames = int(bitrate * length)
rest_frames = num_of_frames % bitrate
wave_data = ''

for x in range(num_of_frames):
 wave_data = wave_data+chr(int(math.sin(x/((bitrate/frequency)/math.pi))*127+128))

for x in range(rest_frames):
 wave_data = wave_data+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = bitrate,
                output = True)

stream.write(wave_data)
stream.stop_stream()
stream.close()
p.terminate()
