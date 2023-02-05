import argparse
import pyautogui
import time

parser = argparse.ArgumentParser(description='Input arguments for screenshoter script!')
parser.add_argument('-p', '--pages', type=int, required=True, help='Length of the document in pages!')
parser.add_argument('-l', '--left', type=int, required=False, help='Left offset of the screenshot area!')
parser.add_argument('-t', '--top', type=int, required=False, help='Top offset of the screenshot area!')
parser.add_argument('-w', '--width', type=int, required=False, help='Width of the screenshot area!')
parser.add_argument('-v', '--height', type=int, required=False, help='Height of the screenshot area!')
args = parser.parse_args()

# left, top, width, height = 530, 190, 600, 820
left = args.left
top = args.top
width = args.width
height = args.height
region = (left, top, width, height)


print(f'Now you will have 5 seconds to focus the PDF document')
for i in range (5): 
  time.sleep(1)
  print(5-i)

if (left == None or top == None or width == None or height == None):
  for i in range (args.pages): 
    time.sleep(1)
    myScreenshot = pyautogui.screenshot()
    pyautogui.press('right')
    myScreenshot.save(f'test{i}.png')
    print(f'Program took a screenshot of page {i}')
else: 
  for i in range (args.pages): 
    time.sleep(1)
    myScreenshot = pyautogui.screenshot(region=region)
    pyautogui.press('right')
    myScreenshot.save(f'test{i}.png')
    print(f'Program took a screenshot of page {i}')