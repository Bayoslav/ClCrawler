import threading

filename = "cuda.txt"
file = open(filename, "a")
for i in range(2,400,1):
    lines = ["  elif(length==" + str(i) + "):\n"]
    for j in range(1,i+1,1):
        lines.append("      thread" + str(j) + "=" + "MyThread(nisam[" + str(j-1) + "])\n")
    for k in range(1,i+1,1):
        lines.append("      thread" + str(k) + ".start()\n")
        lines.append("      threads.append(" + "thread" + str(k) + ")\n")
    file.writelines(lines)
file.close()
