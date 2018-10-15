# bash-comands


#leer archivos en una línea

while IFS= read -r line; do echo $line; done < prueba.txt

#Imprimir ips con el servicio a la escucha

grep "open  telnet" -B 5 resultado_ips.txt | grep Nmap  | awk '{print $6}' | sed 's/(//g' | sed 's/)//g'
