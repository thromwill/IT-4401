#----------------------------------------------------------------------------Helpful Tools
 #----------------------------------------------------------------------------------------
import pygame, re, math
from pygame import mixer

#Global Colors
GREEN = (0, 175, 15)
RED = (225, 30, 30)
YELLOW = (255, 225, 75)
BLUE = (0, 130, 190)
ORANGE = (255, 110, 50)
BLACK = (0, 0, 0)
GREY = (24, 24, 24)
WHITE = (255, 255, 255)

#----------------------------------------------------------------------------------Classes
 #----------------------------------------------------------------------------------------

#Song class
  #name - song name
  #offset - corresponds to time at beginning of song before notes play
  #resolution - number of song ticks in one beat
  #timeSignature - songs time signature
  #BPM - song tempo in beats per minute
  #bpmChanges - data corresponding to the time of tempo changes and the respective new tempo
  #crotchet - time per beat
  #maxTick - song tick of the last note
  #speed - note fall rate in pixels per second
  #length - number of notes in the song
class Song(pygame.sprite.Sprite):
  def __init__(self, FILENAME):
    pygame.sprite.Sprite.__init__(self)

    songInfo, syncTrack, notes = readFile(FILENAME)

    self.name = songInfo[0][0]
    self.offset = int(songInfo[1][0])
    self.resolution = int(songInfo[2][0])

    self.timeSignature = syncTrack[0]
    self.BPM = syncTrack[1][1]/1000
    self.bpmChanges = syncTrack[2]

    self.notes = makeNotes(notes, self.offset)

    self.crotchet = 60/self.BPM  
    self.maxTick = notes[-1][0]  
    self.speed = self.resolution/self.crotchet/60
    self.length = len(notes)


#Note class
  #color - Note color
  #x, y - Note position
class Note(pygame.sprite.Sprite):
  def __init__(self, color, y):
    pygame.sprite.Sprite.__init__(self)

    self.color = color
    self.y = y
    self.x = 0

    if self.color == GREEN:
      self.x = 170 #Furthest left
    elif self.color == RED:
      self.x = 210
    elif self.color == YELLOW:
      self.x = 250
    elif self.color == BLUE:
      self.x = 290
    elif self.color == ORANGE:
      self.x = 330 #Furthest right


#Fret class - Represents each fret on the guitar or each beat in the song being played
  #y - y coordinate of the fret
