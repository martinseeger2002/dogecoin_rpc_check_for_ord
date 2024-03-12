#getTXIDinfo.py
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def load_rpc_credentials(filename):
    """
    Load RPC credentials from a configuration file.
    The file should contain lines in the format 'key=value'.
    """
    credentials = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, _, value = line.strip().partition('=')
                if key and value:
                    credentials[key] = value
        return credentials
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return {}

def get_rpc_connection(credentials):
    """
    Establish an RPC connection using credentials.
    """
    rpc_user = credentials.get("rpc_user", "default_user")
    rpc_password = credentials.get("rpc_password", "default_password")
    rpc_port = credentials.get("rpc_port", "22555")
    rpc_ip = credentials.get("rpc_ip", "localhost")  # Corrected typo 'localost'
    return AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_ip}:{rpc_port}")


def getTXIDinfo(TXID):
    # Load RPC credentials
    credentials = load_rpc_credentials('RPC.conf')
    if not credentials:
        print("Failed to load RPC credentials.")
        return {'error': "Failed to load RPC credentials."}

    # Establish RPC connection
    rpc_connection = get_rpc_connection(credentials)
    try:
        # Retrieve transaction details
        transaction = rpc_connection.getrawtransaction(TXID, 1)

        # Extract the 'asm' field from 'scriptSig'
        script_sig_asm = transaction['vin'][0]['scriptSig']['asm']
        
        # Extract input details
        input_details = []
        for vin in transaction['vin']:
            input_txid = vin['txid']
            input_vout_index = vin['vout']
            input_tx = rpc_connection.getrawtransaction(input_txid, 1)
            input_amount = input_tx['vout'][input_vout_index]['value']
            input_details.append({'txid': input_txid, 'amount': input_amount})

        # Extract output details
        output_details = [{'txid': f"{TXID}:{vout['n']}", 'amount': vout['value']} for vout in transaction['vout']]

        # Return the collected data
        return {'script_sig_asm': script_sig_asm, 'input_details': input_details, 'output_details': output_details}

    except JSONRPCException as e:
        print(f"Error: {e}")
        return {'error': str(e)}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {'error': str(e)}
