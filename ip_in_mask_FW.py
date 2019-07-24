import socket, struct, ipaddr

def ip2long(ip):#convierte octetos a long
    return struct.unpack("!L", socket.inet_aton(ip))[0]

def long2ip(ip):#convierte long en octetos
    return socket.inet_ntoa(struct.pack("!L",ip))

def ipmask(bits):#crea un mascara de la cantidad bits en formato long
    return ((1<<(bits))-1)<<(32-bits)

def iprange(ip,mask):#entrega una tupla con la primera y ultima ip del rango
   return [ip&ipmask(mask),ip|(ipmask(mask)^(1<<32)-1)]
   
myArray=[]

for line in open("./ips_with_mask.txt"):
	myArray.append(line)
	
for ipconsulta in open("./ips_to_found.txt"):	

	for pool in myArray:
#		print("Validando ip: " + ipconsulta)
		ip,mask = pool.split('/')

		mask = int(mask)

		longIP  = ip2long(ip)
		extremos = iprange(longIP,mask)
		
		ipconsulta2 = ip2long(ipconsulta)

		if ipconsulta2 >= extremos[0] and ipconsulta2 <= extremos[1] :
			print(ipconsulta + " in range")

