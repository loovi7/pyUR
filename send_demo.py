# -*- encoding:utf-8 -*-
import UR_Commands as uc

if __name__ == '__main__':
    # q = [-1.5897057, -0.49691067, -1.6831130, -0.787268, 1.0850005, 0.210137]
    # qd = [0, 0, 0, 0, 0, 0.1]
    # uc.movej_list(q,1,0.1)
    # uc.speedj_list(qd, 1, 5)
    # uc.movej_enum(-1.7897057, -0.49691067, -1.6831130, -0.787268, 1.0850005, 0.210137, 1, 0.1)
    # uc.speedj_enum(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 3)
    uc.send_script("test.urscript")
