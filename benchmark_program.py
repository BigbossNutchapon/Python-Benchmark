from tkinter import*
from random import*
import time, random, cpuinfo, psutil, math, os

#Create Tkinter & Set Tkinter 
root = Tk()
root.title("Benchmark")
root.configure(bg = "#FFFFFF")
root.geometry("800x493+350+100")
root.resizable(0,0)
root.overrideredirect(1)

#Define image
BACKGROUD = PhotoImage(file="Window.png")

#Color
BACKGROUD_DEFAULT = "#F5F5F5"

#Font
FONT_DEFULT = ('Microsoft Yahei UI Light')

#button start default
text_Start = "Start"
bg_Start = '#0077b6'

#variable of result
result_CPU, result_Mem, result_Disk, result_Overall = 0,0,0,0
kb = float(1024)
gb = float(kb ** 3)

#Detail CPU & MEM & DISK
if(len(str(cpuinfo.get_cpu_info()["brand_raw"])) > len(str(cpuinfo.get_cpu_info()["brand_raw"][:30]))):
    info_cpu = str(cpuinfo.get_cpu_info()["brand_raw"][:30]+"...")
else:
    info_cpu = str(cpuinfo.get_cpu_info()["brand_raw"])
info_countcpu = "Processor: " + str(psutil.cpu_count(logical=FALSE)) + " core  " + str(psutil.cpu_count()) + " thread"
info_mem = "Memory: " + str(f"{psutil.virtual_memory()[0]/gb:.2f}") + "GB"

#Function Main
def mainPage():
    #Function Start
    def fnStart():
        global result_Overall
        labelCPU.config(text='0')
        labelMem.config(text='0')
        labelDisk.config(text='0')
        labelOverall.config(text='0')
        bench_CPU()
        bench_Memory()
        bench_Disk()
        result_Overall = result_CPU+result_Disk+result_Mem
        labelCPU.config(text=result_CPU)
        labelMem.config(text=result_Mem)
        labelDisk.config(text=result_Disk)
        labelOverall.config(text=result_Overall)
        labelWarnning.config(text=show_warnning)

    #Function Benchmark CPU
    def bench_CPU():
        global result_CPU
        start = time.time()
        end = start + 300
        count = 0
        check = 2
        s = True
        while s:
            for i in range(1, check + 1):
                if (check % i == 0) and i != 1 and i != check:
                    a = i
                    b = a + check
                    c = a + b
                    d = c * math.pi
                    break
                if (time.time() > end):
                    s = False
                    break
            count += 1
            check += 1
        result_CPU = (count // 34)

    #Function Benchmark Memory
    def bench_Memory():
        global result_Mem
        start = time.time()
        end = start + 300
        count = 0
        data = []
        seed(15)
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        data.append(random.randint(1, 1000))
        while True:
            start = time.time()
            if (start < end):
                number = random.choice(data) + random.choice(data)
                data.append(number)
                count += 1
            else:
                break
        result_Mem = (count // 33891)

    #Function Benchmark Disk
    def bench_Disk():
        global result_Disk, show_warnning
        count = 0
        data = open("benchmarkss1.txt", "w")
        start = time.time()
        end = start + 300
        x = "We are the best team" * 20
        try :
            while True:
                start = time.time()
                if (start < end):
                    data.write(x)
                    count += 1
                else:
                    break
            show_warnning = ""
        except OSError as e:
            show_warnning = "Not fully processing performance\nlow disk space"
        result_Disk = (count // 24038)
        data.close()
        os.remove("benchmarkss1.txt")

    #GUI
    #Set backgroud
    My_Bg = Label(root, image=BACKGROUD, width=800, height=500)
    My_Bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    #Frame of CPU & Lable of CPU
    frame_Cpu = Frame(root,width=190,height=70,bg=BACKGROUD_DEFAULT)
    frame_Cpu.place(x=56+1.5,y=150)
    labelCPU = Label(frame_Cpu,text=result_CPU,font=(FONT_DEFULT,18,'bold'),justify=CENTER,width=13,bg=BACKGROUD_DEFAULT)
    labelCPU.place(x=0,y=10)

    #Frame of Memory & Lable of Memory
    frame_Mem = Frame(root,width=190,height=70,bg=BACKGROUD_DEFAULT)
    frame_Mem.place(x=303+1.5,y=150)
    labelMem = Label(frame_Mem,text=result_Mem,font=(FONT_DEFULT,18,'bold'),justify=CENTER,width=13,bg=BACKGROUD_DEFAULT)
    labelMem.place(x=0,y=10)

    #Frame of Disk & Lable of Disk
    frame_Disk = Frame(root,width=190,height=70,bg=BACKGROUD_DEFAULT)
    frame_Disk.place(x=550+1.5,y=150)
    labelDisk = Label(frame_Disk,text=result_Disk,font=(FONT_DEFULT,18,'bold'),justify=CENTER,width=13,bg=BACKGROUD_DEFAULT)
    labelWarnning = Label(frame_Disk,text="",font=(FONT_DEFULT,7),justify=CENTER,width=35,bg=BACKGROUD_DEFAULT)
    labelWarnning.place(x=5,y=40)
    labelDisk.place(x=0,y=10)

    #Frame of Detail & Lable of Detail
    frame_Detail = Frame(root,width=190,height=70,bg=BACKGROUD_DEFAULT)
    frame_Detail.place(x=173+1.5,y=317)
    labelDetail = Label(frame_Detail,text=info_cpu+"\n"+info_countcpu + "\n" +info_mem,font=(FONT_DEFULT,8),justify=LEFT,width=30,bg=BACKGROUD_DEFAULT)
    labelDetail.place(x=0,y=7)

    #Frame of Overall & Lable of Overall
    frame_Overall = Frame(root,width=190,height=70,bg=BACKGROUD_DEFAULT)
    frame_Overall.place(x=421+1.5,y=320)
    labelOverall = Label(frame_Overall,text=result_Overall,font=(FONT_DEFULT,18,'bold'),justify=CENTER,width=13,bg=BACKGROUD_DEFAULT)
    labelOverall.place(x=0,y=10)

    #Button Exit
    Button(width=10,pady=0,text='Exit',bg='red',fg='white',border=0,cursor='hand2',
font=(FONT_DEFULT,11,'bold'),command=root.quit).place(x=685,y=10)

    #Button Start
    button_Start = Button(width=10,pady=0,text=text_Start,bg=bg_Start,fg='white',border=0,cursor='hand2',
font=(FONT_DEFULT,18,'bold'),command=fnStart)
    button_Start.place(x=310,y=430)

#Function main for run program
def main():
    mainPage()

#call Fn main & run GUI of Tkinter
main()
root.mainloop()