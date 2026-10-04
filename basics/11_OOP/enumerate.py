seasons = ["Sping", "Summer", "Fall", "Winter"]
count = 1

for season in seasons:
    print(count, season)
    count +=1   # 1 Sping
                # 2 Summer
                # 3 Fall
                # 4 Winter

for count in range(len(seasons)):
    print(count+1, seasons[count])      # 1 Sping
                                        # 2 Summer
                                        # 3 Fall
                                        # 4 Winter

# Refactoring to enumerate():
for count, season in enumerate(seasons, start=1):
    print(count, season)    # 1 Sping
                            # 2 Summer
                            # 3 Fall
                            # 4 Winter

def my_enum(sequence, start=0):
    count = start
    for item in sequence:
        yield count, item    # yield (hangs something out) is a generator
        count += 1

for val in my_enum(seasons, start=1):
    print(val)  #(1, 'Sping')
                # (2, 'Summer')
                # (3, 'Fall')
                # (4, 'Winter') 

counted_seassons = my_enum(seasons, start=1)
for val in counted_seassons:
    print(val)  # once the yield has been hang out to the variable it will not hang it out anymore, because yield is empty. Nothing to return anymore


