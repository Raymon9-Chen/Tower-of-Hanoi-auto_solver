def generate_hanoi (discs):
    hanoi = []
    pole1 = []
    pole2 = []
    pole3 = []
    for disc in range(discs):
        pole1.append(disc + 1)
        pole2.append(0)
        pole3.append(0)
    hanoi.append(pole1)
    hanoi.append(pole2)
    hanoi.append(pole3)
    return hanoi
 
 
 
 
 
def show_towers(towers,rows,fillchar,polechar):
 
 
   
    maxspace = (len(towers[0]) * 2)+ 1
    list1 = []
    list2 = []
    list3 = []
    for disc in towers[0]:
        variable = polechar.center((disc * 2) + 1 , fillchar)
        #print(variable.center(maxspace, ' '))
        list1.append(variable.center(maxspace, ' '))
 
    for disc in towers[1]:
        variable = polechar.center((disc * 2) + 1 , fillchar)
        #print(variable.center(maxspace, ' '))
        list2.append(variable.center(maxspace, ' '))
 
    for disc in towers[2]:
        variable = polechar.center((disc * 2) + 1 , fillchar)
        #print(variable.center(maxspace, ' '))
        list3.append(variable.center(maxspace, ' '))
 
    thing = 0
    while thing < rows:
        print(list1[thing], list2[thing], list3[thing])
        thing += 1
    print()
       
def find_stack_height (pole):
    length = len(pole)
    indentifier = 0
    stopper = False
    while stopper == False:
        if indentifier >= length:
            stopper = True
        elif pole[indentifier] != 0:
            stopper = True
        else:
            indentifier +=1
    return indentifier
 
 
def make_move(pole_s, pole_d, towers):
    start_height = find_stack_height(towers[pole_s])
    destination_height = find_stack_height(towers[pole_d]) - 1
       
       
   
   
    length = len(towers[0])
   
    if destination_height < 0:
        print('This pole is full')
        return False
    if start_height == length:
        return False
    elif destination_height == (length - 1):
        towers[pole_d][destination_height] = towers[pole_s][start_height]
        towers[pole_s][start_height] = 0
        return True
    elif towers[pole_s][start_height] > (towers[pole_d][destination_height + 1]):
        return False
    else:
        towers[pole_d][destination_height] = towers[pole_s][start_height]
        towers[pole_s][start_height] = 0
        return True
 
 
def solve_hanoi(tower):
    solved = tower[0]
    smalldisc = 0
    counter = 0
    while True:
        make_move(smalldisc, (smalldisc + 1) % 3, tower)
        show_towers(tower, len(tower[0]), '=', '|')
       
        if tower[1] == solved or tower[2] == solved:
            break
       
        if make_move(smalldisc, smalldisc - 1, tower) == False:
            make_move(smalldisc - 1, smalldisc, tower) == False
        show_towers(tower, len(tower[0]), '=', '|')
       
        smalldisc += 1
        smalldisc = smalldisc % 3
        print (smalldisc)
        counter += 1
    print('Hanoi Code Finished')
    print('It took:', counter, 'Tries')

#To call, enter: solve_hanoi(generate_hanoi(Replace this with the amount of disc you want))
