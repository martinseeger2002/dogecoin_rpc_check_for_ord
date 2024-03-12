#findOrd.py
from getTXIDinfo import getTXIDinfo
from decimal import Decimal


TXID = '25350e407f3e78be762f19ea7508f7c61a75b946ff79f569be25535771459d18'


def find_sequence_in_txid(txid, sequence):
    transaction_info = getTXIDinfo(txid)
    if 'error' in transaction_info:
        print(f"Error fetching transaction info for TXID {txid}: {transaction_info['error']}")
        return False

    if sequence in transaction_info['script_sig_asm']:
        print(f"{txid} is ord!")
        return True

    valid_inputs = [input_detail for input_detail in transaction_info['input_details'] 
                    if input_detail['amount'] == Decimal('0.001')]
    
    if not valid_inputs:
        print(f"{txid} has no input of 0.001")
        return False

    for input_detail in valid_inputs:
        if find_sequence_in_txid(input_detail['txid'], sequence):
            return True

    return False

find_sequence_in_txid(TXID, "6582895")