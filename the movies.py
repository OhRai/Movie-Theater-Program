# ------------------- Imports the pygme library ---------------------------------------------- #
import pygame, sys

from pygame.constants import MOUSEBUTTONDOWN
# initializes the modules of pygame
pygame.init()

# ------------------- Screen settings -------------------------------------------------------- #
# sets the window size to 1200x700 pixels
size = width, height = 1200, 600
screen = pygame.display.set_mode(size)

# background colour
backgroundColour = [0, 66, 114]

# sets window name
pygame.display.set_caption("The Movies")

# ------------------------- Images ----------------------------------------------------------- #
# loads images by using files in the folder and the file name
popcorn = pygame.image.load('popcorn icon.png')
title = pygame.image.load('title.png')
shrek = pygame.image.load('shrek.jpg')
cars = pygame.image.load('cars.jpg')
avng1 = pygame.image.load('avng infinity.jpg')
avng2 = pygame.image.load('avng end.jpg') 

# (popcorn icon) - scales the image down smoothly, sets x and/or y position if needed
popcorn1 = pygame.transform.smoothscale(popcorn, (100, 100))
popcorn_rect1 = popcorn.get_rect()
    
popcorn2 = pygame.transform.smoothscale(popcorn1, (100, 100))
popcorn_rect2 = popcorn.get_rect()
popcorn_rect2.x = width - 100

# (movie images)
# (shrek)
shrekimg1 = pygame.transform.scale(shrek, (175, 175))
shrek_rect1 = shrek.get_rect()
shrek_rect1.x = 110
shrek_rect1.y = height/2 - 90

shrekimg2 = pygame.transform.scale(shrekimg1, (175, 175))
shrek_rect2 = shrek.get_rect()
shrek_rect2.x = 915
shrek_rect2.y = height/2 - 90

# (cars)
carsimg = pygame.transform.smoothscale(cars, (125, 125))
cars_rect = cars.get_rect()
cars_rect.x = 130
cars_rect.y = height/2 + 110

# (avengers infinity war)
avng1img = pygame.transform.smoothscale(avng1, (175, 175))
avng1_rect = avng1.get_rect()
avng1_rect.x = 515
avng1_rect.y = height/2 - 90

avng2img = pygame.transform.smoothscale(avng2, (125, 125))
avng2_rect = avng2.get_rect()
avng2_rect.x = 535
avng2_rect.y = height/2 + 110

# (avengers endgame)
avng1img2 = pygame.transform.smoothscale(avng1, (125, 125))
avng1_rect2 = avng1.get_rect()
avng1_rect2.x = 935
avng1_rect2.y = height/2 + 110

# (movies title)
mvtitle = pygame.transform.smoothscale(title, (443, 60))
mvtitle_rect = title.get_rect()
mvtitle_rect.x = width/2 - 443/2
mvtitle_rect.y = 25

# --------------------------------- Rectangles/boxes ------------------------------------------------- #
# text box input functions (if the textbox is active, the colour is visible, otherwise it isn't)
activeun = False
activepw = False
colour_active = pygame.Color(0)
colour_passive = pygame.Color(192, 192, 192)
colour = colour_passive

# -------- Page 1 -------- #
# (x position, y position, width, height)
# (input) creates boxes for login details
loginbox = pygame.Rect(width/2 - 550/2, height/2 - 275/2, 550, 400)
usernamebox = pygame.Rect(width/2 - 300/2, height/2 - 225/4, 375, 30)
passwordbox = pygame.Rect(width/2 - 300/2, height/2, 375, 30)

# (enter and skip buttons)
enterbox = pygame.Rect(width/2 - 115/2, height/2 + 78, 120, 45)
skipbox = pygame.Rect(width/2 - 115/2, height/2 + 138, 120, 45)

