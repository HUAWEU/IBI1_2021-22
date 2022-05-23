<<<<<<< HEAD
import re
seq: str = 'ATGCAATCGACTACGATCAATCGAGGGCC'

fragments = re.findall('GAATTC', seq)
num = len(fragments) / 6
print('The total number of fragments is:', num)
=======
import re
seq: str = 'ATGCAATCGACTACGATCAATCGAGGGCC'

fragments = re.findall('GAATTC', seq)
num = len(fragments) / 6
print('The total number of fragments is:', num)
>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31
