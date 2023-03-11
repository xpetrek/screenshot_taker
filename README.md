# screenshot_taker
Short script for capturing whole displays or small portion of a display. 
1) Script provides 5 second delay for the user to focus the screenshotted document. 
2) Program will take screenshot or either small portion of the window or the full display based on specified arguments. 
3) Program waits 1000ms (if not specified otherwise)
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
*  -s SLEEP, --sleep   Time in between each screenshot. (default set to 1000ms)!
*  -d DIRECTORY, --dir   Specify name of the directory to put the screenshots in.

## Example: 
```
//Program will take 90 whole display screenshots 
./screenshoter.exe -p 90
//Program will take 90 screenshots with window 400 by 400 with an offset of 100 from top and left with 500ms delay in between screenshots and it will save the images to the MYSCREENSHOTS directory
./screenshoter.exe -p 90 -l=100 -t=100 -w=400 -v=400 -s=500 -d=MYSCREENSHOTS

//Program will take 90 whole display screenshots 
python ./screenshoter.py -p 90
//Program will take 90 screenshots with window 400 by 400 with an offset of 100 from top and left. 
python ./screenshoter.py -p 90 -l = 100 -t = 100 -w = 400 -v = 400


```
In case that all the optional parameters are not set, the application will take screenshot of the whole window.