class Fret(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.y = 0


#Strumbar class - Represents strumbar on guitar
  #pressed - Boolean representing if the button is currently being pressed
  #value - Int value that will be incremented each time a strum occurs
class Strumbar(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.pressed = False
    self.value = 0


#Button class - Represents five main note buttons that make up the bottom bar
  #color - Button Color - Green, Red, Yellow, Blue, or Orange
  #x, y - Coordinate positions on canvas
  #pressed - Boolean representing if the button is currently being pressed
class Button(pygame.sprite.Sprite):
  def __init__(self, color):
    pygame.sprite.Sprite.__init__(self)

    self.color = color

    self.y = 480

    if self.color == GREEN:
      self.x = 170
    elif self.color == RED:
      self.x = 210
    elif self.color == YELLOW:
      self.x = 250
    elif self.color == BLUE:
      self.x = 290
    elif self.color == ORANGE:
      self.x = 330

    self.pressed = False


#Score class
  #value - Int value containing the game score
  #notesHit - Int value holding number of notes hit, used to calculate percentage of song played correctly
class Score(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.value = 0
    self.notesHit = 0


#MenuButton class
  #name - button text
  #color - button fill color
  #x, y - position coordinates on display
  #textOffset - x increment used to center text
  #width - button width
  #height - button height
class MenuButton(pygame.sprite.Sprite):
  def __init__(self, name, color, y, textOffset):
    pygame.sprite.Sprite.__init__(self)

    self.name = name
    self.color = color
    self.y = y
    self.textOffset = textOffset

    self.x = 150
    self.width = 200
    self.height = 50

#--------------------------------------------------------------------------------Functions
 #----------------------------------------------------------------------------------------

#readFile - takes name of a text file corresponding to a songs guitar hero chart
#Returns:
    #songInfo - a list with the songs name, offset, and resolution
    #syncTrack - a list with the songs time signature and bpm changes
    #notes - a list of note data for each note in the chart
def readFile(FILENAME):
  #Open the file
  with open(FILENAME, 'rb') as file:
    songInfo = []
    syncTrack = []
    notes = []

    for line in file:
      #Get songInfo data
      if "{" in str(line) or "}" in str(line) or "[" in str(line) or "]" in str(line) or "E" in str(line): #Garbage lines
        continue
      elif "Name" in str(line): #Song Title
        songInfo.append(re.findall('"([^"]*)"', str(line)))
      elif "Offset" in str(line) or "Resolution" in str(line): #Offset and Resolution
        songInfo.append(re.findall(r'\d+', str(line)))
      #Get synTrack data
      elif "TS" in str(line): #Time Signature
        line = line.split()
        syncTrack.append(int(re.sub("[^0-9]", "", str(line[3]))))
      elif "B" in str(line): #BPM Changes
        temp = []
        line = line.split()
        temp.append(int(re.sub("[^0-9]", "", str(line[0]))))
        temp.append(int(re.sub("[^0-9]", "", str(line[3]))))
        syncTrack.append(temp)
      else: #Notes
        temp = []
        line = line.split()

        temp.append(int(re.sub("[^0-9]", "", str(line[0])))) #Note tick
        temp.append(int(re.sub("[^0-9]", "", str(line[3])))) #Note color
        temp.append(int(re.sub("[^0-9]", "", str(line[4])))) #Note length
        notes.append(temp)
  
  return songInfo, syncTrack, notes

#makeNotes - takes a list of notes read in from the chart file
  #Creates a note object for each note, adds it to a list, and returns the completed list
def makeNotes(noteData, offset):
  #Create an empty list
  chart = []

  #Set note color
  for i in noteData:
    color = 0
    if i[1] == 0:
      color = GREEN
    elif i[1] == 1:
      color = RED
    elif i[1] == 2:
      color = YELLOW
    elif i[1] == 3:
      color = BLUE
    elif i[1] == 4:
      color = ORANGE

    #The y value is calculated as the negative tick from the chart file plus the offset
    y = -i[0] + offset

    #Create a new note object
    newNote = Note(color, y)

    #Add the object to the list
    chart.append(newNote)

  return chart


#makeFrets - takes a song object
  #Returns a list of fret objects with one fret for each beat in the song
def makeFrets(Song):
  frets = []
  position = 0

  for i in range(math.ceil(Song.maxTick/Song.resolution)):
    newFret = Fret()
    newFret.y -= position
    position += Song.resolution
    frets.append(newFret)

  return frets


#makeButtons - returns a list of five buttons that make up the bottom bar
def makeGamebar():
  buttons = []

  #Create a Button object for each button
  green = Button(GREEN)
  red = Button(RED)
  yellow = Button(YELLOW)
  blue = Button(BLUE)
  orange = Button(ORANGE)

  #Add to the list
  buttons.append(green)
  buttons.append(red)
  buttons.append(yellow)
  buttons.append(blue)
  buttons.append(orange)

  #Return the list
  return buttons


#drawNotes - takes a list of note objects and a pygame display
  #Draws each note based on its color and corresponding position
def drawNotes(chart, canvas):
  for note in chart:
    pygame.draw.circle(canvas, note.color, (note.x, note.y), 15)


#drawFrets - takes a list of fret objects and a pygame display
  #Draws each fret
def drawFrets(frets, canvas):
  for fret in frets:
    pygame.draw.rect(canvas, GREY,(150, fret.y , 200, 4))
    pygame.draw.rect(canvas, WHITE,(150, fret.y , 200, 2))


#drawGamebar - takes a pygame display and button list
  #Draws each button, and draws a white circle if the button is being pressed
def drawGamebar(canvas, buttons):
  for i in buttons:
    #Draw the buttons, which will appear as a colored outer ring and grey inner circle
    pygame.draw.circle(canvas, i.color, (i.x, i.y), 20, 5)
    pygame.draw.circle(canvas, GREY, (i.x, i.y), 15, 3)

    #Light up the button white if it is pressed
    if i.pressed == True:
      pygame.draw.circle(canvas, WHITE, (i.x, i.y), 12)


#drawScore - takes a pygame display, score object, font object, and song object
  #Draws the number of points and cumulative percentage notes hit
def drawScore(canvas, score, font, song):
  points = font.render(str(score.value), True, WHITE)
  canvas.blit(points, (50, 400))
  #Percentage calculation not currently working - notesHit increases more than once per loop
  #percentage = font.render("{:.0%}".format(score.notesHit/song.length), True, WHITE)
  #canvas.blit(percentage,(50, 350))
  

#drawMenuButton - takes a pygame display, MenuButton object, and font object
  #Draws each button
def drawMenuButton(canvas, button, font):
  pygame.draw.rect(canvas, button.color,(button.x, button.y, button.width, button.height))

  text = font.render(button.name, True, WHITE)
  canvas.blit(text, (button.x + button.textOffset, button.y + 12))


#update - takes a list of note objects, a score object, a list of buttons on the gamebar, and a strumbar object
  #Updates the notes position to move them down the screen, and increases the score if the correct buttons are pressed and a strum has occured at the right time
def update(chart, score, buttons, strumbar, frets, song):
  for fret in frets:
    fret.y += song.speed

  for note in chart:
    #Increase each notes y value to move it down the screen
    note.y += song.speed

    #Set a temp value to zero
    #Once a note hits the min threshhold, record the strumbar value
    #If the strumbar gets pressed, increase the value
    temp = 0
    if note.y > 465:
      temp = strumbar.value
    if strumbar.pressed == True:
      strumbar.value += 1

    #Check if the note is near the notebar
    if note.y > 460 and note.y < 495:
      #Check if the right keys are pressed
      #Since guitars only play the highest note being held down, orange, for example, is counted if any of the buttons are simultaneously held down, while green will only count if green and only green is being pressed
      #**Chords and note length are currently ignored
      if (
            (note.color == GREEN and buttons[0].pressed == True and buttons[1].pressed == False and buttons[2].pressed == False and buttons[3].pressed == False and buttons[4].pressed == False) or
            
            (note.color == RED and buttons[1].pressed == True and buttons[2].pressed == False and buttons[3].pressed == False and buttons[4].pressed == False) or

            (note.color == YELLOW and buttons[2].pressed == True and buttons[3].pressed == False and buttons[4].pressed == False) or

            (note.color == BLUE and buttons[3].pressed == True and buttons[4].pressed == False) or

            (note.color == ORANGE and buttons[4].pressed == True)
        ):
        #Check if the guitar was strum
          #If the value has increased, the strum button has been pressed in time, so the note was hit
          if strumbar.value > temp:
            #All conditions are met, increase the score
            score.value+=10
            score.notesHit+=1

#-------------------------------------------------------------------------Primary Gameplay
 #----------------------------------------------------------------------------------------

#playGame - takes the name of the song to be played
#Creates game objects, intializes necessary materials, runs main game loop
def playGame(songName):
  #Create the song, fret, strumbar, gamebar, and score objects
  song = Song(songName + ".txt")
  frets = makeFrets(song)
  strumbar = Strumbar()
  gamebar = makeGamebar()
  score = Score()
  
  #Initialize pygame, mixer, and font
  pygame.init()
  clock = pygame.time.Clock()

  mixer.init()
  mixer.music.load(song.name + ".wav")

  font = pygame.font.SysFont("Arial", 20)

  #Create and name the display
  canvas = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Definitely Not Guitar Hero")

  #Play the song
  mixer.music.play()

  #-------------------------------------------------------Main Game Loop
  exit = False
  while not exit:
      #Update 60 times per second
      clock.tick(60)

      #Set canvas to black
      canvas.fill(BLACK)
      
      #Draw visual elements
      drawScore(canvas, score, font, song)
      drawFrets(frets, canvas)
      drawNotes(song.notes, canvas)
      drawGamebar(canvas, gamebar)

      #Update visual elements
      update(song.notes, score, gamebar, strumbar, frets, song)
      
      #Take input
      for event in pygame.event.get():
          #Check for program exit
          if event.type == pygame.QUIT:
              mixer.music.stop()
              exit = True

          #Check for main controls
        #--------------------------
          #Colored buttons down
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
              gamebar[0].pressed = True
            if event.key == pygame.K_u:
              gamebar[1].pressed = True
            if event.key == pygame.K_i:
              gamebar[2].pressed = True
            if event.key == pygame.K_o:
              gamebar[3].pressed = True
            if event.key == pygame.K_p:
              gamebar[4].pressed = True
          #Strum buttons down
            if event.key == pygame.K_z:
              strumbar.pressed = True
            if event.key == pygame.K_x:
              strumbar.pressed = True
          #Exit key
            if event.key == pygame.K_ESCAPE:
              mixer.music.stop()
              exit = True
              
          #Colored buttons up
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
              gamebar[0].pressed = False
            if event.key == pygame.K_u:
              gamebar[1].pressed = False
            if event.key == pygame.K_i:
              gamebar[2].pressed = False
            if event.key == pygame.K_o:
              gamebar[3].pressed = False
            if event.key == pygame.K_p:
              gamebar[4].pressed = False
          #Strum buttons up
            if event.key == pygame.K_z:
              strumbar.pressed = False
            if event.key == pygame.K_x:
              strumbar.pressed = False

      #If all notes have passed exit song
      if song.notes[-1].y > 550:
        mixer.music.stop()
        exit = True

      #Update the display
      pygame.display.flip()


#menu - Main menu system
  #Displays four buttons for three songs and an exit button
  #Checks for input and makes appropriate function calls
def menu():
#Initialize pygame, mixer, and font
  pygame.init()
  clock = pygame.time.Clock()

  font = pygame.font.SysFont("Arial", 18)

  #Create and name the display
  canvas = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Definitely Not Guitar Hero")

  #Create menu button objects
  songButton1 = MenuButton("Sample", GREEN, 75, 70)
  songButton2 = MenuButton("Mr. Blue Sky", RED, 175, 55)
  songButton3 = MenuButton("Through the Fire and Flames", BLUE, 275, 5)
  exitButton = MenuButton("Exit", ORANGE, 375, 85)

  #-------------------------------------------------------Display Loop
  exit = False
  while not exit:
      #Update 60 times per second
      clock.tick(60)

      #Set canvas to black
      canvas.fill(BLACK)
      
      #Draw the buttons
      drawMenuButton(canvas, songButton1, font)
      drawMenuButton(canvas, songButton2, font)
      drawMenuButton(canvas, songButton3, font)
      drawMenuButton(canvas, exitButton, font)

      #Take input
      mouse = pygame.mouse.get_pos() 

      for event in pygame.event.get():
          #Check for program exit
          if event.type == pygame.QUIT:
              exit = True

          if event.type == pygame.MOUSEBUTTONDOWN: 
            if 150 <= mouse[0] <= 350:
              if 75 <= mouse[1] <= 125: 
                playGame("sample")
              elif 175 <= mouse[1] <= 225: 
                playGame("mrbluesky")
              elif 275 <= mouse[1] <= 325: 
                playGame("throughthefireandflames")
              elif 375 <= mouse[1] <= 425: 
                pygame.quit()
                exit = True
              
              
      #Update the display
      pygame.display.flip()

#-------------------------------------------------------------------------------------Main
 #----------------------------------------------------------------------------------------
def main():
  menu()

#--------------------------------------------------------------------------------Main Call
 #----------------------------------------------------------------------------------------
main()
