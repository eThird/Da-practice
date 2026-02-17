def printrec(count,N):
    if count==N:
        return
    print(count)
    printrec(count+1,N)

printrec(0,3)