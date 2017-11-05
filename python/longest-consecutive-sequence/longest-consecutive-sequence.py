"""
https://leetcode.com/articles/longest-consecutive-sequence/
- Mayel Espino ><>
"""
from random import randint

def generate_sequence():
    length = randint(50, 100)
    sequence = []
    for index in range(length):
        number = randint(1, 100)
        sequence.append(number)
    return(sequence)

def add_to_sequence(number, sequences):

    if len(sequences) < 1 :
        sub_seq = []
        sub_seq.append(number)
        sequences.append(sub_seq)
        return

    for sequence in sequences:
        if number in sequence:
            return
        prev_number = number - 1

        if prev_number not in sequence:
            continue
        elif sequence.index(prev_number) == 0:
            sequence[:0] = [number]
            return
        elif sequence.index(prev_number) > 0:
            sequence.append(number)
            return
    # if we reach this point the current number is not in any sub_sequence yet
    sub_seq = []
    sub_seq.append(number)
    sequences.append(sub_seq)

def find_longest_sub_sequence(sequences):
    longest_sequence = 0
    for index in range(len(sequences)):
        if len(sequences[index]) > len(sequences[longest_sequence]):
            longest_sequence = index
    return (sequences[longest_sequence])


def main():
    big_sequence = generate_sequence()
    print("Randomly generated sequence:")
    print(big_sequence)
    sub_sequences = []
    for number in big_sequence:
        add_to_sequence(number, sub_sequences)

    print("\n Sub-sequences:")
    print(sub_sequences)

    print("\n Find longest sub-sequence:")
    print(find_longest_sub_sequence(sub_sequences))

if __name__ == "__main__" : main()