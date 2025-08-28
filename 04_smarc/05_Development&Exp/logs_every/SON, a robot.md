#rnd #dream

installed langchain and tavily search
used the ollama api directly without using the ollama python package. 
model answers directly, currently using gemma:2b

Tr@nsformer#9008

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
## code review and debug
#### talk
1. session creation for ollama endpoint
2. prompt file path and model file 
3. context keeping with last 10 conversation
4. consideration for system message and user's message.
5. clearing conversation history
6. loading and reading system prompt
7. conversation with model via ollama
8. stream is set to true (one word after another)
9. weather information formatting (preprocessing gibberish)
10. searching the web using tavily search api. 
11. making the response speakable 
12. main function that quit the session with keywords like exit ,quit and q.
13. searching based on different keywords, instead of knowing the feel or the understanding 
#### onboarding
1. database path, named user_profiles.db
2. imported the chatting and loading system prompt function from talk
3. creates database connection sqlite3.
4. checks duplicate users with a sql command
5. database created with the column name, their datatype for user's information and chat history.
6. loads introduction_config file for personality check.
7. save the user's profile, what if it isn't completed?
8. save the chat messages as chat history, adding user's id, role and content. 
9. loads recent chat history,this type of code is also placed at talk.py, 20 conversations. 
10. calculates the personality entf, enjf, intf and so on. 
11. parsing the birthday correctly from users., taking different date formats.
12. validates the date range for month, year and day, also considered that feb have only 29 days. 
13. complete onboarding process for filling out the database with the information taken from user during onboarding
14. additional logics for full name, nickname and age keepipng rest of the information as it is.
15. validation for user's nickname and name.
16. ask for birthday separately if not captured in questions. 
17. then comes personality assessment. 
18. added information to the personalized master prompt with collected information about personality and personal. 
19. nickname at index 2, birthday at 4 and personality type is at 11. 

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

## cpp inference

AVX/AVX-512: advanced vector extensions, set of cpu instructions which allow CPU to perform SIMD (single intruction, multiple data) operations (Think of it like carrying **8 buckets of water in one go** instead of carrying them one by one.)

avx-512 extended version of avx which uses 512-bit registers so it can process double amount of data compared to avx. consumers chips of intel doesn't support avx-512 but server-chips support that. 

arm neon is a ARM's version of SIMD but for arm devices like smartphones, raspberry pi and jetson M-series. 

ggml is a c library for fast inference of AI models on CPU without any frameworks like pytorch or tensorflow 

### executorch 
#### simd
- CPUs have **vector registers** (wide slots that can hold multiple numbers).
- For example:
    - Normal register → holds **1 number** (say, 32-bit float).
    - SIMD register (128-bit NEON, 256-bit AVX, 512-bit AVX-512) → can hold **4, 8, or 16 numbers** at once.
#### nvidia variant of simd is simt for GPUs.
It’s kind of like SIMD, but instead of just “one wide register,” you have **many lightweight threads all running in lockstep (means **all units move together at the same pace, doing the same instruction at the same time**.)** .
- A **core (student)** works on **threads (homework problems)**.
- To solve each problem, the student uses their **registers (notebook)** to write calculations.
- If the notebook fills up, they have to run to the **library (RAM)**, which takes more time.

**register** is a very small, ultra-fast piece of storage **inside a core**

## august 28

[research grade tts, festival](https://www.cstr.ed.ac.uk/projects/festival/)

1. essential build packages
   `sudo apt-get update && sudo apt-get install -y build-essential cmake libasound2-dev libcurl4-openssl-dev pkg-config`
	`sudo apt-get install -y libcurl4-openssl-dev pkg-config libasound2-dev`

2. cpp ma header vfile vaneko table of contents or blueprint jasto file ho jaha different  functions haru name ani parameters haru mentioned hunxa, class definitions haru  ni included hunxa ani yo file lai chai .cpp file le call garxa for actual implementation. 

### cmake learn

1. `cmake_minimum_required(VERSION 3.16)` set minimum version for CMake, kei features haru naya CMake ko version ma matrai hunxa josle garda version specify garnu parxa. 
2. `project(VoiceAssistant` yo chai project ko name set garaxa, project anusar rakhnu parxa yo nam chai.
3. `set(CMAKE_CXX_STANDARD 17` yesle chai program lai or system lai jun C++ version chainxa tei set garxa.
4. `find_package(PkgConfig REQUIRED` `find_package(CURL REQUIRED` yo duita line le chai CMake lai installed libraries haru kaha xa herna vanxa. aba yeha chai CURL  vetena vane build fail hunxa tesari aru dependency pani rakhna milyo instead of CURL.
5. `include_directories(${CMAKE_SOURCE_DIR}/external)` yo line le chai headers file .h/.hpp files haru kaha xa vanerw specify gardinxa, {CMAKE_SOURCE_DIR} vaneko chai project ko root ho.
6. `set(main.cpp audio_manager.cpp transcriber.cpp llm_client.cpp voice_assistant.cpp`  yo line le chai sabai source files haru list garxa, dherai files haru specify garnu thauna files haru lai  module anusar group garnu parxa.
7. `add_executable(voice_assistant${sources})` yo line le chai kun chai program build garne ho vanerw define garxa, vaneko binary file ko name specify garinxa, `${SOURCES}`  le chai sabai cpp files haru mathi lekheko kura haru include garxa.
8. `target_link_libraries)voice_assistant
	CURL::libcurl
	pthread
	asound `
	yo line le chai sabai external libraries haru include garxa use garan ko lagi, libcurl chai httprequest ko lagi, pthread multithreading ko lagi ani asound chai ALSA audio Linux ma. yesko thauma aru libraries haru ni huna sakyo jun chainxa like *whisper.cpp*.
