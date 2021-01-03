def get_led_indexes(num):
    '''
    This function takes in a number, converts to binary. Shifting through a number's bits, from 0 to 7, will correspond to the LED's index, to be turned on.

    Example num = 99
        First Iteration:
        i = 0
        99 & (1 << 0)   # Is the same as: 0b1100011 & (0b1 << 0)
        0b1100011 & 0b1 # This checks the first bit, starting on the right. Will return 1, if both bits are 1
        >> 1            # Since 1 is True, the value of i, will be appended to the array. (0)

        Second Iteration:
        i = 1
        99 & (1 << 1)    # Is the same as: 0b1100011 & (0b1 << 1) # Shift left 1
        0b1100011 & 0b10 # This checks the second bit, starting on the right. Will return 2, if both bits are 1
        >> 2             # Value of i is appended to the array

        Third Iteration:
        i = 2
        99 & (1 << 2)     # Is the same as: 0b1100011 & (0b1 << 2) # Shift left 2
        0b1100011 & 0b100 # This checks the third bit, starting on the right. Will return 4, if both bits are 1, otherwise 0
    '''
    arr = []
    for i in range(0,8):
        if num & (1 << i):
            arr.append(i)
    return arr