# -------- Page 2 -------- #
# (headings) creates boxes for page 2 (trending, new releases, most popular, etc...)
trendingbox = pygame.Rect(25, height/2 - 175, 350, 60)
newreleasesbox = pygame.Rect(425, height/2 - 175, 350, 60)
mostpopbox = pygame.Rect(825, height/2 - 175, 350, 60)

# -------- Page 3 -------- #
# (headings) creates boxes for page 3 (tickets, seatings, etc...)
ticketsbox = pygame.Rect(50, height/2 - 125, 285, 60)
seatingsbox = pygame.Rect(365, height/2 - 125, 785, 60)
screenbox = pygame.Rect(400, 525, 715, 50)

# (+ and - button, number box)
ticketminus = pygame.Rect(50, height/2, 75, 75)
ticketplus = pygame.Rect(260, height/2, 75, 75)
ticketnumberbox = pygame.Rect(145, height/2, 95, 75)

# (pay button)
continuebox = pygame.Rect(110, height/2 + 200, 175, 50)

# -------- Page 4 -------- #
dayselectbox = pygame.Rect(85, height/2 - 150, 225, 50)
timeselectbox = pygame.Rect(385, height/2 - 150, 225, 50)
checkoutbox = pygame.Rect(780, height/2 - 150, 285, 60)
paybox = pygame.Rect(875, height/2 + 60, 110, 50)
tryagainbox = pygame.Rect(width/2 - 400, height/2 - 80, 800, 100)

# -------- Page 4 -------- #
exitbox = pygame.Rect(width/2 - 70, height/2 + 73, 100, 50)

# ------------------ Seatings settings ----------------- #
# colours for seatings
colourArray = [(192, 192, 192), (0, 255, 0)]

# colour variables for seatings   
c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
c6 = False
c7 = False
c8 = False

c1b = False
c2b = False
c3b = False
c4b = False
c5b = False
c6b = False
c7b = False
c8b = False

# seatings rectangles
seating1 = pygame.Rect(365, height/2, 75, 75)
seating2 = pygame.Rect(465, height/2, 75, 75)
seating3 = pygame.Rect(565, height/2, 75, 75)
seating4 = pygame.Rect(665, height/2, 75, 75)
seating5 = pygame.Rect(765, height/2, 75, 75)
seating6 = pygame.Rect(865, height/2, 75, 75)
seating7 = pygame.Rect(965, height/2, 75, 75)
seating8 = pygame.Rect(1065, height/2, 75, 75)

seating1b = pygame.Rect(365, height/2 + 100, 75, 75)
seating2b = pygame.Rect(465, height/2 + 100, 75, 75)
seating3b = pygame.Rect(565, height/2 + 100, 75, 75)
seating4b = pygame.Rect(665, height/2 + 100, 75, 75)
seating5b = pygame.Rect(765, height/2 + 100, 75, 75)
seating6b = pygame.Rect(865, height/2 + 100, 75, 75)
seating7b = pygame.Rect(965, height/2 + 100, 75, 75)
seating8b = pygame.Rect(1065, height/2 + 100, 75, 75)

# seating and color array
seatings = [seating1, seating2, seating3, seating4, seating5, seating6, seating7, seating8, seating1b, seating2b, seating3b, seating4b, seating5b, seating6b, seating7b, seating8b]
seatingClr = [c1, c2, c3, c4, c5, c6, c7, c8, c1b, c2b, c3b, c4b, c5b, c6b, c7b, c8b]

# ------------------------ Text -------------------------------- #
# font type and size (otf font file, font size)
font = pygame.font.Font('LEMONMILK-Medium.otf', 15)
font15 = pygame.font.Font('LEMONMILK-Medium.otf', 25)
font2 = pygame.font.Font('LEMONMILK-Medium.otf', 30)
font3 = pygame.font.Font('LEMONMILK-Medium.otf', 40)

# (input) text input for username and password
username_text = ''
inputun_rect = pygame.Rect(width/2 - 300/2, height/2 - 225/4, 375, 30)

password_text = ''
inputpw_rect = pygame.Rect(width/2 - 300/2, height/2, 375, 30)

