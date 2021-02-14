
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import haveibeenpawned.main

if __name__ == "__main__":
    haveibeenpawned.main.main(sys.argv[1:])
