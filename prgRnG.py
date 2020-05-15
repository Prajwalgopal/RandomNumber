import numpy as np 
import matplotlib.pyplot as plt 

#To set the starting value
SeedValue = int(input("Enter the value of seed:"))
#To set the size value
SizeValue = int(input("Enter the value of size:"))


def logarithmic():
    np.random.seed(SeedValue)
    while True:
        try:
            #parameter of the shape
            para = float(input("Enter the value of parameter:"))
        except ValueError:
            #validation
            print("Enter a value between 0 and 1")
            continue
        else:
            if para>0 and  para<1:
                break
            else:
                print("Invalid values, value should be:  0 < p < 1")
                continue


    bins=50
    x = np.random.logseries(para, SizeValue)
    x.sort()
    x_inverse = np.exp(x)

    x_inverse.sort()

    #file for generated sequence
    f = open("LOG_%s_genSeq.txt" % para, "w")
    f.write(str(x))
    f.close()

    y = -para**(x)/((x)*np.log(1-para))
    y = y.cumsum()
    y /= y[-1]

    y_inverse = -para**(x_inverse)/((x_inverse)*np.log(1-para))
    y_inverse = y_inverse.cumsum()
    y_inverse /= y_inverse[-1]

    seqProb = [str(i) + ',' + str(j) for i, j in zip(x, y)] 
    f1 = open("LOG_%s_genSeqCDF.txt" % para, "w")
    f1.write(str(seqProb))
    f1.close()

    #plot for CDF of Logarithmic Distribution
    plt.plot(x, y, linewidth=2, color='r', label='p=%s (CDF)' % (para))
    plt.plot(x, y_inverse, 'k--', linewidth=2, color='b', label='p=%s (Inverse CDF)' % (para))
    plt.title("Logarithmic Distribution-->Cumulative Distribution Function")
    plt.xlabel("random numbers(x)")
    plt.ylabel("P(x)")
    legend = plt.legend(loc='lower right', shadow=True, fontsize='large')
    
    #PDF file for CDF Plot
    plt.savefig('LOG_%s_figCDF.pdf' % para)
   
    #plot for Histogram of Logarithmic Distribution
    fig1, ax1 = plt.subplots()
    ax1.set_title("Logarithmic Distribution --> Cumulative Distribution Function --> Histogram")
    ax1.set_xlabel("random numbers(x)")
    ax1.set_ylabel("P(x)")
    n, bins, patches = ax1.hist(x,bins, density=True, cumulative=True,
                                label="Empirical")
    legend = plt.legend(loc='lower right', shadow=True, fontsize='large')
     #PDF file for Histogram Plot
    fig1.savefig('LOG_%s_figHIST.pdf'% para)
                                       

    #plot for BoxPlot of Logarithmic Distribution
    fig2, ax2 = plt.subplots()
    ax2.set_title("Box Plot for Logarithmic Distribution")
    ax2.boxplot(x)
     #PDF file for BoxPlot
    fig2.savefig('LOG_%s_figBOX.pdf'% para)

    plt.show()

def kumaraswamy():
    np.random.seed(SeedValue)
    a = float(input("Enter the value of alpha:"))
    b = float(input("Enter the value of beta:"))
    bins=50
    x=np.random.rand(SizeValue)
    x.sort()

    f = open("KUM_%s_%s_genSeq.txt" % (a,b), "w")
    #file for generated sequence
    f.write(str(x))
    f.close()

    y = 1-(1-x**a)**b
    y_inverse = (1-((1-x)**(1/b)))**(1/a)
    seqProb = [str(i) + ',' + str(j) for i, j in zip(x, y)]
    f1 = open( "KUM_%s_%s_genSeqCDF.txt" % (a,b), "w")
    #file for generated CDF function
    f1.write(str(seqProb))
    f1.close()

    plt.plot(x, y, linewidth=2, color='b', label='$a=%s, $b=%s (Emperical CDF)' % (a, b))
    plt.plot(x, y_inverse, 'k--', linewidth=2, color='red', label='$a=%s, $b=%s (Inverse CDF)' % (a, b))
    plt.title("Kumaraswamy Cumulative Distribution Function")
    plt.xlabel('x')
    plt.ylabel('P(x)')
    

    legend = plt.legend(loc='lower right', shadow=True, fontsize='large')
    plt.savefig('KUM_%s_%s_figCDF.pdf'% (a,b))
    #PDF file for CDF Plot

    


    fig1, ax1 = plt.subplots()
    ax1.set_title('Kumaraswamy Distribution --> Histogram')
    ax1.set_xlabel('Random Numbers(x)')
    ax1.set_ylabel('P(x)')
    ax1.grid(True)
    ax1.hist(x,bins, density=True, cumulative=True, label='Empirical')

    legend = plt.legend(loc='upper left', shadow=True, fontsize='large')
    fig1.savefig('KUM_%s_%s_figHIST.pdf'% (a,b))
    #PDF file for Histogram Plot


    fig2, ax2 = plt.subplots()
    ax2.boxplot(x)
    plt.show()
    fig2.savefig('KUM_%s_%s_figBOX.pdf'% (a,b))
    #PDF file for Histogram Plot

    
   

print('1: Logarithmic Distribution')
print('2: Kumaraswamy Distribution')
print('3: Exit')


while(True):
    opt = int(input('Select an option : '))
    if opt == 1:
        logarithmic()
        continue
    elif opt == 2:
        kumaraswamy()
        continue
    elif opt == 3:
        break
    else:
        print('Invalid Input!')
        continue