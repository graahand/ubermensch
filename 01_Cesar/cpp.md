1. cpp ma kunai variable ko value deko xaina vane (initialize gareko) xaina vane tesko value python ma jasto default value datatype jassari hudena rather memory address ma vako garbage value hunxa default value. yesto  variables lai uninitialized variables vaninxa. 
2. unused variables haru le garda compilation error  aauna sakxa. 
3. g++ le cpp program compile garda aauna sakne error vaneko chai gcc lai c++ ko std libraries haru kaha  hunxa thahahudena. 
4. c++ ko some famous compilers haru chai g++, ms visual c++, clang++, mingw-g++  haru hun.
5. LLVM (Low level virtual machine) euta framework ho compilers haru banaune sanga related rw esle nai clang++ rw clang compilers haru banayeko ho. 
6. compilers haru le standard follow nagarerw programming easier hune tarika le pani banayeko hunxa jasle garda, error aauna sakne thauma pani error naauna sakxa but  that's not accoridnt o the standard of Cpp
7. cpp ko 92 ota words haru chai as a reserved keywords ko lagi use gareko xah. like alignas, alignof, bool, break, nullprt, not, namespace, switch, try and so on.
8. ani identifiers haru pani xah jastai *overide, final, import and module* jun chai keywords chai haina but specific thau ma use garda kheri chai specfic meaning dinxa, kaam garxa. 
9. tarw cpp ma variable ko name lai pani identifier vanxa, identifier banauda reserved keywords, symbols, whitespace use garnu vayena ani number dekhi start hunu vayena nam along  with cpp chai case sensitive xah.
10. the C++ standard library uses the underscore method for both variables and functions. Sometimes you’ll see a mix of the two: underscores used for variables and intercaps used for functions
11. cpp ma lekhda whitespace jasto rakheko xas testai print hunxa. 
12. cpp whitespace independent langauge ho kina vane testo formatting restrictions haru cpp le rakheko xaina. 
13. In general programming, an **expression** is a non-empty sequence of literals, variables, operators, and function calls that calculates a value
14. cpp ma header vfile vaneko table of contents or blueprint jasto file ho jaha different  functions haru name ani parameters haru mentioned hunxa, class definitions haru  ni included hunxa ani yo file lai chai .cpp file le call garxa for actual implementation. 
15. 




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


