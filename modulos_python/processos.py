import subprocess


# Windows - ping 127.0.0.1

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

saida = proc.stdout
erro = proc.stderr
codigo_retorno = proc.returncode
argumentos = proc.args
