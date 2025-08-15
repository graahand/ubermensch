#rnd #dream

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
| face_recognition on hold, let's work on jung personality test.                                                                                                                                                | 8/13       |
| onboarding (persona details and personality test) implemented with functional code                                                                                                                            | 8'13       |
| now testing with llama3.2:2b model, isn't a thinking model so good.                                                                                                                                           |            |
| listed out the issues with existing main code files (talk, tts, whisper_streaming_test, onboarding, master_prompt, introduction_user)                                                                         | 13/8       |
| improvements recorded and listed down from existing code                                                                                                                                                      | 13/8       |
| tts requires some work bro, streaming tts                                                                                                                                                                     | 13/8       |
| **900 lines of code review required with comments**                                                                                                                                                           | 15/8       |


## improvements in existing code 8/13

* i didn't found the schema mismatch, check it again if any confusion, don't perform any changes here.
* i don't need the fallbacks for missing files they will be there at any cost. don't need changes here. 
* handle the duplicate user,
* user input data types also should have validation
* database connnection failure doesn't needs error handling but i am concerned about multiple connection variable declared and setup in multiple funciton, i know why it have been done but is that production level? 
* add cleanup for partial insertions. 
* age input should be provided in number, integer.
* working with date is hard i know but add effective and robust parsing the birthdate taken from the user. 
* memory limit don't do that i don't need that
* connection timeout and ollama failed issues doesn't needs any fallback keeps them as it is. 
* for now don't look at tts.py leave it as it is, it needs some work so leave it. 
* for streaming_whisper_test.py instead of global queues what is better what is alternative, list that out or explain that to me. 
* talk.py, add the  conversation context management.
* face_recogntion, leave that, that isn't ready yet
* cleanup the temporary audio files properly. 
* instead of loading whisper model at every transcription call, add resource efficient and robust way, first explain that to me. 
* pool the database connection as well. 
* solve the memory leakage during the audio streaming. 
* filepath hardcoding is fine
* don't add any validation for model availability, it will be there anyhow.
* solve the issue regarding chat history growing unbounded, i don't need pause resume the conversations. 
* don't need authentication between sessions. 
* user's shouldn't be able to go back and change the anaswer its totally intended. 
* currently i  don't want integration just each units. 
* add typehints for the functions where required, 
* data flow should be robust and clear
* instead of loading llm on every request, what else better can be done, but remember resources utilization and time taken for response are also key factors. 
* dont cache the model 
* if the use of global variables is issue, use the better way. 
* don't load the chat history entirely to the memory, just relevant. 
* 


## Notes

1. monotonic timstamps(increasing timestamps(segments) that never decreases or wrap around)
2. assert statement in Python is used to check if a condition is true or not. if the  condition is false, the statement will  raise Assertion Error exception, used for debugging. 
3. Voice activity detectio