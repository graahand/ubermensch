
installed langchain and tavily search
used the ollama api directly without using the ollama python package. 
model answers directly, currently using gemma:2b


| task                                                                                                                                                                                                          | date       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| installed langchain and tavily search                                                                                                                                                                         | 8/2        |
| used the ollama api directly without using the ollama python package.                                                                                                                                         | 8/2        |
| model answers directly, currently using gemma:2b                                                                                                                                                              | 8/2        |
| tavily search api key: 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                                                                                                                                              | 8/2        |
| used the .env file to save the api key.                                                                                                                                                                       | 8/2        |
| every response is a sentence for speaking out in humanly way possible using tts.                                                                                                                              | 8/3        |
| tested tts with kokoro tts (found the readme file for voices along with the ISTFT(like extracting frames from videos but for audio), sampling rate(higher the sampling rate, better the audio sounds))        | 8/4        |
| streaming tts for real time llm response to speech conversion for robot (possible models picovoice(api), xtts v2, kyutai tts(allow cloning voice with 6 second clip))                                         | 8/5        |
| NousResearch hermes 3b model tested, don't have any idea how it is better or worse, needs more testing                                                                                                        | 8/5        |
| tts with kokoro completed but have issue with length of text it can synthesize at a time (500 characters).                                                                                                    | 8/5        |
| installation of xtts text-to-speech requires (pip install TTS)                                                                                                                                                | 8/6        |
| whisper, faster-whisper, whisper-cpp researched, faster whisper is  top contender whisper is heavy and faster-whisper report claims whisper cpp  memory usage is  higher. So first  testing on faster-whisper | 8/6        |
| **whisperX, whisper-ctranslate2, whisper_streaming, whisperlive needs some research on these as well**                                                                                                        | 8/6        |
| fasterwhisper tested with a audio sample, real time streaming test remains                                                                                                                                    | 8//6, 8/10 |
| streaming whisper worked perfectly fine for transcribtion.                                                                                                                                                    | 9/8        |
| **face recognition (who is who, cosine similarity) written code, needs to test with 10 images of a person for identification**                                                                                | 10/8       |
| personality test jung personality.                                                                                                                                                                            | 9/9        |
| pymupdfllm for rag and llms not researched enough and not even tested from reddit post.                                                                                                                       | 9/9        |
| [marker pdf parser](https://github.com/datalab-to/marker) test this as well for parsing pdf as markdown and json                                                                                              | 9/9        |

1. monotonic timstamps(increasing timestamps(segments) that never decreases or wrap around)
2. assert statement in Python is used to check if a condition is true or not. if the  condition is false, the statement will  raise Assertion Error exception, used for debugging. 
3. Voice activity detection
4. 