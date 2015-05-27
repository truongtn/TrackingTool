def tachhead(noidung):
    ketqua=""
    a= noidung.find("<head>")+len("<head>")
    b = noidung.find("</head>",a)
    for i in range(a,b):
        ketqua+=noidung[i]
    return ketqua

