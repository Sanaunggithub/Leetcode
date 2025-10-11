def flipAndInvertImage(image):

    for row in range(len(image)):
        for col in range(len(image[row])):
            if image[row][col] == 1:
                image[row][col] = 0

            else:
                image[row][col] = 1
        
        image[row].reverse()
    return image


image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))