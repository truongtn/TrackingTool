def ngoaile(noidung):


        if noidung.find("currentServerDate")!=-1:
                string =""
                vitri = noidung.find("currentServerDate")

                vitri1 = noidung.find("'",vitri)+1
                vitri2 = noidung.find("'",vitri1)
                for i in range(vitri1,vitri2):
                        string+=noidung[i]
                noidung = noidung.replace(string,"")

        if noidung.find("session_id=")!=-1:
                string =""
                vitri = noidung.find("session_id=")+len("session_id=")


                vitri2 = noidung.find('"',vitri)

                for i in range(vitri,vitri2):
                        string=string+noidung[i]
       
                noidung = noidung.replace(string,"")
  
        if noidung.find("rand=")!=-1:
                string=""
                randvt1 = noidung.find("rand=")
                randvt1end =  noidung.find('"',randvt1+2)
                for i in range(randvt1+5,randvt1end):
                        string+=noidung[i]
                noidung = noidung.replace(string,"")
             
                string=""
                randvt2 = noidung.find("rand=",randvt1+1)
                randvt2end =  noidung.find('"',randvt2+2)

          
                for i in range(randvt2+5,randvt2end):
                        string+=noidung[i]
                noidung = noidung.replace(string,"")
            
        return noidung


