from pathlib import Path
import numpy as np
import soundfile as sf
from app import preprocess_audio, gemini_transcribe

RAW = Path('khmer_stt_data/raw_audio')
RAW.mkdir(parents=True, exist_ok=True)
file = RAW / 'test_silence.wav'
# 1 sec 16000 Hz silence
sr = 16000
data = np.zeros(sr, dtype=np.float32)
sf.write(str(file), data, sr)

print('raw file', file, file.exists())
clean = preprocess_audio(file)
print('clean', clean)
try:
    payload = gemini_transcribe(clean)
    print('payload', payload)
except Exception as e:
    import traceback
    print('Exception', e)
    traceback.print_exc()