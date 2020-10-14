# wav 파일 재생하기_pyaudio
import pyaudio
import wave

chunk = 1024
path = "The-Avengers-Theme-Song.wav"

with wave.open(path, 'rb') as f:
    p = pyaudio.PyAudio()
    pyaudio.stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(chunk)
    
    while data:
        pyaudio.stream.write(data)
        data = f.readframes(chunk)

    pyaudio.stream.stop_stream()
    pyaudio.stream.close()

    p.terminate()