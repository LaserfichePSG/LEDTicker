from MatrixRGB import Matrix

#declaration of char_map
'''
char_map_bw = {
        'a' : Matrix(5, 3, [(0,1,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,2,1)]),
        'b' : Matrix(5, 3, [(0,0,1), (0,1,1), (1,0,1), (1,1,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]), #LOOKS A LITTLE WEIRD
        'c' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (3,0,1), (4,0,1), (4,1,1), (4,2,1)]),
        'd' : Matrix(5, 3, [(0,0,1), (0,1,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1)]),
        'e' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (4,0,1), (4,1,1), (4,2,1)]),
        'f' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (2,1,1), (3,0,1), (4,0,1)]),
        'g' : Matrix(5, 4, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (3,0,1), (3,2,1), (3,3,1), (4,0,1), (4,1,1), (4,2,1), (4,3,1)]), #LOOKS A LITTLE WEIRD
        'h' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,2,1)]),
        'i' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,1,1), (2,1,1), (3,1,1), (4,0,1), (4,1,1), (4,2,1)]),
        'j' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,1,1), (2,1,1), (3,1,1), (4,0,1), (4,1,1)]),
        'k' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,1,1), (2,0,1), (3,0,1), (3,1,1), (4,0,1), (4,2,1)]),
        'l' : Matrix(5, 3, [(0,0,1), (1,0,1), (2,0,1), (3,0,1), (4,0,1), (4,1,1), (4,2,1)]),
        'm' : Matrix(5, 4, [(0,0,1), (0,3,1), (1,0,1), (1,1,1), (1,2,1), (1,3,1), (2,0,1), (2,3,1), (3,0,1), (3,3,1), (4,0,1), (4,3,1)]), #LOOKS A LITTLE WEIRD
        'n' : Matrix(5, 3, [(0,0,1), (0,1,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,2,1)]), #LOOKS VERY WEIRD
        'o' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        'p' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (4,0,1)]),
        'q' : Matrix(5, 5, [(0,1,1), (0,2,1), (1,0,1), (1,3,1), (2,0,1), (2,2,1), (2,3,1), (3,0,1), (3,3,1), (4,1,1), (4,2,1), (4,4,1)]), #LOOKS WEIRD
        'r' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,1,1), (4,0,1), (4,2,1)]),
        's' : Matrix(5, 3, [(0,1,1), (0,2,1), (1,0,1), (2,0,1), (2,1,1), (3,2,1), (4,0,1), (4,1,1)]), #LOOKS A LITTLE WEIRD
        't' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,1,1), (2,1,1), (3,1,1), (4,1,1)]),
        'u' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        'v' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,1,1)]),
        'w' : Matrix(5, 4, [(0,0,1), (0,3,1), (1,0,1), (1,3,1), (2,0,1), (2,3,1), (3,0,1), (3,1,1), (3,2,1), (3,3,1), (4,0,1), (4,3,1)]), #LOOKS A LITTLE WEIRD
        'x' : Matrix(5, 3, [(0,0,1), (0,2,1), (2,1,1), (4,0,1), (4,2,1)]), #LOOKS A LITTLE WEIRD
        'y' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,2,1), (2,1,1), (3,1,1), (4,1,1)]),
        'z' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (2,1,1), (4,0,1), (4,1,1), (4,2,1)]), #LOOKS A LITTLE WEIRD
        '0' : Matrix(5, 3, [(0,1,1), (1,0,1), (1,2,1), (2,0,1), (2,2,1), (3,0,1), (3,2,1), (4,1,1)]),
        '1' : Matrix(5, 3, [(0,1,1), (1,0,1), (1,1,1), (2,1,1), (3,1,1), (4,0,1), (4,1,1), (4,2,1)]),
        '2' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (4,0,1), (4,1,1), (4,2,1)]),
        '3' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        '4' : Matrix(5, 3, [(0,0,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,2,1), (4,2,1)]),
        '5' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (2,1,1), (2,2,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        '6' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        '7' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,2,1), (2,2,1), (3,2,1), (4,2,1)]),
        '8' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,0,1), (3,2,1), (4,0,1), (4,1,1), (4,2,1)]),
        '9' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,0,1), (1,2,1), (2,0,1), (2,1,1), (2,2,1), (3,2,1), (4,2,1)]),
        '.' : Matrix(5, 1, [(4,0,1)]),
        ',' : Matrix(5, 2, [(2,1,1), (3,1,1), (4,0,1)]),
        ';' : Matrix(5, 2, [(1,1,1), (3,1,1), (4,0,1)]),
        ':' : Matrix(5, 1, [(1,0,1), (3,0,1)]),
        '!' : Matrix(5, 1, [(0,0,1), (1,0,1), (2,0,1), (4,0,1)]),
        '?' : Matrix(5, 3, [(0,0,1), (0,1,1), (0,2,1), (1,2,1), (2,1,1), (2,2,1), (3,1,1), (4,1,1)]), #LOOKS A LITTLE WEIRD
        '/' : Matrix(5, 3, [(0,2,1), (2,1,1), (4,0,1)]), #LOOKS A LITTLE WEIRD
        '"' : Matrix(5, 3, [(0,0,1), (0,1,1), (1,0,1), (1,1,1)]),
        ' ' : Matrix(5, 1),
        '\'' : Matrix(5, 1, [(0,0,1), (1,0,1)])
        }
'''

