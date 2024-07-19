# Help player win card game

Here is the original question:

'''
'''
# Card game:
# // Write a program to rearrange the player's hand, and help them win the maximum possible times for the cards they were dealt with.
#// Max win is defined as the total number of indices i, 0 <= i < n, where rearranged_player_hand[i] > dealer[i] (n is the length of the array)
#// Given that, find the maximum possible wins which can be achieved by some rearrangement of the array.


# // # Example 1
# // # Input:
# // # dealer_hand  =    [1, 3, 5, 2, 1, 3, 1]
# // # player_hand  =    [1, 3, 5, 2, 1, 3, 1]
rearranged_player_hand = [2, 5, 1, 3, 3, 1, 1]
                            
# // # Output: max_wins= 4; rearranged_player_hand=[2, 5, 1, 3, 3, 1, 1]

# // # Explanation : max_wins achieved by player = 4 for the rearranged_player_hand=[2, 5, 1, 3, 3, 1, 1] where the winning indices were [ 0, 1, 3, 4] after rearrangement

# // # Example 2
# // # Input:
# // # dealer_hand = [1, 5, 4, 7, 2, 3]
# // # player_hand = [10, 8, 1, 2, 3, 9]
# Output: max_wins = 5; rearranged_player_hand = [2, 9, 8, 10, 3, 1] 

'''

'''             *
dealer_hand  = [1, 3, 5, 2, 1, 3, 1]
player_hand  = [1, 3, 5, 2, 1, 3, 1]
current_player_index = 1,2,3,5
current_player_card = 2,5,2,3 <-Min()
winnig_cards (1,2),(2,5)

indexes =[]

sorted_player_hand = [1,1,2,3,3,5]

dh = 9,9,9,1,9,1,9,9
ph = 1,2,3,1,1,1,1,1

'''

def help_player_win(dh, ph):
    ph.sort()
    phi = 0
    result_card_list = []
    win_card_list =[]
    other_card_list = []
    win_count = 0
    for card in dh:
        phi = 0
        while phi < len(ph):
            if ph[phi] <= card: 
                #other_card_list.append(ph[phi])
                phi += 1
            else:
                win_card_list.append(ph[phi])
                win_count +=1
                ph[phi] = 0
                break
            
    
    print(win_card_list)
    print(other_card_list)
    result_card_list.extend(win_card_list)
    result_card_list.extend(other_card_list)
    return(win_count, result_card_list)
    
dealer_hand = [1, 3, 5, 2, 1, 3, 1]
player_hand = [1, 3, 5, 2, 1, 3, 1]

# right rearrange - [2, 5, 1, 3, 3, 1, 1]
# wrong rearrange - [2, 5, 3, 3, 1, 1, 1]

print(help_player_win(dealer_hand, player_hand))

'''
