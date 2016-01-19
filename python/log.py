# -*- coding: cp936 -*-
import logging
# ����һ��logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)
# ����һ��handler������д����־�ļ�
file_h = logging.FileHandler('test.log')
file_h.setLevel(logging.DEBUG)
# ����һ��handler���������������̨
console_h = logging.StreamHandler()
console_h.setLevel(logging.DEBUG)
# ����handler�������ʽ
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')
file_h.setFormatter(formatter)
console_h.setFormatter(formatter)
# ��logger���handler
logger.addHandler(file_h)
logger.addHandler(console_h)
# ��¼һ����־
logger.info('Info')
logger.debug('Debug')