# (number) ticket and price amount starts at 1 ticket and $10.00
ticket_amount = int(1)
price_amount = float(10.00)

mouseBuffer = True
displayOptions = False
timeDisplay = False
selectedDate = None
selectedTime = None 

# -------- Page 1 -------- #
# (("text"), antialiasing, colour)
def usernametext(x, y): 
    username = font.render(("Username:"), True, (0, 0, 0))
    screen.blit(username, (x, y))
    
def passwordtext(x, y): 
    password = font.render(("Password:"), True, (0, 0, 0))
    screen.blit(password, (x, y))
    
def logintitletext(x, y): 
    logintitle = font2.render(("Login"), True, (0, 0, 0))
    screen.blit(logintitle, (x, y))
    
def entertext(x, y): 
    enter = font2.render(("Enter"), True, (0, 0, 0))
    screen.blit(enter, (x, y))    
    
def skiptext(x, y): 
    skip = font2.render(("Skip"), True, (0, 0, 0))
    screen.blit(skip, (x, y)) 

def loginerrortext(x, y): 
    loginerror = font3.render(("Please enter your credentials"), True, (255, 255, 255))
    screen.blit(loginerror, (x, y))
       
# -------- Page 2 -------- #
def trendingtext(x, y): 
    trend = font3.render(("Trending"), True, (255, 255, 255))
    screen.blit(trend, (x, y))
    
def newreleasestext(x, y): 
    newreleases = font2.render(("New Releases"), True, (255, 255, 255))
    screen.blit(newreleases, (x, y))
    
def mostpoptext(x, y): 
    mostpop = font2.render(("Most Popular"), True, (255, 255, 255))
    screen.blit(mostpop, (x, y))  

# -------- Page 3 -------- #
def ordertext(x, y): 
    order = font3.render(("Order Tickets"), True, (255, 255, 255))
    screen.blit(order, (x, y))   

def ticketstext(x, y): 
    tickets = font3.render(("Tickets"), True, (255, 255, 255))
    screen.blit(tickets, (x, y))

def seatingstext(x, y): 
    seatings = font3.render(("Theater Seatings"), True, (255, 255, 255))
    screen.blit(seatings, (x, y))   

def ticket_amount_text(x, y):
    tickets2 = font3.render((str(ticket_amount)), True, (255, 255, 255))
    screen.blit(tickets2, (x, y))

# formats the number to having 2 decimal points, then converts the formatted float into a string (since floats only have 1 decimal point)
def pricetext(x, y):
    format_price = "{:.2f}" .format(price_amount)
    price = font2.render("$" + str(format_price), True, (255, 255, 255))
    screen.blit(price, (x, y))

def totalpricetext(x, y): 
    totalprice = font2.render(("Total Price:"), True, (255, 255, 255))
    screen.blit(totalprice, (x, y))

def continuetext(x, y):
    continuet = font2.render(("Continue"), True, (255, 255, 255))
    screen.blit(continuet, (x, y))

def chooseseatstext(x, y): 
    chooseseat = font15.render(("Please Choose a seat or the correct amount of seats"), True, (255, 255, 255))
    screen.blit(chooseseat, (x, y))

# -------- Page 4 -------- #
def dateselecttext(x, y, text="Select Date"):
    date = font2.render(text, True, (255, 255, 255))
    screen.blit(date, (x, y))

def timeselecttext(x, y, text="Select Time"):
    time = font2.render(text, True, (255, 255, 255))
    screen.blit(time, (x, y))

def checkouttext(x, y):
    checkout = font3.render("Check Out", True, (255, 255, 255))
    screen.blit(checkout, (x, y))

def ticketamounttext(x, y): 
    ticketamount = font2.render("Ticket Amount:", True, (255, 255, 255))
    screen.blit(ticketamount, (x, y))

def paytext(x, y): 
    pay = font3.render("Pay", True, (255, 255, 255))
    screen.blit(pay, (x, y))

