import re


class CalculoIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara 
        self.prefixo = prefixo 

        if mascara and prefixo:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')

        if(self.mascara == None and self.prefixo == None):
            raise ValueError("Para o funcionamento correto é nescessario o envio da mascara ou do prefixo.")
        elif(self.mascara == None):
            self.mascara = self.build_mascara()
        else:
            self.prefixo = self.build_prefixo()

        self.rede = self.build_rede()
        self.broadcast = self.build_broadcast()
        self.quantidade_ips = self.build_quantidade_ip()

        
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
        if not self._valida_ip(valor):
            raise ValueError('IP inválido.')

        self._ip = valor
    
    @mascara.setter 
    def mascara(self, valor):
        self._mascara = valor
        
    @prefixo.setter 
    def prefixo(self, valor):
        self._prefixo = valor

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def dec_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_bin)
    
    @staticmethod
    def bin_to_dec(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32, 8)]
        return '.'.join(blocos)

    def build_prefixo(self):
        masc_bin = self.dec_to_bin(self._mascara)
        return masc_bin.count('1')

    def build_mascara(self):
        masc_bin = (self.prefixo * '1').ljust(32, '0')
        return self.bin_to_dec(masc_bin)

    def build_rede(self):
        rede = self.dec_to_bin(self.ip)[:self.prefixo].ljust(32, '0')
        return self.bin_to_dec(rede)

    def build_broadcast(self):
        broadcast = self.dec_to_bin(self.rede)[:self.prefixo].ljust(32, '1')
        return self.bin_to_dec(broadcast)
    
    def build_quantidade_ip(self):
        return 2 ** (32 - self.prefixo) - 2
