print(1)
print('hano')
def Hano(N,Source,Target,Auxilirary):
     if N > 0:
          Hano(N-1,Source,Auxilirary,Target)
          print(f"将盘子 {N} 从 {Source} 移动到 {Target}")
          Hano(N-1,Auxilirary,Target,Source)
Hano(3,"A","C","B")