def tryagaintext(x, y): 
    tryagain = font3.render("Please Select a Time and Date", True, (255, 255, 255))
    screen.blit(tryagain, (x, y))

# -------- Page 5 -------- #
def thankyoutext(x, y): 
    final = font3.render(("Thank you for ordering your tickets!"), True, (255, 255, 255))
    screen.blit(final, (x, y))

def datetext(x, y): 
    global selectedDate
    datet = font2.render(("Date: " + str(selectedDate)), True, (255, 255, 255))
    screen.blit(datet, (x, y))

def timetext(x, y):
    global selectedTime 
    timet = font2.render(("Time: " +  str(selectedTime)), True, (255, 255, 255))
    screen.blit(timet, (x, y))

def exittext(x, y): 
    close = font2.render(("Exit"), True, (255, 255, 255))
    screen.blit(close, (x, y))

# -------------------------- Display for Page 5 --------------------------------------------- #
def page5(): 
    running5 = True
    while running5: 

        # if user wants to quit, the program closes
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running5 = False
                sys.exit()

            # sets the background colour
            screen.fill(backgroundColour) 

            # --------------------------- Images ---------------------------------- #

            # displays images
            screen.blit(popcorn1, popcorn_rect1)
            screen.blit(popcorn2, popcorn_rect2)
            screen.blit(mvtitle, mvtitle_rect)

            # --------------- Draws the rectangles (with colour) ------------------ #

            pygame.draw.rect(screen, (0, 255, 0), exitbox)

            # -------------------------------- Text ------------------------------- #

            thankyoutext(150, height/2 - 100)
            datetext(250, height/2 - 25)
            timetext(250, height/2 + 25)    
            exittext(width/2 - 50, height/2 + 75)

            # -------------------------------- Exitting ------------------------------- #

            # if user clicks on exit box
            if event.type == MOUSEBUTTONDOWN: 
                if exitbox.collidepoint(event.pos):

                    # end the program and close it
                    running5 == False
                    sys.exit()

            pygame.display.flip()

