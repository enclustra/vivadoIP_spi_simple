##############################################################################
#  Copyright (c) 2019 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################

import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(THIS_DIR + "/../sim")

os.system("vsim -c -do ci.do")

with open("Transcript.transcript") as f:
	content = f.read()
	
#Expected Errors
if "###ERROR###" in content:
	exit(-1)
#Unexpected Errors
if "SIMULATIONS COMPLETED SUCCESSFULLY" not in content:
	exit(-2)
	
	
#Success
exit(0)