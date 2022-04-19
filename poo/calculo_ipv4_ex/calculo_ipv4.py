from ntpath import join


class CalculoIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara 
        self.prefixo = prefixo 

        self.dec_to_bin(ip)

    @property
    def ip(self):
        return self._ip
    
    @property
    def mascara(self):
        return self._mascara
    
    @property
    def prefixo(self):
        return self._prefixo
    
    @ip.setter
    def ip(self, valor):
        self._ip = valor
    
    @mascara.setter 
    def mascara(self, valor):
        self._mascara = valor 
    
    @prefixo.setter 
    def prefixo(self, valor):
        self._prefixo = valor 
    

    @staticmethod
    def dec_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        print(blocos_bin_str)
        