# -------------------------- Display for Page 4 --------------------------------------------- #
def page4(): 
    global dayselectbox, timeselectbox, displayOptions, selectedDate, timeDisplay, selectedTime
    running4 = True
    while running4: 

        # if user wants to quit, the program closes
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running2 = False
                sys.exit()

            # sets the background colour
            screen.fill(backgroundColour)  

            # --------------------------- Images ---------------------------------- #

            # displays images
            screen.blit(popcorn1, popcorn_rect1)
            screen.blit(popcorn2, popcorn_rect2)
            screen.blit(mvtitle, mvtitle_rect)

            # --------------- Draws the rectangles (with colour) ------------------ #

            pygame.draw.rect(screen, (192, 192, 192), dayselectbox)
            pygame.draw.rect(screen, (192, 192, 192), timeselectbox)
            pygame.draw.rect(screen, (192, 192, 192), checkoutbox)
            pygame.draw.rect(screen, (0, 255, 0), paybox)

            # -------------------------------- Text ------------------------------- #

            # If the selected date is not None
            if (selectedDate != None):
                # Display the selected date
                dateselecttext(95, height/2 - 145, selectedDate)
            else:

                # Display the default date
                dateselecttext(95, height/2 - 145)

            # If the selected time is not None
            if (selectedTime != None):

                # Display the selected time
                timeselecttext(400, height/2 - 145, selectedTime)
            else:
                # Display the default time
                timeselecttext(400, height/2 - 145)

            checkouttext(800, height/2 - 150)
            totalpricetext(700, height/2)
            ticketamounttext(645, height/2 - 50)
            ticket_amount_text(950, height/2 - 57)
            pricetext(935, height/2)
            paytext(887, height/2 + 57)

            # --------------------- Date and Time Selection ------------------------ #

            # Date and time list containing all rectangles in the list
            datesRectArray = []
            timesRectArray = []

            # Date and time list containing all text objects in the list
            datesTextArray = []
            timesTextArray = []

            # Day and time list containing all available days and times
            days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            times = ["8:30 AM", "10:30 AM", "12:30 PM", "3:00 PM", "5:00 PM"]

            # For loop for each day in the week
            for date in range (7):
                # Calculating y value
                y = (height/2 - 150) + 55 + date * 45

                # Creating rectangle and text object
                rect = pygame.Rect(95, y, 205, 45)
                text = font2.render(days[date], True, (255,255,255))

                # Appending rectangle and text object to the list
                datesRectArray.append(rect)
                datesTextArray.append(text)
            
            # For loop for each time slot
            for time in range (5):
                # Calculating y value
                y = (height/2 - 150) + 55 + time * 45

                # Creating the rectangle and text object
                rect = pygame.Rect(400, y, 200, 45)
                text = font2.render(times[time], True, (255,255,255))

                # Appending rectangle and text object to the list
                timesRectArray.append(rect)
                timesTextArray.append(text)

            # If the event is mouse down
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # If the day select box is being clicked on by the mouse, and the mouseBuffer is clear
                if dayselectbox.collidepoint(event.pos) and mouseBuffer:
                    # Change the mouse buffer
                    mouseBuffer = False
                    
                    # Switch from displaying the options
                    displayOptions = not displayOptions

                # If the time select box is being clicked on by the mouse, and the mouseBuffer
                if timeselectbox.collidepoint(event.pos) and mouseBuffer:
                    # Change the mouse buffer
                    mouseBuffer = False

                    # Switch from displaying the options
                    timeDisplay = not timeDisplay

            # If the event is mouse button up
            if event.type == pygame.MOUSEBUTTONUP:
                # Clear the mouse buffer
                mouseBuffer = True

            # If the displayOptions variable is true
            if displayOptions:
                
                # For loop for displaying the dates in options
                for i in range(7):

                    # Draw the ith rectangle from the date rect array
                    pygame.draw.rect(screen, (192, 192, 192), datesRectArray[i])

                    # Select the ith rectangle for the display box for the ith text element
                    displayRect = datesRectArray[i]

                    # Offset the display box                    
                    displayRect.x += 5

                    # Display the text on the display box
                    screen.blit(datesTextArray[i], displayRect)

                # For loop for checking for collision in the dates rect
                for i in range(7):
                    # If the event is mouse button down
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # If the ith rectangle from the dates rect array is being clicked on by the mouse
                        if datesRectArray[i].collidepoint(event.pos):
                            # Change the mouse buffer
                            mouseBuffer = False

                            # Set the selected date
                            selectedDate = days[i]

                            # Stop displaying the options
                            displayOptions = False
                        
                # For loop for draw line segments
                for i in range(6):
                    # Draw line dividing options
                    pygame.draw.line(screen, (0,0,0), (datesRectArray[i].x, datesRectArray[i].y+45), (datesRectArray[i].x+195, datesRectArray[i].y+45), width=2)       

            # If the time display variable is true
            if timeDisplay:
                
                # For loop for displaying the dates in options
                for i in range(5):
                    # Draw the ith rectangle from the date rect array
                    pygame.draw.rect(screen, (192, 192, 192), timesRectArray[i])

                    # Select the ith rectangle for the display box for the ith text element
                    displayRect = timesRectArray[i]

                    # Offset the display box   
                    displayRect.x += 5

                    # Display the text on the display box
                    screen.blit(timesTextArray[i], displayRect)

                # For loop for checking for collision in the time rectangle array
                for i in range(5):
                    # If the event is mouse button down
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # If the ith rectangle from the times rect array is being clicked on by the mouse
                        if timesRectArray[i].collidepoint(event.pos):

                            # Clear mouse buffer
                            mouseBuffer = False

                            # Set the selected time
                            selectedTime = times[i]

                            # Stop display the time options
                            timeDisplay = False

                # For loop for draw line segments       
                for i in range(4):
                    # Draw line dividing options
                    pygame.draw.line(screen, (0,0,0), (timesRectArray[i].x, timesRectArray[i].y+45), (timesRectArray[i].x+195, timesRectArray[i].y+45), width=2)       
            
            # If user did not select a time and date
            if selectedTime == None or selectedDate == None:

                # if user clicks pay button
                if event.type == MOUSEBUTTONDOWN: 
                    if paybox.collidepoint(event.pos): 

                        # display a box with an error message
                        pygame.draw.rect(screen, (175, 175, 175), tryagainbox)
                        tryagaintext(width/2 - 350, height/2 - 65)

                        # update screen and display for 2000 milliseconds
                        pygame.display.flip()
                        pygame.time.wait(2000)

            # otherwise, if user selects a time and date, bring them to the 5th page            
            else:
                if event.type == MOUSEBUTTONDOWN: 
                    if paybox.collidepoint(event.pos):
                        page5()                 

            # updates display
            pygame.display.flip()

           

