import re
seq: str = 'ATGCAATCGACTACGATCAATCGAGGGCC'

fragments = re.findall('GAATTC', seq)
num = len(fragments) / 6
print('The total number of fragments is:', num)
