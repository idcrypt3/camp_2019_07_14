from random import *
import msvcrt
import os
from os import walk
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','.','?','-','+','=','1','2','3','4','5','6','7','8','9','0',' ','\'','"','!']


def diskgen(alphabet):
    #DISK GENERATION
    disk_avail = []
    disk_direc = []
    disk_map = []
    for num in range (0,len(alphabet)):
        disk_avail.append(num)
        disk_direc.append(num)
    #Begin mapping
    while len(disk_direc) > 0:
        choose_ep = randint(0,len(disk_avail)-1)
        exit_position = disk_avail[choose_ep]
        disk_map.append(exit_position)
        del disk_avail[choose_ep]
        del disk_direc[0]
    for pos in range (0,len(alphabet)):
        disk_map[pos] = disk_map[pos] - pos
    return disk_map


def reflector(alphabet):
    reflect_avail = []
    reflect_map = []
    for num in range (0,len(alphabet)):
        reflect_avail.append(num)
        reflect_map.append('x')
    if len(reflect_avail)%2 == 0:
        while len(reflect_avail) > 0:
            from_num = reflect_avail[0]
            to_pos = randint(1,len(reflect_avail)-1)
            fin_num = reflect_avail[to_pos]
            reflect_map[from_num] = fin_num
            reflect_map[fin_num] = from_num
            del reflect_avail[0]
            del reflect_avail[to_pos-1]
        for pos in range (0,len(alphabet)):
            reflect_map[pos] = reflect_map[pos] - pos
        return reflect_map


def rotate(selected_disk):
    new_disk = []
    new_disk.append(selected_disk[len(selected_disk)-1])
    for pos in range (0,len(selected_disk)-1):
        new_disk.append(selected_disk[pos])
    return new_disk


def code(reflector,letter,language,disk1,disk2,disk3,disk4):
    language_map = {}
    for x in range (0,len(language)):
        language_map.update({language[x]:x})
    ltnumb = language_map[letter]
    disk1_scramble = (disk1[ltnumb] + ltnumb + len(disk1))%len(disk1)
    disk2_scramble = (disk2[disk1_scramble] + disk1_scramble + len(disk2))%len(disk2)
    disk3_scramble = (disk3[disk2_scramble] + disk2_scramble + len(disk3))%len(disk3)
    disk4_scramble = (disk4[disk3_scramble] + disk3_scramble + len(disk4))%len(disk4)
    rfb = (reflector[disk4_scramble] + disk4_scramble + len(reflector))%len(reflector)
    for x in range (0,len(disk4)):
        if (disk4[x]+x+len(disk4))%len(disk4) == rfb:
            disk4_reverse = x
            break
    for x in range (0,len(disk3)):
        if (disk3[x]+x+len(disk3))%len(disk3) == disk4_reverse:
            disk3_reverse = x
            break
    for x in range (0,len(disk2)):
        if (disk2[x]+x+len(disk2))%len(disk2) == disk3_reverse:
            disk2_reverse = x
            break
    for x in range (0,len(disk1)):
        if (disk1[x]+x+len(disk1))%len(disk1) == disk2_reverse:
            eletter = language[x]
            break
    return eletter


#------------------------------------------------------------------------
cwd = os.getcwd()
print(cwd)
if not os.path.exists(cwd+'\\rotor'):
    os.mkdir(cwd+'\\rotor')
f = []
for (dirpath, dirnames, filenames) in walk(cwd+'\\rotor'):
    f.extend(filenames)
files = []
for fname in f:
    if fname.endswith('.rotor'):
        files.append(fname.replace('.rotor',''))
start_selection = input('[1]\tNew Setting\n[2]\tReload Setting from file\n')
if start_selection == '2':
    print(files)
    for num in range (len(files)):
        print('['+str(num)+']\t'+files[num])
    f_choose = int(input())
    with open (cwd+'\\rotor\\'+files[f_choose]+'.rotor','r') as f:
        information = eval(f.read())
elif start_selection == '1':
    d1 = diskgen(english)
    d2 = diskgen(english)
    d3 = diskgen(english)
    d4 = diskgen(english)
    rf = reflector(english)
    d1rc = 0
    d2rc = 0
    d3rc = 0
    d4rc = 0
    rfrc = 0
    raw_type = ''
    enc_type = ''
    information = [d1,d2,d3,d4,rf,d1rc,d2rc,d3rc,d4rc,rfrc,raw_type,enc_type]
    wtf = input('Write to file? [y/n]: ')
    if (wtf == 'y') or (wtf == 'Y'):
        while True:
            name = input('NAME: ')
            os.system('cls')
            if not os.path.isfile(cwd+'\\rotor\\'+name+'.rotor'):
                newf = open(cwd+'\\rotor\\'+name+'.rotor','w')
                break
            if os.path.isfile(cwd+'\\rotor\\'+name+'.rotor'):
                proceed = input('File already exists, overwrite?\n[1]\tYes\n[2]\tNo\n')
                if proceed == '1':
                    newf = open(cwd+'\\rotor\\'+name+'.rotor','w')
                    break
        newf.write(str(information))
        newf.close()
os.system('cls')
d1 = information[0]
d2 = information[1]
d3 = information[2]
d4 = information[3]
rf = information[4]
d1rc = information[5]
d2rc = information[6]
d3rc = information[7]
d4rc = information[8]
rfrc = information[9]
raw_type = input('Plaintext: ')
enc_type = information[11]
word_address = 0
while word_address < len(raw_type):
    print(raw_type+'\n'+enc_type)
    letter = raw_type[word_address]
    os.system('cls')
    try:
        encoded_letter = code(rf,letter,english,d1,d2,d3,d4)
        enc_type += encoded_letter
    except:
        continue
    decoded_letter = code(rf,encoded_letter,english,d1,d2,d3,d4)
    d1 = rotate(d1)
    d1rc += 1
    if d1rc == len(d1):
        d1rc = 0
        d2 = rotate(d2)
        d2rc += 1
        if d2rc == len(d2):
            d2rc = 0
            d3 = rotate(d3)
            d3rc += 1
            if d3rc == len(d3):
                d4 = rotate(d4)
                d3rc = 0
                d4rc += 1
                if d4rc == len(d4):
                    d4rc = 0
                    rf = rotate(rf)
                    rfrc += 1
    word_address += 1
print(raw_type+'\n'+enc_type)
input()