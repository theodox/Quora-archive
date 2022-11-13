# Why does Unreal Editor stay stuck at 45% when loading, and how do I fix it?

	author: Steve Theodore
	written: 2021-03-11
	views: 505
	upvotes: 2
	quora url: /Why-does-Unreal-Editor-stay-stuck-at-45-when-loading-and-how-do-I-fix-it/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


45% is typically [where it sticks while compiling shaders](https://answers.unrealengine.com/questions/966233/editor-stuck-at-45-frozen-and-not-compiling-shader.html). Unfortunately there’s not necessarily one particular reason : there are a number of things that can cause a shader recompile — most are legit but some are bugs.

You can at least take a look at your task manager to see if the Unreal Shader Compiler Worker process is hanging or actually working: sometimes its not hung, its just chewing through a lot of shaders without updating the progress bar.

This [answer](https://forums.unrealengine.com/community/general-discussion/1683076-compiling-shaders-doesn-t-work-stuck-with-no-progress) suggests you might be able to disable parallel shader compiling (“XGE”). [This one ](https://answers.unrealengine.com/questions/790929/shader-compiling-really-slow.html?sort=oldest)suggests maybe you can bump the priority on the compiler process. Unfortunately there are so many variables that there’s not one right answer.

