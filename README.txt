Introduction:
	I wrote Kadre for myself to make quick Python-based applications. I followed a model-view-
	controller pattern, and while it's just a starting point, I did want to point some things 
	out, in case anyone decided to use it, or wants to add to it.

Dependancies:
	- Python 2.7.3 (32-bit) - may work on 64 bit, I haven't tried.
	- Sqlite version 3.7.13
	- PySide v 1.1.2

Folder System:

	main.py: Runs the program - shouldn't need much editing. Can change the style.

	test.py: Runs the unit tests. If you add unit tests, or change the names, edit Here.

	setup.py: Creates and initializes the database, and the test database, based on the config
		files (tables.json, db_init.json and test_db_init.json) in the \\data folder. If you want 
		to change these, you'll have to edit (database_creator.py and test_db_creator.py) in 
		\\controller.

	kglobals.py: A set of objects or variables that can be created once, and called from anywhere 
		in the program. You could add a "datamapper" object to this, to manage persistance, if 
		the objects don't do that themselves.

\\controller:
	database_creator and test_db_creator: These object pull in the data from the config files in 
		\\data, make the databases, and store them in the \\data\\database folder. For testing 
		and debugging I've found http://sourceforge.net/projects/sqlitebrowser/ , to be super 
		helpful.

	database_manager.py: Handles all the sql statements. I made a convenience query function, 
		which picks the appropriate query statement. I haven't done any performance testing, 
		since the programs I've been writing tend to be small and contained.

\\data
	tables.json: Config file for the database. Name the table, then add the attributes, with 
	their types. Usually "text", "integer", "float", or "blob". There's not a lot of validation 
	here, so be precise.

\\model
Here's where I make my model objects. I did a simple mockup of a tank with some data that might 
be used, just to illustrate how testing might work. 

All it requires is that you set a tagnumber and a maxvolume. The parameters show how I might 
automatically add the "TNK-", and calculate a minvolume automatically from the maxvolume. 

\\tests
These are the unittests. Unittest usually does a setup and teardown for each test. I modded it 
based on Something Meaningful blog (http://stezz.blogspot.com/2011/04/calling-only-once-setup-in-
unittest-in.html), so there's only one setup that can then be used. Add these to test.py to run 
in a suite.

\\utils
A couple of utility functions.
	myjson.py gets the json data into a dictionary
	myPickle.py is for storing data in a "blob" in sqlite, and getting it back. 


\\view
UI Intro:
	Basically, I have a main window, which calls actions on the PageManager, (which is a cusom 
	QStackedWindow). Thate generates the pages (defined in \\pages) on demand, and keeps track of 
	lastpage, nextpage, thispage. You should be able to add as many pages as you want, but you 
	can also use dialogs for quick popup questions, to keep the number of pages down. Once 
	they're made in pagemaker, that's it, there's no re-creating them, but they do refresh, so 
	you can update data, just not change the structure easily.


KMainWindow Setup:
	menu_actions.json and toolbar_actions.json: These are similar, they specify the actions for 
		the menubar and the toolbar respecively.
	
		Some things to note: 
			* I was using a dictionary, and python dictionaries are unordered, so I did a bit of 
			a hack and added in the position attribute. It has to be in order under each menu, 
			like in &File.
			* The paths to the icons are relative to main.py, so you have to include view\\ like 
			shown.
			* You can use "Separators" to add a separator in the menu, or toolbar, as shown.

	To make the buttons and menu selections actually do something, you need to connect the action 
	with a "callback", in the main_window.py (KMainWindow) in the self.actiondict variable. 

	Then you can write the functions in the KMainWindow.

	Once you've specified your pages in \\page, you have to connect them in the pagemanager.py, 
	self.pagedict variable. You have to import the page object by name, and give it a keyword, 
	and the class name to call.

\\view\\pages
	I tried to make defining pages quite simple.
	
	All the pages derive from pages.py Pages class, which is a QWidget. PageManager is what will 
	be constructing them, and it passes itself as it's parent, and gives it the name you gave it, 
	so the __init__ functions should all look pretty similar as far as interface goes. BlankPage 
	is a good example of the simplest version.

	Example:
		To get a form, look at formpage. I'll admit it's not pretty, but it gets the job done. 
		Questions out, input in.

		So, on __init__, page is going to call _setup and then _build. You can overwrite either, 
		set them to pass if you don't want them to do anything, and write something else, but I 
		found this pattern convenient.

		_setup:
			On setup, I define my lists. If I have a combobox, the list gets defined here. The 
			combolist could come from the database, and then you could get it again on refresh. 

			self.formlist is a list of dictionaries, (so this time it maintains it's order).
			Specify:
				"column" - The name you want to refer to it by (I usually make this the same as 
				the column in the database I will store the info in).
				
				"label" - What you want the ui to display.
	
			"type" - Can be:
				- "textenter": label + text entry box, 
				- "checkbox" : a checkbox. Value should be "True" or "False"
				- "button" : if you want a button. 
					-Add a "callback" attribute with the method to call when pressed.
				- "combobox" for a pulldown list selector. 
					- define the "list" attribute, as shown.
			
			"value" - This is the default value you want to show. (button's don't need it).

		_header:
			Simple label for the header. I used some html to style it up a bit. don't forget to 
			add the widget to the layout using self.layout.addWidget(). If you want to get crazy, 
			you can use PyQt documentation to adjust. 

		_center:
			Adds the form to the center of the page. "Form" is a custom widget I made to handle 
			all the setup for me. You can find it in \\view\\widgets. 

			All it needs to create it is the formlist.

		_footer:
			Simple ok, cancel buttons.

		_refresh:
			You may need to adjust this. It should be called when something needs updating, so 
			depending on what you're doing, you may need calls to the database here.

\\view\\assets\\icons
	I got these from http://findicons.com/. Use them, add to them, or replace them.

So that's pretty much it. I've made some convienience widgets with the same type of pattern, 
which are all used in the example pages or popups (except for treeview, I'm still working on that 
one.) It's not pretty, but it's quick to make small apps to help with my engineering gigs. I'll 
work on posting some of those too, as examples. 


Useful references:
Stackoverflow - for all your sotware questions.
Sqlite - http://www.sqlite.org/lang.html
Python - http://docs.python.org/2/
PySide - https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html


