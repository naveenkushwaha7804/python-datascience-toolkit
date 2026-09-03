import numpy as np



#                    SLICING IN NUMPY


# Slicing Syntax
# arr[start:end:step]

# start  -> kaha se start
# end    -> kaha tak (end include nahi hota)
# step   -> gap kitna



#             SLICING ON 1 DIMENSION ARRAY


# Create a 1D array
arr = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(arr)

print("\n----------------------------")


# 1. Basic slicing
print("1) arr[2:7] -> index 2 to 6")
print(arr[2:7])


# 2. Slicing from start
print("\n2) arr[:5] -> from start to index 4")
print(arr[:5])


# 3. Slicing till end
print("\n3) arr[4:] -> from index 4 to end")
print(arr[4:])


# 4. Full array
print("\n4) arr[:] -> full array")
print(arr[:])


# 5. Step slicing
print("\n5) arr[1:9:2] -> every 2nd element from index 1 to 8")
print(arr[1:9:2])


# 6. Every second element
print("\n6) arr[::2] -> every 2nd element")
print(arr[::2])


# 7. Every third element
print("\n7) arr[::3] -> every 3rd element")
print(arr[::3])


# 8. Reverse array
print("\n8) arr[::-1] -> reverse array")
print(arr[::-1])


# 9. Negative indexing
print("\n9) arr[-5:-1] -> negative indexing")
print(arr[-5:-1])


# 10. Skip last element
print("\n10) arr[:-1] -> all except last")
print(arr[:-1])


# 11. Skip first element
print("\n11) arr[1:] -> all except first")
print(arr[1:])


# 12. Last element
print("\n12) arr[-1] -> last element")
print(arr[-1])


# 13. First element
print("\n13) arr[0] -> first element")
print(arr[0])


# 14. Last three elements
print("\n14) arr[-3:] -> last three elements")
print(arr[-3:])


# 15. First three elements
print("\n15) arr[:3] -> first three elements")
print(arr[:3])


# 16. Reverse using negative step
print("\n16) arr[8:2:-1] -> reverse from index 8 to 3")
print(arr[8:2:-1])


# 17. Reverse with step
print("\n17) arr[::-2] -> reverse with every 2nd element")
print(arr[::-2])


# 18. Negative start and step
print("\n18) arr[-2:-8:-2]")
print(arr[-2:-8:-2])


# ============================================================
#             SLICING ON 2 DIMENSION ARRAY
# ============================================================

# Syntax
# arr[row_start:row_end , column_start:column_end]

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("\n\nOriginal 2D Array:")
print(arr)

print("\n----------------------------")


# 1. Single element
print("1) arr[1,2] -> row 1, column 2")
print(arr[1, 2])


# 2. Full second row
print("\n2) arr[1,:] -> full second row")
print(arr[1, :])


# 3. Full third column
print("\n3) arr[:,2] -> full third column")
print(arr[:, 2])


# 4. First two rows
print("\n4) arr[0:2,:] -> first two rows")
print(arr[0:2, :])


# 5. Last two columns
print("\n5) arr[:,2:4] -> last two columns")
print(arr[:, 2:4])


# 6. Middle block
print("\n6) arr[1:3,1:3] -> middle 2x2 matrix")
print(arr[1:3, 1:3])


# 7. Alternate rows
print("\n7) arr[::2,:] -> alternate rows")
print(arr[::2, :])


# 8. Alternate columns
print("\n8) arr[:,::2] -> alternate columns")
print(arr[:, ::2])


# 9. Reverse rows
print("\n9) arr[::-1,:] -> reverse rows")
print(arr[::-1, :])


# 10. Reverse columns
print("\n10) arr[:,::-1] -> reverse columns")
print(arr[:, ::-1])


# 11. Reverse both rows and columns
print("\n11) arr[::-1,::-1] -> reverse rows and columns")
print(arr[::-1, ::-1])


# 12. First two rows and first two columns
print("\n12) arr[:2,:2]")
print(arr[:2, :2])


# 13. First two rows and last two columns
print("\n13) arr[:2,-2:]")
print(arr[:2, -2:])


# 14. Last two rows and first two columns
print("\n14) arr[-2:,:2]")
print(arr[-2:, :2])


# 15. Last two rows and last two columns
print("\n15) arr[-2:,-2:]")
print(arr[-2:, -2:])


# 16. Every second row and column
print("\n16) arr[::2,::2]")
print(arr[::2, ::2])


# 17. Reverse alternate rows
print("\n17) arr[::-2,:] -> reverse alternate rows")
print(arr[::-2, :])


# 18. Reverse alternate columns
print("\n18) arr[:,::-2] -> reverse alternate columns")
print(arr[:, ::-2])


