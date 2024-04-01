

from cerberus_smi.cerberus_smi_backend import *
from cerberus_smi.cerberus_smi_frontend import *



def main():
    """
    First entry point for CERBERUS.
    """
    cerberus_smi_backend = CerberusSMIBackend()
    cerberus_smi_app = CerberusSMIFrontend(backend = cerberus_smi_backend)

    cerberus_smi_app.run()

if __name__ == "__main__":
    main()