# -------------------------- Display for Page 3 --------------------------------------------- #
def page3():

    # take the global variable and allows it to modify these variables locally
    global ticket_amount, price_amount, seatings, seatingClr

    # running is set to true
    running3 = True

    # sets a while loop for displaying the screen
    while running3: 

        # if user wants to quit, the program closes
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running3 = False
                sys.exit()
          
            # sets the background colour
            screen.fill(backgroundColour)

            # --------------------------- Images ---------------------------------- #
            # displays images
            screen.blit(popcorn1, popcorn_rect1)
            screen.blit(popcorn2, popcorn_rect2)
            screen.blit(mvtitle, mvtitle_rect)

            # --------------- Draws the rectangles (with colour) ------------------ #
            pygame.draw.rect(screen, (192, 192, 192), ticketsbox)
            pygame.draw.rect(screen, (192, 192, 192), seatingsbox)
            pygame.draw.rect(screen, (192, 192, 192), ticketminus)
            pygame.draw.rect(screen, (192, 192, 192), ticketplus)
            pygame.draw.rect(screen, (192, 192, 192), ticketnumberbox)
            pygame.draw.rect(screen, (0, 0, 0), screenbox)
            pygame.draw.rect(screen, (0, 255, 0), continuebox)

            # ---------------------- Choosing seats ------------------------------- #
            # for loop for seatings 
            for seatNum in range(16):
                # setting the default color
                act = 0

                # if the seat is selected
                if (seatingClr[seatNum]):
                    # setting the color to green
                    act = 1;

                # drawing the seating with correct color
                pygame.draw.rect(screen, colourArray[act], seatings[seatNum])

     
            # variable counting the total amount of seats
            currSeating = 0

            # if the mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                # for loop for seatings
                for seatNum in range (16):
                    # if the seating is selected
                    if seatingClr[seatNum]:
                        # add to the total seatings
                        currSeating+=1 

                # for loop for seatings
                for seatNum in range (16):
                    # if the mouse collides with the seatings rectangle and the total settings does not exceed the ticket amount
                    if seatings[seatNum].collidepoint(event.pos) and currSeating < ticket_amount:

                        # changing the seating
                        seatingClr[seatNum] = not seatingClr[seatNum]
                    # if the total settings exceeds the ticket amount
                    if currSeating > ticket_amount:

                        # for loop for seatings
                        for seatNum in range(16):
                            # set all the seatings back to vacant
                            seatingClr[seatNum] = False

            # ---------------------------------------------- Lines ---------------------------------------------- #
            # minus sign
            pygame.draw.line(screen, (0, 0, 0), (60, height/2 + 35), (115, height/2 + 35), width = 5)

            # plus sign
            pygame.draw.line(screen, (0, 0, 0), (270, height/2 + 35), (325, height/2 + 35), width = 5)
            pygame.draw.line(screen, (0, 0, 0), (260 + 75/2, height/2 + 10), (260 + 75/2, height/2 + 62), width = 5)
            
            # ------------------------------- Tickets and Price ------------------------------- #
            # clicking on - button
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if ticketminus.collidepoint(event.pos):

                    # if the ticket amount is greater than or equal to 2
                    if ticket_amount >= 2:

                        # subtract 1 ticket and $10.00
                        ticket_amount -= 1
                        price_amount -= 10.00

  
            # clicking on + button
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if ticketplus.collidepoint(event.pos):

                    # if the ticket amount is less than or equal to 9 
                    if ticket_amount <= 9:

                        # add 1 ticket and $10.00
                        ticket_amount += 1
                        price_amount += 10.00  

            # -------------------------------- Text --------------------------------#
            # displays text (x position, y position)
            ordertext(width/2 - 155, height/2 - 200)
            ticketstext(110, height/2 - 125)
            seatingstext(width/2 - 30, height/2 - 125) 
            ticket_amount_text(175, height/2 + 10)
            pricetext(145, height/2 + 140)
            totalpricetext(95, height/2 + 90)
            continuetext(117, height/2 + 205)

            # If the number of chosen seats do not equal to the ticket amount
            if currSeating != ticket_amount:

                # if user clicks continue button
                if event.type == MOUSEBUTTONDOWN: 
                    if continuebox.collidepoint(event.pos): 

                        # display a box with an error message
                        pygame.draw.rect(screen, (175, 175, 175), tryagainbox)
                        chooseseatstext(width/2 - 395, height/2 - 50)

                        # update screen and display for 2000 milliseconds
                        pygame.display.flip()
                        pygame.time.wait(2000)
            else:             
                if continuebox.collidepoint(event.pos): 
                    page4()
                    

            # updates the screen 
            pygame.display.flip()

