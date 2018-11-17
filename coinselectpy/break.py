from decimal import Decimal
from . import utils

def broken(utxos, output, feeRate):
    bytesAccum = utils.transactionBytes(utxos, [])
    try:
        feeRate = Decimal(feeRate)
        value = Decimal(output.value)
        inAccum = utils.sumOrNaN(utxos)
    except Exception:
        return {'fee': round(feeRate * bytesAccum)}

    outputBytes = utils.outputBytes(output)
    outAccum = 0
    outputs = []

    while True:
        fee = feeRate * (bytesAccum + outputBytes)

        # did we bust?
        if inAccum < (outAccum + fee + value):
            # premature?
            if outAccum == 0:
                return {'fee': round(fee)}
            break

        bytesAccum += outputBytes
        outAccum += value
        outputs.push(output)

    return utils.finalize(utxos, outputs, feeRate)
