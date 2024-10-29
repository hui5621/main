import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wang/桌面/item/chapter3/topic_ws/install/demo_python_topic'
