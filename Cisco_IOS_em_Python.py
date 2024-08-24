Cisco IOS
Navegação no IOS Cisco – Configuração do Switch


Modo EXEC com privilégios:
Switch> enable


Modo de configuração global:
Switch# configure terminal


Modo de configuração de linhas:
Switch(config)# line console 0


Sair do modo de configuração de linhas:
Switch(config-line)# exit


Modo de subconfiguração:
Switch(config)# interface vlan 1
Switch(config-if)# end


Mostrar informações do sistema:
Switch# ?


Nomear dispositivo:
Switch(config)# hostname SW-1


Configurar senha no modo EXEC:
SW-1(config)# line console 0
SW-1(config-line)# password cisco
SW-1(config-line)# login
SW-1(config-line)# end
SW-1# exit


Configurar senha à linha VTY:
SW-1(config)# enable secret class
SW-1(config)# line vty 0 15
SW-1(config-line)# password cisco
SW-1(config-line)# login
SW-1(config-line)# end
SW-1# exit


Criptografar senha:
SW-1(config)# service password-encryption
SW-1(config)# end
SW-1# show running-config


Mensagem Banner:
SW-1(config)# banner motd $ACESSO RESTRITO$


Arquivos de Configuração:
SW-1# copy running-config startup-config


Alterar a configuração de execução:
SW-1# reload
SW-1# wr
SW-1# erase startup-config


Salvar configurações:
SW-1# show running-config
SW-1# show startup-config


Configurar um endereço IP:
SW-1(config)# interface vlan 1
SW-1(config-if)# ip address 192.168.1.20 255.255.255.0
SW-1(config-if)# no shutdown
