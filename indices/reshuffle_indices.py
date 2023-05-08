#create new shuffles of the testing and training indices
import os
import random

indices_type = 'sex'
#or 'scan_age' or 'sex'
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

for i in range(list_len):
    entry = full_list[i]

    third = i % 3
    if third == 0:
        new_train_list.append(entry)
    elif third == 1:
        new_test_list.append(entry)
    elif third == 2:
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

