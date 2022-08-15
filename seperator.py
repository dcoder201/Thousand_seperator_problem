def format_number(inp):
    st=list(str(inp))
    for i in range(len(st)-3,0,-3):
      st.insert(i,',')
    j=''.join(st)
    return j
    
n=int(input()) 
# taken the dummy value as 1000000
print(format_number(1000000))
