#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input <show, viewer_count> and <show, channel>
#input files and return viewer counts for tv shows that air on ABC.
# Note the input will come as a group of lines with same show (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current show and previous show, if show changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_show          = " "                #initialize previous show to blank string

is_abc             = 0 #indicate shows on abc
viewer_total         = 0 #sum viewers
# see https://docs.python.org/2/tutorial/datastructures.html for list details

line_cnt           = 0  #count input lines
curr_show          = " "
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    #note: for simple debugging use print statements, ie:  
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    #-----------------------------------------------------
    # Check if its a new show and not the first line 
    #   (b/c for the first line the previous word is not applicable)
    #   if so then print out list of dates and counts
    #----------------------------------------------------
    if curr_show != prev_show:

        # -----------------------     
	#now write out the join result, but not for the first line input
        # -----------------------
        if line_cnt>1 and is_abc==1:
	    print('{0} {1}'.format(prev_show,viewer_total))
            #now reset lists
	is_abc = 0
        viewer_total = 0
        prev_show = curr_show  #set up previous show for the next set of input lines

	
    # ---------------------------------------------------------------
    #whether or not the join result was written out, 
    #   now process the curr show    
  	
    #determine if its from file <show, viewer_count> or <show, channel>
    # and add up the total viewers
    # ---------------------------------------------------------------
    if value_in == 'ABC': 
        
        is_abc = 1

    else:

        viewer_total += int(value_in)

# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------
print('{0} {1}'.format(curr_show,viewer_total))
