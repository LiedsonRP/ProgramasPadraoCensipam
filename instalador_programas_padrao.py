import os

CHOCOLATELY_SITE = "'https://community.chocolatey.org/install.ps1'"
CHOCOLATELY_PACKAGE_INSTALL_COMMAND = f'@"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString({CHOCOLATELY_SITE}))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\\bin"'

programnsCode = {1:"JAVA", 2:"ADOBE-READER", 3:"GOOGLE", 4:"FIREFOX", 5:"LIBRE-OFFICE", 6:"AVAST", 7:"QGIS"}
defaultPrograms = {"JAVA": "server-jre", "ADOBE-READER": "adobereader", "GOOGLE": "googlechrome", "FIREFOX": "firefox", "LIBRE-OFFICE": "libreoffice-fresh",
                   "AVAST": "avastfreeantivirus", "QGIS": "qgis-ltr"}

'''
FUNÇÃO RESPONSÁVEL POR INSTALAR OS PROGRAMAS QUE POSSUEM PACOTE NO CHOCOLATELY
'''
def chocaletalyInstall(option):
    os.system(CHOCOLATELY_PACKAGE_INSTALL_COMMAND)
    print(f"Instalando {option}")
    os.system(f"choco install --confirm --reload {option}")

if __name__ == '__main__':

    print("-----------------------\nPROGRAMAS\n-----------------------")
    for code in programnsCode.keys():
        print(f"[{code}]" + programnsCode.get(code))

    codesSelected = input("Digite os códigos dos programas Ex: (1, 3 ou 234):")

    for option in codesSelected:
        program = programnsCode.get(int(option))
        chocaletalyInstall(defaultPrograms.get(program))
