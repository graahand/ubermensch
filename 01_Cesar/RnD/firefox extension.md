1. so every extension contain a manifest.json(name, version, permission, which file to run) file which consist of the configuration for the extension. manifest files have different versions/standard, currently used version is V2 but seems like V3 is the future standard. 
2.  the folder structure for the project.
	1. root-folder
		1. manifest.json
		2. popup.html
		3. popup.js.
		4. popup.css
		5. background.js
		6. content-scripts
			1. content.js
		7. icons
			1. icon48.jpg
3. firefox extensions are built with WebExtensions-API, a modern cross-browser system that even Chrome and  Edge use. These extensions are nothing but html, css and js. 
4. action vanne kura chai manifest.json file ma sabse important hunxa jasle k kura execute garne ho vanne kura decide garxa or specific js file batw kei kura execute garxa like popup nikalne or tyo extension ma click garepaxi dark theme enabled hune jasto kura haru. 
5. firefox le chai browser.storage vanne functionality dinxa jasle chai data haru store garne thau dinxa. 
6. [mdn webextension guide](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)
7. means that you can do a lot more in an extension than you can with code in a web page.



## plan for pomodoro extension development

Develop a firefox extension that is basically a implements pomodoro timer. Each pomodoro session is 25 minutes long followed by 5 minute break and after every 4 pomodoro sessions there is a long break of 15 minutes. 

Color specification for the extension popup: use transparent bluish theme for extension with a normal size of popup window. 

Features: Pomodoro Timer and Saving the statistics of the pomodor sessions which should be extracted as a csv for pdf file, the stats should also contain the visualization along with the actual stats. 

