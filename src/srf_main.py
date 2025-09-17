
# # -*- coding: utf-8 -*-

# SHICTHRS StarRail FPSUnlocker
# 立项时间 20250917
# 开发人员 : 鸡哥

# © 2025-2026 SHICTHRS, Std. All rights reserved.

# 算法诠释一切 质疑即是认可
# Algorithms = rule ; Questioning = approval

import sys
sys.path.append('..')
import os

from PySide6.QtWidgets import (QApplication , QMainWindow)
from PySide6 import QtGui
from ui.sfr_ui import Ui_srf


class sfr_gui(Ui_srf , QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  
        self.show()




if __name__ == '__main__':
    PATH = os.getcwd()

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(PATH , 'icon' , 'logo_32x32.ico')))

    main = sfr_gui()
    sys.exit(app.exec())


