from tkinter import * 
from tkinter import messagebox
import random

window = Tk()
window.title("Minesweeper - Amir, Araf, Nathan, Jeremy")

def reset_function(): 
  """single function to reset the entire game without stopping the code - Nathan"""
  global buttons_clicked

#Creates a 2-d list of 10x10 0s - Araf and Amir
  cell_variables_list = [[0 for _ in range(10)] 
                            for _ in range(10)]
  
  #What it looks like:  [[0,0,0,0,0,0,0,0,0,0], 
  #                      [0,0,0,0,0,0,0,0,0,0], 
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0],
  #                      [0,0,0,0,0,0,0,0,0,0]] 

  def spread_bombs_and_values():
    """Author: Araf, Amir, and Jeremy 
   randomly spread the bombs throughout the board and changes the 'cell_variables_list' accordingly.
    """
    #spreading the bombs:
    bomb_or_empty = [0,0,0,"B"] # a list that has the bomb as a 1 in 4 chance to be selected
    
    for row in range(1, 9):
      for column in range(1, 9): # goes through each spot in the lists and randomly selects if its a bomb or not
        cell_variables_list[row][column] = random.choice(bomb_or_empty)

    for row in range(1, 9):
      for column in range(1, 9): # goes through and checks how many bombs are around each tile
        
         if cell_variables_list[row][column] == 0: # if the cell does not contain a bomb, calculate the number of bombs in its vicinity 
          number_of_bombs_present = 0 # number of bombs in the perimeter around the selected cell
           
          for row_change in range(-1, 2, 1):
            for column_change in range(-1, 2, 1): # check coordinates around cell to check for bombs
              
                if cell_variables_list[row+row_change][column+column_change] == 'B': 
                  number_of_bombs_present += 1
         
    #setting cell to value of number of bombs in proximity
          cell_variables_list[row][column] = number_of_bombs_present
          
    # for tmp in range(1,9):
    # print(cell_variables_list[tmp][1:-1]) # THIS IS FOR TESTING
    # print()

  def cell_clicked(row, column, button_to_disable):
    """Handle a cell click - Araf & Nathan"""
    
    buttons_clicked[column][row] = 'C' # gets the location of where each button is and replaced the character in that spot of the list to a 'C' to signify that it was clicked
    
    btn_text = button_to_disable['text'] # grabs the button's text
    
    if btn_text == 'B': # checks if the button you clicked had the text of 'B'
        messagebox.showinfo("Game Over", "You hit a bomb! Game over.") # end the game if bomb is clicked
        window.quit(command = reset_function()) # game over screen when you hit a bomb
      
    else:
      button_to_disable['state'] = 'disabled' # disables the specific button when clicked
      possible_win() # goes to check if you won
  
  def first_layer_blank_button_board():
    """Makes a board of empty buttons in an 8 x 8 grid - Nathan & Araf & Amir"""
    
    global buttons_clicked
    
    text_color = '#DDDDDD' # sets a custom color for the button to use
    
    for button_column in range(1,9):  # two for loops to make an 8 x 8 grid
      for button_row in range(1,9):
        
        blank_button = Button(window, text=str(cell_variables_list[button_column][button_row]), 
                              activeforeground = text_color, 
                              activebackground = text_color, 
                              bg = text_color, 
                              fg = text_color, 
                              disabledforeground = 'black', 
                              padx = 9, 
                              pady = 4) # the button is placed with a randomized text and the text color is set to be the same as the button color, once the button gets disabled it turns the text black
        
        blank_button.config(command=lambda btn=blank_button, row=button_row, column=button_column: cell_clicked(row, column, btn))# we need to wrap cell_clicked in a lambda function so that it does not call blank_button immediately during assignment, causing an infinite loop

        blank_button.grid(row=button_column, column=button_row)  # places the button in a grid

  def possible_win():
    """Checks if all the tiles that are not bombs are clicked and outputs a win screen - Nathan"""
    
    # use buttons_clicked and have it check if each line is a 'C' or a 'B'
    checked_cells = 0 # counter for the cells that match the criteria that is needed
    
    for list_num in range(1, 9): # checks the lists that are required
      for list_char in range(1, 9): # checks the 8 items in the list that are required
        
        if buttons_clicked[list_num][list_char] == 'B' or buttons_clicked[list_num][list_char] == 'C': # checks if the character is a 'B' or a 'C'
          checked_cells += 1 # adds one to the counter of the cells that match the criteria needed
          
    if checked_cells == 64: # if all match it displays a message saying you got all the non bomb tiles
      messagebox.showinfo('YOU WIN!', 'You got all the tiles that were not a bomb.') # shows the you win screen
      window.quit(command = reset_function()) # resets the game if you won
  
  spread_bombs_and_values() # makes the randomly generated bomb grid
  first_layer_blank_button_board() # runs the function to make the grid of buttons
  
  buttons_clicked = [] # makes a brand new list
  for list_counter in range(0, 10): # counter that goes from 0 to 9
    buttons_clicked.append(cell_variables_list[list_counter]) # adds each list from cell_variable_list to buttons_clicked making a copy of the list

  mainloop()
reset_function() # calls the function to start the game