char_map = {
        'a' : Matrix(5, 3, [(0,1,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]),
        'b' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (1,0,(255,255,255)), (1,1,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]), #LOOKS A LITTLE WEIRD
        'c' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'd' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255))]),
        'e' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'f' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255))]),
        'g' : Matrix(5, 4, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (3,3,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255)), (4,3,(255,255,255))]), #LOOKS A LITTLE WEIRD
        'h' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]),
        'i' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,1,(255,255,255)), (2,1,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'j' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,1,(255,255,255)), (2,1,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255))]),
        'k' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,1,(255,255,255)), (2,0,(255,255,255)), (3,0,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]),
        'l' : Matrix(5, 3, [(0,0,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'm' : Matrix(5, 4, [(0,0,(255,255,255)), (0,3,(255,255,255)), (1,0,(255,255,255)), (1,1,(255,255,255)), (1,2,(255,255,255)), (1,3,(255,255,255)), (2,0,(255,255,255)), (2,3,(255,255,255)), (3,0,(255,255,255)), (3,3,(255,255,255)), (4,0,(255,255,255)), (4,3,(255,255,255))]), #LOOKS A LITTLE WEIRD
        'n' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]), #LOOKS VERY WEIRD
        'o' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'p' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255))]),
        'q' : Matrix(5, 5, [(0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,3,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (2,3,(255,255,255)), (3,0,(255,255,255)), (3,3,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255)), (4,4,(255,255,255))]), #LOOKS WEIRD
        'r' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]),
        's' : Matrix(5, 3, [(0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255))]), #LOOKS A LITTLE WEIRD
        't' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,1,(255,255,255)), (2,1,(255,255,255)), (3,1,(255,255,255)), (4,1,(255,255,255))]),
        'u' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        'v' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,1,(255,255,255))]),
        'w' : Matrix(5, 4, [(0,0,(255,255,255)), (0,3,(255,255,255)), (1,0,(255,255,255)), (1,3,(255,255,255)), (2,0,(255,255,255)), (2,3,(255,255,255)), (3,0,(255,255,255)), (3,1,(255,255,255)), (3,2,(255,255,255)), (3,3,(255,255,255)), (4,0,(255,255,255)), (4,3,(255,255,255))]), #LOOKS A LITTLE WEIRD
        'x' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (2,1,(255,255,255)), (4,0,(255,255,255)), (4,2,(255,255,255))]), #LOOKS A LITTLE WEIRD
        'y' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,1,(255,255,255)), (3,1,(255,255,255)), (4,1,(255,255,255))]),
        'z' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (2,1,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]), #LOOKS A LITTLE WEIRD
        '0' : Matrix(5, 3, [(0,1,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,1,(255,255,255))]),
        '1' : Matrix(5, 3, [(0,1,(255,255,255)), (1,0,(255,255,255)), (1,1,(255,255,255)), (2,1,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '2' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '3' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '4' : Matrix(5, 3, [(0,0,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,2,(255,255,255)), (4,2,(255,255,255))]),
        '5' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '6' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '7' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,2,(255,255,255)), (2,2,(255,255,255)), (3,2,(255,255,255)), (4,2,(255,255,255))]),
        '8' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,0,(255,255,255)), (3,2,(255,255,255)), (4,0,(255,255,255)), (4,1,(255,255,255)), (4,2,(255,255,255))]),
        '9' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,0,(255,255,255)), (1,2,(255,255,255)), (2,0,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,2,(255,255,255)), (4,2,(255,255,255))]),
        '.' : Matrix(5, 1, [(4,0,(255,255,255))]),
        ',' : Matrix(5, 2, [(2,1,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255))]),
        ';' : Matrix(5, 2, [(1,1,(255,255,255)), (3,1,(255,255,255)), (4,0,(255,255,255))]),
        ':' : Matrix(5, 1, [(1,0,(255,255,255)), (3,0,(255,255,255))]),
        '!' : Matrix(5, 1, [(0,0,(255,255,255)), (1,0,(255,255,255)), (2,0,(255,255,255)), (4,0,(255,255,255))]),
        '?' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (0,2,(255,255,255)), (1,2,(255,255,255)), (2,1,(255,255,255)), (2,2,(255,255,255)), (3,1,(255,255,255)), (4,1,(255,255,255))]), #LOOKS A LITTLE WEIRD
        '/' : Matrix(5, 3, [(0,2,(255,255,255)), (2,1,(255,255,255)), (4,0,(255,255,255))]), #LOOKS A LITTLE WEIRD
        '"' : Matrix(5, 3, [(0,0,(255,255,255)), (0,1,(255,255,255)), (1,0,(255,255,255)), (1,1,(255,255,255))]),
        ' ' : Matrix(5, 1),
        '\'' : Matrix(5, 1, [(0,0,(255,255,255)), (1,0,(255,255,255))])
        }


#char_map['Q'].test_display()

def change_color(color, all_chars, chars=None):

    #validate inputs
    if (not type(all_chars) is bool):
        print ("BAD DATA")
        return

    #change the color of all characters
    if (all_chars):
        for k in char_map:
            for m in range(char_map[k].m):
                for n in range(char_map[k].n):
                    if (char_map[k].getdatum(m,n) != (0,0,0)):
                        char_map[k].setdatum(m, n, color)

    #change the color of characters specified in input
    else:
        #validate optional input
        if (not type(chars) is list):
            print ("BAD DATA")
            return

        for char in chars:
            for m in range(char_map[char].m):
                for n in range(char_map[char].n):
                    if (char_map[char].getdatum(m,n) != (0,0,0)):
                        char_map[char].setdatum(m, n, color)
    

def display_phrase(phrase):
    count = 0
    result = None
    for char in phrase:
        temp = char_map[char]
        if (count == 0):
            result = temp
            result = result.concatenate(Matrix(5,(255,255,255)))
        else:
            result = result.concatenate(temp)
            result = result.concatenate(Matrix(5,(255,255,255)))
        count = count + 1
    result.test_display()


#display_phrase("sobriquet")
#change_color((0,0,255), False, ['b', 'c'])
#char_map['a'].print_matrix()
#char_map['b'].print_matrix()
