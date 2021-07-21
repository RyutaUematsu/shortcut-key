from google.cloud.speech_v1p1beta1 import SpeechClient, types

from settings import SST_METADATA, SST_BOOT_WARD, SST_LANG, SST_MODEL, PYAUDIO_RATE
from typing import List


client = SpeechClient()

config = types.RecognitionConfig(
    encoding=types.RecognitionConfig.AudioEncoding.LINEAR16,
    metadata=SST_METADATA,
    sample_rate_hertz=PYAUDIO_RATE,
    language_code=SST_LANG,
    model=SST_MODEL,
    speech_contexts=SST_BOOT_WARD
)

streaming_config = types.StreamingRecognitionConfig(
    config=config,
    single_utterance=True)


def sst(frame: List) -> str:
    try:
        resps = client.streaming_recognize(config=streaming_config, requests=(
            types.StreamingRecognizeRequest(audio_content=content) for content in [b''.join(frame)]), timeout=2)
        for resp in resps:
            for result in resp.results:
                alternatives = result.alternatives
                for alternative in alternatives:
                    text = alternative.transcript
        print(f'Recognize -> {text}')
        return str(text)
    except:
        print("Cannot recognize")