# bash-comands


#leer archivos en una línea

while IFS= read -r line; do echo $line; done < prueba.txt

#Imprimir ips con el servicio a la escucha

grep "open  telnet" -B 5 resultado_ips.txt | grep Nmap  | awk '{print $6}' | sed 's/(//g' | sed 's/)//g'


##Lectura de pcap desde consola con formato plano

sudo tcpdump -ttttnnr tcp_dump.pcap

##Captura de pcap desde consola windows, ejemplo captura DNS

.\WinDump.exe -i 2 -q -w C:\DNS_TCP2\DNS_TCP -n -C 30 -W 10 -U -s 0 tcp and port 53 
