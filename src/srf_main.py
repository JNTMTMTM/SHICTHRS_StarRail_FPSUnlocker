
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
# 导入GUI框架
from PySide6.QtWidgets import (QApplication , QMainWindow)
from PySide6 import QtGui
from ui.sfr_ui import Ui_srf
# 导入解锁方法
from utils.unlocker.srf_fps_unlocker import srf_fps_unlocker

class sfr_gui(Ui_srf , QMainWindow):
    # 初始化窗口
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)  
        self.__slot__()
        self.show()

    # 绑定槽函数
    def __slot__(self) -> None:
        pass



# 主函数
if __name__ == '__main__':
    # 读取程项目路径
    PATH = os.getcwd()
    # 初始化GUI
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QtGui.QIcon(os.path.join(PATH , 'icon' , 'logo_32x32.ico')))
    # 实例化窗口
    main = sfr_gui()
    # 主循环
    sys.exit(app.exec())


