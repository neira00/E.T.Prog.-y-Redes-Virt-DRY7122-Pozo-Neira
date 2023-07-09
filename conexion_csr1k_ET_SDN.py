from ncclient import manager

router = {
    'host': '192.168.56.104',  # Dirección IP del router CSR1000v
    'port': 22,  # Puerto SSH del router (por defecto es 22)
    'username': 'cisco',  # nombre de usuario para acceso al csr
    'password': 'cisco123!'  # contraseña para cceso al csr
}

new_hostname = 'Pozo_Neira'

config_change_hostname = f"""
<config>
    <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
        <hostname>{new_hostname}</hostname>
    </system>
</config>
"""

config_create_loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback1</name>
            <description>Interfaz Loopback 1</description>
            <ipv4>
                <address>
                    <ip>1.1.1.1</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    m.edit_config(target='running', config=config_change_hostname)
    m.edit_config(target='running', config=config_create_loopback)

