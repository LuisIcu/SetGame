#    
#   filename: SetGame.py
#   date: 24/12/2023
#   author: Luis Icú
#   email: luisfer200010@gmail.com 

TxFile = open('TexFile.txt','w')

MyShapes = ['\\rhomb','\\NotCircle','\\duck']
MyColors = ['MyGreen','MyViolet','MyOrange']
#MyColors = ['red','green','blue']
Filled = ['','fill=','pattern=horizontal lines,pattern color=']
MyNumbers = ['1','2','3']
counter = 0

for myshape in MyShapes:
    for mycolor in MyColors:
        for mfill in Filled:
            for num in MyNumbers:
                TxFile.write(
                    #'\\begin{center}\n' +
                    '\\vspace*{-0.2cm}\n' +
                    '\\begin{figure}[H]\n' +
                    '\\centering \n'+
                    '\t' + myshape + '{' + mycolor + '}{' + mfill + '}{' + num + '}\n'
                    '\\end{figure}\n\n'
                    #'\\end{center}\n\n'
                )
                counter += 1
                if counter<81:
                    TxFile.write(
                        '\\newpage \n\n'
                    )

