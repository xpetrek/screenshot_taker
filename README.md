# screenshot_taker
Short script for capturing whole displays or small portion of a display. 
1) Script provides 5 second delay for the user to focus the screenshotted document. 
2) Program will take screenshot or either small portion of the window or the full display based on specified arguments. 
3) Program waits 1 second
4) Program will turn document to the next page via "right arrow" and then repeats step 2.
5) After the specified amount of pages is screenshotted program stops. 


# Usage
Run either python script or .exe app in command line with following arguments:


Mandatory:
*  -p PAGES, --pages     Length of the document in pages!

Optional:
*  -l LEFT, --left       Left offset of the screenshot area!
*  -t TOP, --top         Top offset of the screenshot area!
*  -w WIDTH, --width     Width of the screenshot area!
*  -v HEIGHT, --height   Height of the screenshot area!

In case that all the optional parameters are not set, the application will take screenshot of the whole window.