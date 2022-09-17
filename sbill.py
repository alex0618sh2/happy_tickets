#!/usr/bin/env python3

sch = 0
for i in range(0, 1000000):

    string = str (i)
##### DEBAG ################
#    print ('--------------')
#    print (string)
##### END DEBAG ############


# GRAB stringo
    try:
        s1 = string[-1]
    except IndexError:
        s1 = '0'
    try:
        s2 = string[-2]
    except IndexError:
        s2 = '0'
    try:
        s3 = string[-3]
    except IndexError:
        s3 = '0'
    try:
        s4 = string[-4]
    except IndexError:
        s4 = '0'
    try:
        s5 = string[-5]
    except IndexError:
        s5 = '0'
    try:
        s6 = string[-6]
    except IndexError:
        s6 = '0'

# zero insert
    if s1 == '':
         s1  = '0'
    if s2 == '':
         s2  = '0'
    if s3 == '':
         s3 = '0'
    if s4 == '':
         s4 = '0'
    if s5 == '':
         s5 = '0'
    if s6 == '':
         s6 = '0'


    MainString = s6 + s5 + s4 + s3 + s2 + s1

###### DEBAG ###############################
#    print(MainString)
###### END DEBAG ###########################

# count set
    s6int = int(s6)
    s5int = int(s5)
    s4int = int(s4)
    s3int = int(s3)
    s2int = int(s2)
    s1int = int(s1)

# main logics
    Left = s6int + s5int + s4int
    Right = s3int + s2int + s1int
    if Left == Right:
        sch = sch + 1
######## DEBAG #######################
#        print ("------>", MainString)
######## END DEBAG ###################
        print (MainString)   ### DEBAG comment !!!!!#####

print ('----------------------------')
print ('---ALL HAPPY TICKETS :)))---')
print (sch-1)
print ('----------------------------')

