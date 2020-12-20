import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from insertion_sort import insertionsort
from heap_sort import heapsort


if __name__=="__main__":
    while True:
        n=int(input(" Input jumlah Array n: "))
        
        print('1. Heap Sort')
        print('2. Insertion Sort')
    
        ch=int(input("Enter your choice: "))
        
        y = np.random.randint(1,n+1,n)
        fig,axes = plt.subplots()
        
        if ch==1:
            title='HEAP SORT O(n**log(n))'
            generator = heapsort(y,n)
        elif ch==2:
            title='INSERTION SORT O(n**2)'
            generator = insertionsort(y)
            
        mycmap= cm.get_cmap('rainbow')
        
        my_norm = Normalize(vmin=0, vmax=100)
        
        
        barr = axes.bar(np.arange(1,n+1),y,align='edge',color=mycmap(my_norm(y)))
        axes.set_xticks(range(0,n+1,n//5))
        axes.set_yticks(range(0,n+1,n//5))
        text = axes.text(0.02, 0.95, "", transform=axes.transAxes)
        axes.set_title(title)
        
        count=0
        def outp(y,r):
            global count
            for a,b in zip(r,y):
                a.set_height(b)
            count+=1
            text.set_text("Number of Operations: "+str(count))
        
        anim = FuncAnimation(fig, outp, fargs=(barr,) ,frames = generator, interval=5, repeat=False)
        plt.show()
        ct = input("Apakah ingin mengulanginya lagi ?(y/n): ")
        if ct!='y' and ct!='Y':
            break