# -------------------------- Display for Page 2 --------------------------------------------- #
def page2():
    running2 = True
    while running2: 

        # if user wants to quit, the program closes
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running2 = False
                sys.exit()

            # sets the background colour
            screen.fill(backgroundColour)

            # ------------------------------------------- Images --------------------------------- #
            # displays images
            screen.blit(popcorn1, popcorn_rect1)
            screen.blit(popcorn2, popcorn_rect2)
            screen.blit(mvtitle, mvtitle_rect)
            screen.blit(shrekimg1, shrek_rect1)
            screen.blit(shrekimg2, shrek_rect2)
            screen.blit(carsimg, cars_rect)
            screen.blit(avng1img, avng1_rect)
            screen.blit(avng2img, avng2_rect)
            screen.blit(avng1img2, avng1_rect2)

            # -------------------------- Movie Select ---------------------------------------------- #
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shrek_rect1.collidepoint(event.pos) or shrek_rect2.collidepoint(event.pos) or cars_rect.collidepoint(event.pos) or avng1_rect.collidepoint(event.pos) or avng2_rect.collidepoint(event.pos) or avng1_rect2.collidepoint(event.pos): 
                    
                    # load page 3 if mouse collides with movie
                    page3() 

            # ------------------------------------ Rectangles -------------------------------------- #
            # displays boxes for page 2
            pygame.draw.rect(screen, (192, 192, 192), trendingbox)
            pygame.draw.rect(screen, (192, 192, 192), mostpopbox)
            pygame.draw.rect(screen, (192, 192, 192), newreleasesbox)

            # --------------------------------- Text ----------------------------------------------- #
            # displays text
            trendingtext(90, height/2 - 175)
            newreleasestext(480, height/2 - 165)
            mostpoptext(875, height/2 - 165)

            # updates screen
            pygame.display.flip() 

