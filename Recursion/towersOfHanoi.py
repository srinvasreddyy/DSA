def TOH(From,to,via,n):
    if n== 1:
        print(f'Disk {From} to {to}')
    else:
        TOH(From,via,to,n-1)
        print(f'Disk {From} to {to}')
        TOH(via,to,From,n-1)
From= 'A'
to= 'C'
via= 'B'
TOH(From,to,via,2)