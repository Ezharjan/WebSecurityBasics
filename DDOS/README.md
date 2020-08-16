Dos攻击种类繁多，常见的有TCP Flood,UDP Flood,ICMP Flood,HTTP Flood...

TCP Flood:常称SYN Flood,因为ACK Flood代价太高，必须等到主机回应才能发送，这样也不能隐藏IP,因此不选ACK Flood攻击
UDP Flood:因为UDP是无连接的，因此纯粹就是发送大量无用数据冲洗带宽，显然不是很明智(相比于ACK Flood还需要目标主机维护一个队列来说)
ICMP Flood:学校里禁止Ping...不能用
HTTP Flood:又称CC攻击，直接手动请求网页即可，由于没有代理池，先将就着本机用吧

总体来说，由于是无线网卡，本机带宽太小，似乎Dos攻击不能起到应有的效果，如果有肉鸡效果应该会好很多
