import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wang/desktop/item/chapter5/chapt5_ws/install/demo_python_tf'