# -------------------------- Display for Page 1 --------------------------------------------- #
running = True
while running: 

    # if user wants to quit, the program closes
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        # sets the background colour
        screen.fill(backgroundColour)

        # ----------------------------- Images ------------------------------------ #
        # displays images
        screen.blit(popcorn1, popcorn_rect1)
        screen.blit(popcorn2, popcorn_rect2)
        screen.blit(mvtitle, mvtitle_rect)
        
        # ---------------------------- Rectangles --------------------------------- #
        # displays rectangles
        pygame.draw.rect(screen, (255, 255, 255), loginbox)
        pygame.draw.rect(screen, (192, 192, 192), usernamebox)
        pygame.draw.rect(screen, (192, 192, 192), passwordbox)
        pygame.draw.rect(screen, (0, 255, 0), enterbox)
        pygame.draw.rect(screen, (100, 200, 255), skipbox)

        # ------------------------------ Text ------------------------------------- # 
        # displays text
        usernametext(width/2 - 500/2, height/2 - 55)
        passwordtext(width/2 - 500/2, height/2 + 5)
        logintitletext(width/2 - 230/5, height/2 - 125)
        entertext(width/2 - 230/5, height/2 + 80)
        skiptext(width/2 - 140/4, height/2 + 138)

        # ------------------------------ Text Input ------------------------------- #

        # if user clicks on the textbox, it becomes selected
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputun_rect.collidepoint(event.pos):

                # sets active username to True if clicked
                activeun = True 

            # otherwise it is set to false
            else:
                activeun = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputpw_rect.collidepoint(event.pos):

                # sets active password to True if clicked
                activepw = True 

            # otherwise it is set to false    
            else: 
                activepw = False

        # if user clicked on textbox, allow them to input characters and backspace characters
        if event.type == pygame.KEYDOWN: 

            # if user cliked on the box and active username is set to True
            if activeun == True: 

                # if user presses backspace, it deletes a character
                if event.key == pygame.K_BACKSPACE: 
                    username_text = username_text[:-1]

                # else if the length of the string is less than 30, when the user presses a key on the keyboard, it prints it out with unicode    
                elif len(username_text) < 30: 
                    username_text += event.unicode

            # if user clicked on the box and active password is set to True        
            if activepw == True: 

                if event.key == pygame.K_BACKSPACE: 
                    password_text = password_text[:-1]

                # else if the length of the string is less than 30, when the user presses a key on they keyboard, it prints out asterick signs    
                elif len(password_text) < 30: 
                    password_text += '*'

        # if user clicked on textbox, make the text visible        
        if activeun: 
            colour = colour_active
        else: 
            colour_passive

        if activepw: 
            colour = colour_active
        else: 
            colour_passive
        
        # (where the text is being displayed, colour, area)
        # display username text input 
        pygame.draw.rect(screen, (192, 192, 192), inputun_rect)

        # renders the text 
        text1_surface = font.render(username_text, True, (0))
        screen.blit(text1_surface, (width/2 - 290/2, height/2 - 220/4))
        inputun_rect.w = max(375, text1_surface.get_width() + 10)

        # display password text input
        pygame.draw.rect(screen, (192, 192, 192), inputpw_rect)
        text2_surface = font.render(password_text, True, (0))
        screen.blit(text2_surface, (width/2 - 290/2, height/2 + 5))
        inputpw_rect.w = max(375, text2_surface.get_width() + 10)


        # ------------------------------ Buttons ------------------------------------------ #
        # if user clicks on enter/skip box, it brings them to the next page 
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if user clicks on enterbox and there are characters inputted, allow them to enter
            if enterbox.collidepoint(event.pos):
                if (username_text != '' or password_text != ''):
                    page2()

                # otherwise show error message    
                else: 
                    if enterbox.collidepoint(event.pos):

                        # display a box with an error message
                        pygame.draw.rect(screen, (175, 175, 175), tryagainbox)
                        loginerrortext(width/2 - 360, height/2 - 60)

                        # update screen and display for 1500 milliseconds
                        pygame.display.flip()
                        pygame.time.wait(1500)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if skipbox.collidepoint(event.pos):
                page2()
                     
        # updates the display
        pygame.display.update() 













        
