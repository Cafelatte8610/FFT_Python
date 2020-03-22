import pyaudio
import numpy as np
from matplotlib import pyplot as plt

time=1           # 時間[s]
samplerate = 44100  # サンプリングレート
fs = 1024           # フレームサイズ

def record(index, samplerate, fs, time):
    pa = pyaudio.PyAudio()
    data = []
    dt = 1 / samplerate
    
        stream = pa.open(format=pyaudio.paInt16, channels=1, rate=samplerate,
                     input=True, input_device_index=index, frames_per_buffer=fs)
    
    for i in range(int(((time / dt) / fs))):
        frame = stream.read(fs)
        data.append(frame)

    stream.stop_stream()
    stream.close()
    pa.terminate()
    data = b"".join(data)
    
    return data, i

wfm, i = record( 1, samplerate, fs, time)
plt.figure(figsize=(15,3))
plt.xlabel('time [s]',fontsize="10")
npwfm=np.frombuffer(wfm, dtype="int16")
plt.plot(npwfm)
plt.show()
plt.close()
x = np.fft.fft(npwfm)
x_abs=abs(x)
plt.plot(x_abs[44:500])
print(np.argmax(x_abs[44:500]))
plt.show()
