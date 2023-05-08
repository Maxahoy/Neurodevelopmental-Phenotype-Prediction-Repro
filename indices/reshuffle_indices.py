#create new shuffles of the testing and training indices
import os
import random
import math

indices_type = 'sex'
#indices_type = 'birth_age'
#indices_type = 'scan_age'
#or 'scan_age' or 'sex'

#percentage that goes to the training set; the rest is evenly divided between testing and validation
#mode = 'thirds'
mode = 'fraction'

training_fraction = 4.0 / 5.0

remainder = 1 - training_fraction
testing_fraction = remainder / 2.0
val_fraction = remainder / 2.0

input_folder = '.'
full_file_name = indices_type + "_full.txt"
train_file_name = indices_type + "_train_reshuffle.txt"
test_file_name = indices_type + "_test_reshuffle.txt"
val_file_name = indices_type + "_val_reshuffle.txt"

#create file paths
full_path = os.path.join(input_folder, full_file_name)
print(full_path)

train_path = os.path.join(input_folder, train_file_name)
test_path = os.path.join(input_folder, test_file_name)
val_path = os.path.join(input_folder, val_file_name)

full_list = open(full_path).read().split('\n')

list_len = len(full_list)
sample_size = list_len / 3

#reorder list randomly to act as sample without replacement
shuffle_list = random.shuffle(full_list)

#select first third as training, next third as testing, next third as val
new_train_list = []
new_test_list = []
new_val_list = []

third = 0

if mode == 'thirds':
    for i in range(list_len):
        entry = full_list[i]

        third = i % 3
        if third == 0:
            new_train_list.append(entry)
        elif third == 1:
            new_test_list.append(entry)
        elif third == 2:
            new_val_list.append(entry)

elif mode == 'fraction':
    num_in_train_sample = round(training_fraction * list_len)
    remaining_sample = list_len - num_in_train_sample
    test_half = math.floor(remaining_sample / 2)
    val_half = math.ceil(remaining_sample / 2)

    #if (num_in_train_sample + test_half + val_half) == list_len:
    #    print("Correct amount: ", (num_in_train_sample + test_half + val_half), list_len)
    #elif (num_in_train_sample + test_half + val_half) != list_len:
    #    print("Incorrect amount!", (num_in_train_sample + test_half + val_half), list_len)
    
    for i in range(list_len):
        entry = full_list[i]

        decider = random.random()
        if 0 <= decider < training_fraction:
            #send to training set
            new_train_list.append(entry)
        elif training_fraction <= decider < (training_fraction + testing_fraction):
            #send to testing fraction
            new_test_list.append(entry)
        elif (training_fraction + testing_fraction) <= decider < (training_fraction + testing_fraction + val_fraction):
            #send to val fraction
            new_val_list.append(entry)


train_write = open(train_file_name, 'w+')
test_write = open(test_file_name, 'w+')
val_write = open(val_file_name, 'w+')

train_write.writelines([f"{line}\n" for line in new_train_list if line])
print("Wrote ", len(new_train_list), " entries to ", train_file_name)

test_write.writelines([f"{line}\n" for line in new_test_list if line])
print("Wrote ", len(new_test_list), " entries to ", test_file_name)

val_write.writelines([f"{line}\n" for line in new_val_list if line])
print("Wrote ", len(new_val_list), " entries to ", val_file_name)