# 19. Row range with step
print("\n19) arr[0:4:2,:] -> rows with step 2")
print(arr[0:4:2, :])


# 20. Column range with step
print("\n20) arr[:,0:4:2] -> columns with step 2")
print(arr[:, 0:4:2])


# ============================================================
#             SLICING ON 3 DIMENSION ARRAY
# ============================================================

# Syntax
#
# arr[block_start:block_end,
#     row_start:row_end,
#     col_start:col_end]


# Create 3D array
# Shape = (2,3,4)
# 2 blocks
# Each block has 3 rows
# Each row has 4 columns

arr = np.array([
    [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12]
    ],

    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print("\n\nOriginal 3D Array:")
print(arr)

print("\nShape:", arr.shape)

print("\n----------------------------")


# General rule:
# arr[block, row, column]


# 1. Single element
print("1) arr[1,1,2] -> single element")
print(arr[1, 1, 2])


# 2. Full first block
print("\n2) arr[0,:,:] -> full first block")
print(arr[0, :, :])


# 3. Full second block
print("\n3) arr[1,:,:] -> full second block")
print(arr[1, :, :])


# 4. First block, second row
print("\n4) arr[0,1,:] -> first block, second row")
print(arr[0, 1, :])


# 5. Same row from all blocks
print("\n5) arr[:,1,:] -> second row from all blocks")
print(arr[:, 1, :])


# 6. Same column from all blocks
print("\n6) arr[:,:,2] -> third column from all blocks")
print(arr[:, :, 2])


# 7. Only first block using slicing
print("\n7) arr[0:1,:,:] -> only first block")
print(arr[0:1, :, :])


# 8. Middle rows from all blocks
print("\n8) arr[:,1:3,:] -> middle rows from all blocks")
print(arr[:, 1:3, :])


# 9. First two columns from all blocks
print("\n9) arr[:,:,0:2] -> first two columns")
print(arr[:, :, 0:2])


# 10. Alternate columns
print("\n10) arr[:,:,::2] -> alternate columns")
print(arr[:, :, ::2])


# 11. Reverse columns
print("\n11) arr[:,:,::-1] -> reverse columns")
print(arr[:, :, ::-1])


# 12. Reverse blocks
print("\n12) arr[::-1,:,:] -> reverse blocks")
print(arr[::-1, :, :])


# 13. Alternate blocks
print("\n13) arr[::2,:,:] -> alternate blocks")
print(arr[::2, :, :])


# 14. First block, first two rows
print("\n14) arr[0,:2,:] -> first block, first two rows")
print(arr[0, :2, :])


# 15. First block, last two columns
print("\n15) arr[0,:,-2:]")
print(arr[0, :, -2:])


# 16. Last block, last two rows
print("\n16) arr[-1,-2:,:]")
print(arr[-1, -2:, :])


# 17. Last block, last two columns
print("\n17) arr[-1,:,-2:]")
print(arr[-1, :, -2:])


# 18. First two rows and first two columns from all blocks
print("\n18) arr[:,:2,:2]")
print(arr[:, :2, :2])


# 19. Last two rows and last two columns
print("\n19) arr[:,-2:,-2:]")
print(arr[:, -2:, -2:])


# 20. Alternate rows and columns
print("\n20) arr[:,::2,::2]")
print(arr[:, ::2, ::2])


# 21. Reverse rows
print("\n21) arr[:,::-1,:] -> reverse rows")
print(arr[:, ::-1, :])


# 22. Reverse rows and columns
print("\n22) arr[:,::-1,::-1] -> reverse rows and columns")
print(arr[:, ::-1, ::-1])


# 23. Reverse everything
print("\n23) arr[::-1,::-1,::-1] -> reverse blocks, rows and columns")
print(arr[::-1, ::-1, ::-1])


# 24. Specific block + row + column slicing
print("\n24) arr[0:2,0:2,1:4]")
print(arr[0:2, 0:2, 1:4])


#                    QUICK SUMMARY


# 1D
# arr[start:end]
# arr[start:end:step]
# arr[::-1]             -> reverse
# arr[-3:]              -> last 3 elements
# arr[:-1]              -> except last element


# 2D
# arr[row,column]
# arr[row_start:row_end,column_start:column_end]
# arr[:,column]         -> complete column
# arr[row,:]            -> complete row
# arr[::-1,:]           -> reverse rows
# arr[:,::-1]           -> reverse columns


# 3D
# arr[block,row,column]
# arr[block,:,:]        -> complete block
# arr[:,row,:]          -> same row from all blocks
# arr[:,:,column]       -> same column from all blocks
# arr[::-1,:,:]         -> reverse blocks
# arr[:,::-1,:]         -> reverse rows
# arr[:,:,::-1]         -> reverse columns
# arr[::-1,::-1,::-1]   -> reverse everything