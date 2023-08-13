import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display as display
import csv


numbers1 = []
with open('10numbers.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

numbers1.append(10)
x = 0
for i in data[0]:
    if x != 0:
        numbers1.append(int(i))
    x+=1


numbers2 = []
with open('1000numbers.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

numbers2.append(10)
x = 0
for i in data[0]:
    if x != 0:
        numbers2.append(int(i))
    x+=1

numbers3 = []
with open('millionnumbers.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

numbers3.append(10)
x = 0
for i in data[0]:
    if i != ' ':
        if x != 0:
            numbers3.append(int(i))
    x+=1


count = 0
def main():
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))
    display.filebox.add_options(['thousand', 'million', 'ten'])
    current_alg = None
    alg_iterator = None
    current_file = None
    file_iterator = None

    timer_delay = time()
    global  count

    menu = True
    menu2 = False
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                menu2 = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False
                    menu2 = True
        display.screen.fill(display.white)
        start_message = [
            "                                           ",
            "                                           ",
            "                                           ",
            "       press 'ENTER' to start"
            ]
        y = 80
        font1 = pygame.font.SysFont("console", 24)

        for i in start_message:
            text = font1.render(i, False, display.black)
            display.screen.blit(text, (150,y))
            y += 80
        pygame.display.update()

    while menu2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu2 = False
                running = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu2 = False
                    running = True
        display.screen.fill(display.black)
        start_message = [
            "                                           ",
            "                                           ",
            "                                           ",
            "   Made By Sumsam and Bahadur",
            "           Press Enter "
            ]
        y = 80
        font1 = pygame.font.SysFont("console", 24)

        for i in start_message:
            text = font1.render(i, False, display.white)
            display.screen.blit(text, (150,y))
            y += 80
        pygame.display.update()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.updateWidgets(event)
        
        if display.playButton.isActive: # play button clicked
            display.playButton.isActive = False
            display.do_sorting = True
            current_alg = display.algorithmBox.get_active_option()
            current_file = display.filebox.get_active_option()
            # display.numBars = int(display.sizeBox.text)

            if current_alg == 'bonus algo':
                if current_file == 'ten':
                    display.numBars = 10
                    numbers = [x for x in numbers1] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator
                
                elif current_file == 'thousand':
                    display.numBars = 1000
                    numbers = [x for x in numbers2] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

                elif current_file == 'million':
                    display.numBars = 1000000
                    numbers = [x for x in numbers3] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

            else:
                if current_file == 'ten':
                    display.numBars = 10
                    numbers = [x for x in numbers1] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator
                
                elif current_file == 'thousand':
                    display.numBars = 1000
                    numbers = [x for x in numbers2] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator
                  
                elif current_file == 'million':
                    display.numBars = 1000000
                    numbers = [x for x in numbers3] # random list to be sorted
                    alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        if display.stopButton.isActive: # stop button clicked
            display.stopButton.isActive = False
            display.do_sorting = False
            display.paused = False
            try: # deplete generator to display sorted numbers
                while True:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
            except StopIteration:
                pass

        if display.do_sorting and not display.paused: # sorting animation
            
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer_delay = time()
                    count+=1
            except StopIteration:
                display.do_sorting = False
        elif display.do_sorting and display.paused: # animation paused
            display.drawInterface(numbers, -1, -1, -1, -1)
        else: # no animation
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)

    with open('sorted.txt', 'w') as f:
        for i in numbers:
            f.write(str(i))
            f.write(", ")

if __name__ == '__main__':
    main()
    # print(numbers)
    print(count)
