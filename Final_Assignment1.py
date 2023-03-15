#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1 finding sum of pair distances of arary elements - hamming distance

def get_distance(arr):
    
    arr_len = len(arr)       # length of array 
    sum_of_pair_distances = 0    # setting initial value of sum to 0
    shift_bit = 0                # having a variable shift_bit for hamming distance
    for i in range(0, 8):        
        # looping though a constant interval and considering only 8 positions 
        count = 0                # count number of elt's with bit set at position i
        for j in range(0, arr_len):    
            # looping through the array elements
            arr_j = arr[j]       # selecting elt of array and setting it to a variable
            #print(arr_j)
            shift_bit = 1 << i   # shifting the bits of binary representation of 1 by i bits 
            bit_and = arr_j & shift_bit  #performing bitwise & on j'th elt and shiftbit
            #print(bit_and)
            if (bit_and):        
                # if the value after bit_and is 1 increement counter
                count+= 1
        sum_of_pair_distances += (count * (arr_len - count)); # finding the distance of the paired values and adding them
        
    #print(sum_of_pair_distances)    
    sum_of_pair_distances = sum_of_pair_distances * 2    # multiply the total by 2 to consider even reciprocative pairs
    
    
    return sum_of_pair_distances


# In[ ]:


#Q2
#using reccursive method, we can find the number of ways in which the ‘k’ steps be covered

def move_steps(k):
    if k == 1:
        # if k = 1, number of ways = 1
        return 1      
    
    if k == 2:
        # if k = 2, number of ways = 2
        return 2      
    
    else:
        # if k>2, then we call the function reccursively by decreasing the 
        # value of k by 1 and 2 steps respectively until k becomes 1 and 
        # returns 1 step on each call of the function
        dec1 = move_steps(k-1) #function to keep reducing the passed k value by 1 step each time
        #print(dec1)
        dec2 = move_steps(k-2) #function to keep reducing the passed k value by 1 step each time
        #print(dec1)
        answer = dec1 + dec2   # adding the values of both decreements to count number of ways
    
    return answer


# In[ ]:


#Q3 - to find if the message received is a corrupted message or no

def decode_message(s):
    i=1
    s_len = len(s)
    output=s[0]  # initialising output to the first character of the message 's'
    while(i<s_len): # looping through the string
        #print("check")
        if(s[i]!=s[i+1]): #checking if the prev string char and next string char are not same, the return original message
            return s      
        i=i+3             # increementing the value of i by three to move to the next character to be checked
    j=1                   # setting j variable to 1
    while(j<s_len):
       # print(j)
        if(j%2==0 or j%3 ==0): # a pattern was noticed that the characters position checked were either a multiple of 2 or 3
            # if they the conditions are fulfilled, we add the character to the output message
            output=output+s[j]
        j=j+1
    message = output    
    return message


# In[ ]:


#Q4 to return the number of substrings that have equal numbers of consecutive a’s and followed by consecutive b’s

def count_sub_strs(s : str) -> int:
    s_len=len(s)
    number_of_sub_strings = 0
    i = 0;
    while(i<s_len):
        # setting counter variables of a and b initially to 0
        count_a = 0
        count_b = 0
        if (s[i] != 'a') :    
            # checking condition where i'th character of string is not a
            
            while (i < s_len and s[i] == 'b') :    #running a loop to check if the character is b
                # if true, increement the counter value by 1
                count_b += 1
                i += 1
                #print("count1 : i ", count_b," : ", i)
            j = i
            while (j < s_len and s[j] == 'a') :    #running a loop to check if the character is a
                # if true, increement the counter value by 1
                count_a += 1
                #print("count2 : j ", count_a," : ", j)
                j += 1
        else :
            while (i < s_len and s[i] == 'a') :    #running a loop to check if the character is a
                # if true, increement the counter value by 1
                count_a += 1
                #print("count3 : i ", count_a," : ", i)
                i += 1
            j = i
            while (j < s_len and s[j] == 'b') :    #running a loop to check if the character is b
                # if true, increement the counter value by 1
                count_b += 1
                #print("count4 : j ", count_b," : ", j)
                j += 1
        #print("count_a : count_b ", count_a," : ", count_b)        
        min_count = min(count_a, count_b)
        #print(min_count)
        number_of_sub_strings += min_count
        
    return number_of_sub_strings


# In[ ]:


#Q5 : check if string s1 can be transformed into string s2 by replacing characters
def check_transformation(s1, s2):
    len_n1 = len(s1)
    s1_list = []           # creating a list to store s1 content
    len_n2 = len(s2)
    s2_list = []           # creating a list to store s2 content
    
    for i in (s1):             # loop through the characters and check if it is present in s1
        s1_inx = s1.index(i)   # fetching the index value of elt at ith position
        s1_list.append(s1_inx) # appending the s1 list , the index value is set according to the letter/ character encountered in the string
        #print("i: ", i, "s1_list", s1_list)
    #print(s1_list)
    print(" ")
        
    for i in s2:               # loop through the characters and check if it is present in s1
        s2_inx = s2.index(i)   # fetching the index value of elt at ith position
        s2_list.append(s2_inx) # appending the s2 list , the index value is set according to the letter/ character encountered in the string
        #print("i: ", i, "s2_list", s2_list)
    #print(s2_list)
    
    if s1_list == s2_list:    # comparing both the lists, if the list content i.e. the integer values assigned are similar, then return True
        #print(" ")
        #print("s1 : ",s1,"s2 : ",s2)
        #print("s1 : ",s1_list,"s2 : ",s2_list)
        return True
    else:
        # comparing both the lists, if the list content i.e. the integer values assigned are not similar, then return False
        #print(" ")
        #print("s1 : ",s1,"s2 : ",s2)
        #print("s1 : ",s1_list,"s2 : ",s2_list)
        return False

