
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
from PySide6.QtWidgets import (QApplication , QMainWindow , QMessageBox)
from PySide6 import QtGui
from ui.sfr_ui import Ui_srf
# 导入解锁方法
from utils.unlocker.srf_fps_unlocker import srf_fps_unlocker
# 导入json io方法
from utils.json.srf_read_json import ReadJsonFile
from utils.json.srf_verify_json import VerifySacJfpOrder
from copy import deepcopy


class sfr_gui(Ui_srf , QMainWindow):
    # 初始化窗口
    def __init__(self) -> None:
        # 加载窗口
        super().__init__()
        self.setupUi(self)  

        # 绑定槽函数
        self.__slot__()

        # 显示窗口
        self.show()

        # 加载软件信息
        self.LoadRegeditInfo()

        # 加载当前游戏FPS上限



    # 绑定槽函数
    def __slot__(self) -> None:
        pass

    # 加载软件信息
    def LoadRegeditInfo(self) -> None:
        """
        加载软件信息(JSON) <-> SAC_JFP VERIFICATION
        temp_dict -> var.SRF_INFO(DC)

        GUI-LOADED -> lb_index_0_regedit_path
            [+] lb_index_0_regedit_path
            [+] lb_index_0_graphics_index
            [+] lb_index_1_version_info
            [+] lb_index_1_github_link

        param : None
        return : None
        """

        temp_dict : dict = {}  # json临时加载空间
        temp_dict = ReadJsonFile(os.path.join(var.PATH , 'config' , 'srf_info.json'))  # 读取json文件
        
        # SAC_JFP校验
        if VerifySacJfpOrder(temp_dict):  # 校验通过
            var.SRF_INFO = deepcopy(temp_dict)
            del temp_dict  # 释放临时空间
            # 向控件加载软件信息
            self.lb_index_0_regedit_path.setText('注册表路径 : ' + os.path.join(*var.SRF_INFO['PATH']['REGISTRY_KEY_PATH']))
            self.lb_index_0_graphics_index.setText('图形设置引导 : ' + var.SRF_INFO['PATH']['GRAPHICS_VALUE_NAME'])
            self.lb_index_1_version_info.setText(f'版本信息 : {var.SRF_INFO['VERSION']['VERSION_INDEX']} - {var.SRF_INFO['VERSION']['UPDATE_TIME']}')
            self.lb_index_1_github_link.setText(f'<a href="{var.SRF_INFO['PATH']['GITHUB_REPO_URL']}">项目地址 : {var.SRF_INFO['PATH']['GITHUB_REPO_URL'].split('/')[-1]}</a>')
            self.lb_index_1_github_link.setOpenExternalLinks(True)  # 激活超链接



        else:  # 校验不通过
            pass

class sfr_var():
    def __init__(self) -> None:
        self.PATH : str = os.getcwd()
        self.SRF_INFO : dict = {}

# 主函数
if __name__ == '__main__':
    var = sfr_var()
    # 初始化GUI
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QtGui.QIcon(os.path.join(var.PATH , 'icon' , 'logo_32x32.ico')))
    # 实例化窗口
    main = sfr_gui()
    # 主循环
    sys.exit(app.exec())


