print("                                                                      ")
print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆Madokomputer☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
print("       =====Menjual Komputer=====")
print("Pilih Socket LGA : 1.LGA 1700\n                   2.LGA 1155             ")
socketLga = input("Pilih Socket [1/2] : ")
def fungsiLga1700():
    
    print("Pilih Prosessor : 1.Intel Core i9 14900  |    Rp.9.000.000")
    print("                  2.Intel Core i7 14700  |    Rp.6.245.000")
    print("                  3.Intel Core i5 14500f |    Rp.4.150.000")
    print("                  4.Intel Core i3 14100  |    Rp.2.500.000")
    
    pilihCPU = input("Pilih Prosessor [1/2/3/4] : ")
    pilihCPU = int(pilihCPU)
    
    if pilihCPU == 1:
        pilihCPU = 9000000
        
    
    elif pilihCPU == 2: 
        pilihCPU = 6245000
       
    
    elif pilihCPU == 3:
        pilihCPU = 4150000
        
    
    elif pilihCPU == 4:
        pilihCPU = 2500000
        
    
    else :
        print("error")
    
  
    print("Pilih RAM : 1.Corsair Vengeance 5600Mhz 2x32GB DDR5 | Rp.3.600.000")
    print("            2.Corsair Vengeance 5200Mhz 2x32GB DDR5 | Rp.2.600.000")
    print("            3.TeamGroup T-Crate 3200Mhz 2x32GB DDR4 | Rp.2.300.000")
    
    pilihRAM = input("Pilih RAM [1/2/3] : ")
    pilihRAM = int(pilihRAM)
    
    if pilihRAM == 1:
        pilihRAM = 3600000
    
    elif pilihRAM == 2: 
        pilihRAM = 2600000
    
    elif pilihRAM == 3:
        pilihRAM = 2300000
    
    else :
        print("error")
        
 
    print("Pilih VGA : 1.ASUS ROG RTX 4090 OC 24GB GDDR6X | Rp.40.000.000")
    print("            2.Colorful RTX 3080 OC 10GB GDDR6X | Rp.16.000.000")
    print("            3.Zotac Gaming RTX 4080 SUPER 16GB | Rp.16.400.000")
    
    pilihVGA = input("Pilih VGA [1/2/3] : ")
    pilihVGA = int(pilihVGA)
    if pilihVGA == 1:
        pilihVGA = 40000000
    
    elif pilihVGA == 2: 
        pilihVGA = 16000000
    
    elif pilihVGA == 3:
        pilihVGA = 16400000
    
    
    else :
        print("error")
   
    total = pilihCPU + pilihRAM + pilihVGA
    totalharga = "Total Pembelian : " + str(total)
   #CPU
    if pilihCPU == 9000000:
        cpu = "Intel Core i9 14900  |    Rp.9.000.000"
    elif pilihCPU == 6245000:
        cpu = "Intel Core i7 14700  |    Rp.6.245.000"
    elif pilihCPU == 4150000:
        cpu = "Intel Core i5 14500f |    Rp.4.150.000"
    elif pilihCPU == 2500000:
        cpu = "Intel Core i3 14100  |    Rp.2.500.000"
    #CPU
    #RAM
    if pilihRAM == 3600000:
        ram = "Corsair Vengeance 5600Mhz 2x32GB DDR5 | Rp.3.600.000"
    elif pilihRAM == 2600000:
        ram = "Corsair Vengeance 5200Mhz 2x32GB DDR5 | Rp.2.600.000"
    else :
        ram = "TeamGroup T-Crate 3200Mhz 2x32GB DDR4 | Rp.2.300.000"
    #RAM
    #VGA
    if pilihVGA == 40000000:
        vga = "ASUS ROG RTX 4090 OC 24GB GDDR6X | Rp.40.000.000"
    elif pilihVGA == 16000000:
        vga = "Colorful RTX 3080 OC 10GB GDDR6X | Rp.16.000.000"
    else :
        vga = "Zotac Gaming RTX 4080 SUPER 16GB | Rp.16.400.000"
    print("                                        ")
    print("☆☆☆v☆☆☆☆☆☆☆☆☆☆☆MikaKomputer☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("                                        ")
    print("========== S T R U K   B E L I ==============")
    print("=============================================")
    print("CPU\t\t:", cpu,)
    print("RAM\t\t:", ram,)
    print("VGA\t\t:", vga,)
    print("TOTAL   : Rp. ", totalharga,)
    print("============================================")
    print("============================================")
    
def fungsiLga1155():
    
    print("Pilih Prosessor : 1.Intel Core i7 3770  |    Rp.700.000")
    print("                  2.Intel Core i5 3470  |    Rp.200.000")
    print("                  3.Intel Core i5 2400  |    Rp.150.000")
    print("                  4.Intel Core i3 3220  |    Rp.60.000")
    print("                  5.Intel Core i3 2120  |    Rp.50.000")
    
    pilihCPU = input("Pilih Prosessor [1/2/3/4/5] : ")
    pilihCPU = int(pilihCPU)
    
    if pilihCPU == 1:
        pilihCPU = 700000
        
    
    elif pilihCPU == 2: 
        pilihCPU = 200000
       
    
    elif pilihCPU == 3:
        pilihCPU = 150000
        
    
    elif pilihCPU == 4:
        pilihCPU = 60000
    
    elif pilihCPU == 5:
        pilihCPU = 50000
    else :
        print("Tidak Ada Dalam Pilihan")
    
    print("Pilih RAM       : 1.Kingston DDR3 1600Mhz 8GB   |    Rp.200.000")
    print("                  2.Samsung DDR3 1600Mhz 4GB    |    Rp.100.000")
    print("                  3.Kingston DDR3 1333Mhz 8GB   |    Rp.200.000")
    print("                  4.Hynix DDR3 1333Mhz 4GB      |    Rp.60.000")
    
    pilihRAM = input("Pilih RAM [1/2/3/4] : ")
    pilihRAM = int(pilihRAM)
    
    if pilihRAM == 1: 
        pilihRAM = 200000
       
    
    elif pilihRAM == 2:
        pilihRAM = 100000
        
    
    elif pilihRAM == 3:
        pilihRAM = 200000
    
    elif pilihRAM == 4:
        pilihRAM = 60000
    else :
        print("Tidak Ada Dalam Pilihan")
    
    print("Pilih VGA       : 1.Nvidia GTX 560 1GB 256BIT GDDR5    |    Rp.350.000")
    print("                  2.Nvidia GTX 750Ti 2GB 128BIT GDDR5  |    Rp.800.000")
    print("                  3.Radeon RX 560 2GB 128BIT GDDR5     |    Rp.1.200.000")
    print("                  4.Nvidia GTS 450 512MB 128BIT GDDR5  |  Rp.250.000")
    
    pilihVGA = input("Pilih VGA [1/2/3/4] : ")
    pilihVGA = int(pilihVGA)
    
    if pilihVGA == 1:
        pilihVGA = 350000
        
    
    elif pilihVGA == 2: 
        pilihVGA = 800000
       
    
    elif pilihVGA == 3:
        pilihVGA = 1200000
        
    
    elif pilihVGA == 4:
        pilihVGA = 250000
    
    else :
        print("Tidak Ada Dalam Pilihan")
    
     #CPU
    if pilihCPU == 700000:
        cpu = "Intel Core i7 3770   |    Rp.700.000"
    elif pilihCPU == 200000:
        cpu = "Intel Core i5 3470   |    Rp.200.000"
    elif pilihCPU == 60000:
        cpu = "Intel Core i3 3220   |    Rp.60.000"
    elif pilihCPU == 150000:
        cpu = "Intel Core i5 2400   |    Rp.150.000"
    else :
        cpu = "Intel Core i3 2120   |    Rp.50.000"
    #CPU
    total = pilihCPU + pilihRAM + pilihVGA
    totalharga = "Total Pembelian : " + str(total)
    #RAM
    if pilihRAM == 200000:
        ram = "Kingston DDR3 1600Mhz 8GB  |    Rp.200.000"
    elif pilihRAM == 100000:
        ram = "Samsung DDR3 1600Mhz 4GB   |    Rp.100.000"
    elif pilihRAM == 200000 :
        ram = "Kingston DDR3 1333Mhz 8GB  |    Rp.200.000"
    else :
        ram = "Hynix DDR3 1333Mhz 4GB     |    Rp.60.000"
    #RAM
    #VGA
    if pilihVGA == 350000:
        vga = "Nvidia GTX 560 1GB 256BIT GDDR5    |    Rp.350.000"
    elif pilihVGA == 800000:
        vga = "Nvidia GTX 750Ti 2GB 128BIT GDDR5  |    Rp.800.000"
    elif pilihVGA == 1200000 :
        vga = "Radeon RX 560 2GB 128BIT GDDR5     |    Rp.1.200.000"
    else :
        vga = "Nvidia GTS 450 512MB 128BIT GDDR5  |  Rp.250.000"
    
    
    print("                                        ")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆MadoKomputer☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("                                        ")
    print("============== S T R U K   B E L I ====================")
    print("=======================================================")
    print("CPU\t\t:", cpu,)
    print("RAM\t\t:", ram,)
    print("VGA\t\t:", vga,)
    print("TOTAL   : Rp. ", totalharga,)
    print("=======================================================")
    print("=======================================================")
case = int(socketLga)
switch = {
    1:fungsiLga1700,
    2:fungsiLga1155,
}
switch[case]()