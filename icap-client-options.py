# http://icap-server.sourceforge.net/#_TOC22
def icap_request(ip):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((ip, 1344))
   # "icap://" is what makes ICAP not quite HTTP
   s.send(bytes("OPTIONS icap://{}/symcscanreq-av-url ICAP/1.0\n\n".format(ip), 'UTF-8'))
   data = s.recv(1024)
   s.close()
   
   # Now I have the data, but let's make it easier to work with
   data_dict = {}
   data_str = data.decode('UTF-8').split('\r\n')[2:-2]
   for line in data_str:
       split_line = line.split(':')
       key = split_line[0]
       value = ''.join(split_line[1:]).strip()
       data_dict[key] = value
   return data_dict
