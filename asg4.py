FILENAME = "datafiles/building.txt"

def file_read(file_table: str) -> list:
    """
    Opens and reads the file, and turns the text file into a list
    """
    #opens the file for read only
    f = open(file_table, "r")
    row = []
    table = []
    #.strip('\n') removes the new line function
    #split('|') removes the '|' in the text
    for line in f:
        row = line.strip('\n').split('|')
        #this adds every row into a list, making a list in list, like a spreadsheet
        table.append(row)
    #closes the file
    f.close()
    return table

def file_write(file_table: str, result: str) -> None:
    """
    This will create a file, showing the results based on the order of the dices
    """
    #opens the file for write
    f = open(file_table, "w")
    #it will display the scoring results in a new text file
    f.write(result)
    #closes the file
    f.close()

def table_in_str(table: str) -> str:
    """
    Opens the file again to read the texts and returns it as a string
    """
    text = ""
    f = open(table, 'r')
    #for every line in the file, add that line into the text variable
    for line in f:
        text += line
    #this adds a space between the table and the scoring results
    text += '\n'
    return text
    
def green_points(table: list) -> int:
    """
    This checks how many recycle dice are in the table,
    and adding up a certain amount of points depending on the amount of recycle dice
    """
    green_counter = 0
    #for every row in the table, for every index in that row,
    #if the index contains 'R' in it, count the green dices by 1 
    for row in table:
        for i in row:
            if "R" in i:
                green_counter += 1
    #depending on how many green dices there are,
    #it will make the green_score equal to a certain amount
    if green_counter == 6:
        green_score = 30
    elif green_counter == 5:
        green_score = 20
    elif green_counter == 4:
        green_score = 15
    elif green_counter == 3:
        green_score = 10
    elif green_counter == 2:
        green_score = 5
    elif green_counter == 1:
        green_score = 2
    else:
        green_score = 0
    return green_score

def black_points(table: list) -> int:
    """
    This checks what level the stone dice is in, the it will add a certain amount of points depending on it's level.
    """
    black_score = 0
    #This counts x up to the range of tthe length of the table
    #This then counts y up to the range of the length of x row
    for x in range(0, len(table), 1):
        for y in range(0, len(table[x]), 1):
            if 'S' in table[x][y]:
                #This is looking at the table, going up to the 4th row and above.
                #If 'S' is in the index, increment the points by 8
                if x <= len(table) - 4:
                    black_score += 8
                #This is looking at the table, going up to the 3rd row.
                #If 'S' is in the index, increment the points by 5
                elif x == len(table) - 3:
                    black_score += 5
                #This is looking at the table, going up to the 2nd row.
                #If 'S' is in the index, increment the points by 3
                elif x == len(table) - 2:
                    black_score += 3
                #This is looking at the table, looking only at the 1st row.
                #If 'S' is in the index, increment the points by 2
                else:
                    black_score += 2  
    return black_score           

def orange_points(table: list) -> int:
    """
    This will calculate if a wooden dice is beside anything in the x axis or the y axis.
    If so, then it will add 2 points for every dice that it's beside in
    """
    orange_score = 0
    #for x value in the range of the length of the table,
    #for y value in the range of the x row,
    #if 'W' is in the index,
    for x in range(0, len(table), 1):
        for y in range(0, len(table[x]), 1):
            if 'W' in table[x][y]:
                #if x is at the very top, look at the x row below it and if it equals to '--'
                if x == 0:                    
                    if table[x + 1][y] != "--":
                        orange_score += 2
                #if it's looking at x in the very bottom level, 
                #only look at the x row above it to check if it equals to '--'
                elif x == len(table) - 1:
                    if table[x - 1][y] != "--":
                        orange_score += 2
                #if the x is not either at the very top or at the very bottom,
                #then check if the row above or below is '--'
                else:
                    if table[x - 1][y] != "--": 
                        orange_score += 2
                    if table[x + 1][y] != "--":
                        orange_score += 2
                #if y is at the very left,
                #check if the y at the right of it is '--'
                if y == 0:
                    if table[x][y + 1]  != "--":
                        orange_score += 2
                #if we're looking at the very right of the table,
                #we are only looking at the left of it to see if it is == '--'
                elif y == len(table[x]) - 1:
                    if table[x][y - 1]  != "--":
                        orange_score += 2
                #if we're looking at the vertical-middle of the table,
                #check both left and right sides of it to see if there are any dices that are beside it
                else:
                    if table[x][y - 1] != "--": 
                        orange_score += 2
                    if table[x][y + 1] != "--":
                        orange_score += 2         
    return orange_score

def white_points(table: list) -> int:
    """
    This will calculate the white points and return the value,
    which will be picked up in the main
    """
    white_score = 0
    #for every row in the table,
    #for every index in those rows,
    for line in table:
        for i in line:
            #if 'G' is present in the index,
            if 'G' in i:
                #only take the second character of the index, which contains the number
                num = i[1]
                #turn that character from a str to an int and store it into a variable
                number = int(num)
                #increment white_score by that number
                white_score += number
    return white_score

def main() -> None:
    table = file_read(FILENAME)
    table_text = table_in_str(FILENAME)
    #these variables are making the table variable to be a parameter in these functions
    recycle_points = green_points(table)
    stone_points = black_points(table)
    wood_points = orange_points(table)
    glass_points = white_points(table)
    #this variable adds all the points that are stored in the previous variables
    total_points = recycle_points + stone_points + wood_points + glass_points
    #this is a display of the socring result in a table-like format
    result = (f"{table_text}\n+----------+----+\n| glass    |{glass_points:>3} |\n| recycled |{recycle_points:>3} |\n| stone    |{stone_points:>3} |\n| wood     |{wood_points:>3} |\n+==========+====+\n| total    |{total_points:>3} |\n+----------+----+")
    #This takes the result variable to be its parameter
    file_write("scoring-results.txt", result)

main()

#Resources
#I used this website, and my lecture notes to fully understand how strip() works
#https://stackoverflow.com/questions/53772060/what-is-the-difference-between-input-strip-split-and-input-split#:~:text=There's%20no%20difference.,this%20behavior%20of%20split()%20.

