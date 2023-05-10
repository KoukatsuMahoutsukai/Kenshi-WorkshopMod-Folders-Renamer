# Kenshi-WorkshopMod-Folders-Renamer
This tool automatically renames workshop mod folders to match their corresponding .mod file name, which is necessary for editing via FCS and offline play. Normally, workshop mod folders are identified by their ID, such as "steamapps\workshop\content\233860\1621026948\Profitable Slavery.mod," but this format is not editable or playable offline. With this tool, the folder format will be changed to "Profitable Slavery\Profitable Slavery.mod."

Here's how to use it:

1.	Copy the workshop mods you want to rename to a new folder(preferably a new folder on desktop? or on somewhere where there isnt write protection).
2.	Run the .exe or .py file from an IDE.
3.	Click "Select Folder" and choose the folder containing the mods you copied.


Notes:

-	The tool works by using the .mod file name inside the folder.
- Make sure you have permissions to rename the workshop mod folders.
-	The program will skip folders that contain more than one .mod file, as well as folders that do not have a .mod file at all. Additionally, if the selected folder is located within the "workshop\content" directory, it will   also be skipped.
-	Running the tool directly on "steamapps\workshop\content\233860\1621026948" will also be skipped.
-	After renaming, copy the folders to the "Kenshi\mods" folder if you plan to edit them via FCS or play offline. Be aware that conflicts may arise if a mod is - both in the "mods" folder and subscribed to via workshop? if     you plan to unsubscribe from the workshop mods maybe leave a favorite and like
