
# # -*- coding: utf-8 -*-

# SHICTHRS StarRail FPSUnlocker
# 立项时间 20250917
# 开发人员 : 鸡哥

# © 2025-2026 SHICTHRS, Std. All rights reserved.

# 算法诠释一切 质疑即是认可
# Algorithms = rule ; Questioning = approval

from multiprocessing import current_process
import sys
sys.path.append('..')
import os
from copy import deepcopy
import winreg
import json
import threading
from win32api import GetShortPathName

# 导入GUI框架
from PySide6.QtWidgets import (QApplication , QMainWindow , QMessageBox)
from PySide6 import QtGui
from ui.sfr_ui import Ui_srf
# 导入解锁方法
from utils.unlocker.srf_fps_unlocker import SrfFpsUnlocker
from utils.unlocker.sfr_processes_scanner import GetAllProcesses
# 导入json io方法
from utils.json.srf_read_json import ReadJsonFile
from utils.json.srf_verify_json import VerifySacJfpOrder
from utils.regedit.srf_regedit_io import ReadRegistryValue
# 导入系统进程扫描器



class sfr_gui(Ui_srf , QMainWindow):  # 主窗口
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

        # 加载游戏路径
        self.LoadGamePathInfo()

        if os.path.exists(os.path.join(*var.SRF_INFO['PATH']['GAME_PATH'])):  # 游戏目录存在
            # 加载当前游戏FPS上限
            self.LoadCurrentGameFPSLimit()
        
        else:  # 游戏目录不存在
            QMessageBox.critical(self , 'SRF-错误' , '游戏目录不存在 , 请下载游戏或验证游戏目录完整性。')
            self.__quit()  # 退出方法

    # 绑定槽函数
    def __slot__(self) -> None:
        self.pbtn_index_0_unlock_fps.clicked.connect(self.__res_pbtn_index_0_unlock_fps)
        self.pbtn_index_1_start_game.clicked.connect(self.__res_pbtn_index_1_start_game)

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
        try:
            temp_dict : dict = {}  # json临时加载空间
            temp_dict = ReadJsonFile(os.path.join(var.PATH , 'config' , 'srf_info.json'))  # 读取json文件
            
            # SAC_JFP校验
            if VerifySacJfpOrder(temp_dict):  # 校验通过
                var.SRF_INFO = deepcopy(temp_dict)
                del temp_dict  # 释放临时空间

                # 向控件加载软件信息
                self.lb_index_0_regedit_path.setText('注册表路径 : ' + os.path.join(*var.SRF_INFO['PATH']['REGISTRY_KEY_PATH']))  # 注册表路径
                self.lb_index_0_graphics_index.setText('图形设置引导 : ' + var.SRF_INFO['PATH']['GRAPHICS_VALUE_NAME'])  # 图形设置引导
                self.lb_index_1_version_info.setText(f'版本信息 : {var.SRF_INFO['VERSION']['VERSION_INDEX']} - {var.SRF_INFO['VERSION']['UPDATE_TIME']}')  # 版本信息
                self.lb_index_1_github_link.setText(f'<a href="{var.SRF_INFO['PATH']['GITHUB_REPO_URL']}">项目地址 : {var.SRF_INFO['PATH']['GITHUB_REPO_URL'].split('/')[-1]}</a>')  # 项目地址
                self.lb_index_1_github_link.setOpenExternalLinks(True)  # 激活超链接

            else:  # 校验不通过
                if QMessageBox.question(self , 'SRF-错误' , 'JSON文件校验失败 , 请检查JSON文件是否完整或已损坏。\n是否尝试重新读取 ?' , QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:  # 用户选择是 重载
                    self.LoadRegeditInfo()  # 重载方法

                else:  # 用户选择否 退出
                    self.__quit()  # 退出方法

        except Exception as e:  # 发生错误 退出
            QMessageBox.critical(self , 'SRF-错误' , f'JSON文件读取失败 , 请检查JSON文件是否完整或已损坏。\n错误信息 : {e}')
            self.__quit()  # 退出方法

    # 读取游戏路径
    def LoadGamePathInfo(self) -> None:
        """
        读取游戏路径(ALV-JSON) <-> SAC_JFP VERIFICATION
        temp_value -> var.SRF_INFO(DC)
        """
        # 从注册表中读取键值
        temp_path : str = ''  # 临时路径
        temp_path = ReadRegistryValue(
            winreg.HKEY_CURRENT_USER ,  # 从当前用户的注册表路径中读取
            os.path.join(*var.SRF_INFO['PATH']['GAME_REGISTRY_KEY_PATH']) ,        # 注册表的具体路径
            var.SRF_INFO['PATH']['GAME_VALUE_NAME']       # 需要读取的键值名称
        )
        temp_path = temp_path.split('\\')  # 分割路径
        temp_path.append(var.SRF_INFO['PATH']['GAME_NAME'])  # 添加游戏名称

        var.SRF_INFO['PATH']['GAME_PATH'] = deepcopy(temp_path)
        
        del temp_path  # 释放临时空间
    
    # 加载当前游戏FPS上限
    def LoadCurrentGameFPSLimit(self) -> None:
        """
        加载当前游戏FPS上限(ALV-JSON) <-> SAC_JFP VERIFICATION
        temp_value -> None
        temp_format_value -> var.SRF_REGEDIT_INFO(DC)

        GUI-LOADED -> lb_index_0_current_fps
            [+] pbtn_index_0_unlock_fps
            [+] rb_index_0_unlock_120fps
            [+] rb_index_0_rlb_60fps

        param : None
        return : None
        """
        try:
            temp_value : dict = {}  # 创建临时加载空间
            temp_format_value : dict = {}  # 创建临时格式化加载空间

            temp_value = ReadRegistryValue(
                winreg.HKEY_CURRENT_USER ,
                os.path.join(*var.SRF_INFO['PATH']['REGISTRY_KEY_PATH']) ,
                var.SRF_INFO['PATH']['GRAPHICS_VALUE_NAME']
                )
            temp_format_value = json.loads(temp_value.decode('utf-8').strip('\x00'))

            var.SRF_REGEDIT_INFO = deepcopy(temp_format_value)
            var.SRF_INFO['OTHERS']['CURRENT_FPS'] = deepcopy(var.SRF_REGEDIT_INFO['FPS'])

            del temp_value  # 释放临时空间
            del temp_format_value  # 释放临时格式化空间

            # 向控件加载当前游戏FPS上限
            self.lb_index_0_current_fps.setText(f'当前帧率 : {var.SRF_INFO['OTHERS']['CURRENT_FPS']}')  # 当前帧率

            # 解锁控件
            if var.SRF_INFO['OTHERS']['CURRENT_FPS'] != 120:  # 当前帧率不是120FPS
                self.rb_index_0_unlock_120fps.setChecked(True)  # 默认选中120FPS
            
            else:  # 当前帧率已经为120FPS
                self.rb_index_0_rlb_60fps.setChecked(True)  # 默认选中60FPS
            
            self.pbtn_index_0_unlock_fps.setEnabled(True)  # 解锁按钮可用
    
        except Exception as e:
            QMessageBox.critical(self , 'SRF-错误' , f'注册表读取失败 , 请下载游戏或验证游戏目录完整性。\n错误信息 : {e}')
            self.__quit()  # 退出方法

    # 响应 pbtn_index_0_unlock_fps 点击信号 解锁FPS
    def __res_pbtn_index_0_unlock_fps(self) -> None:
        """
        响应 pbtn_index_0_unlock_fps(ALV-JSON) 点击信号 <-> 解锁FPS

        FUNC-LOADED -> LoadRegeditInfo
            [+] LoadCurrentGameFPSLimit
            [+] GetAllProcesses

        param : None
        return : None
        """
        # 检查游戏是否在运行
        current_process_list : list = GetAllProcesses()  # 获取当前进程列表
        if not var.SRF_INFO['PATH']['GAME_NAME'] in current_process_list:  # 游戏不在运行
        
            if self.rb_index_0_unlock_120fps.isChecked():  # 用户选择120FPS
                try:
                    SrfFpsUnlocker(var , 120)
                    QMessageBox.information(self , 'SRF-提示' , 'FPS解锁成功 , 重启游戏生效。')
                except Exception as e:
                    QMessageBox.critical(self , 'SRF-错误' , f'FPS解锁失败 , 请检查游戏目录完整性。\n错误信息 : {e}')

            else:  # 用户选择60FPS
                try:
                    SrfFpsUnlocker(var , 60)
                    QMessageBox.information(self , 'SRF-提示' , 'FPS回滚成功 , 重启游戏生效。')
                except Exception as e:
                    QMessageBox.critical(self , 'SRF-错误' , f'FPS回滚失败 , 请检查游戏目录完整性。\n错误信息 : {e}')
            
            self.LoadRegeditInfo()
            self.LoadGamePathInfo()
            self.LoadCurrentGameFPSLimit()
        
        else:  # 游戏在运行
            QMessageBox.warning(self , 'SRF-警告' , '游戏正在运行 , 请先关闭游戏后再进行操作。')

    # 响应 pbtn_index_1_start_game 点击信号 启动游戏
    def __res_pbtn_index_1_start_game(self) -> None:
        """
        响应 pbtn_index_1_start_game(Win32api) 点击信号 <-> 启动游戏

        FUNC-LOADED -> None

        param : None
        return : None
        """
        def LaunchGame(game_path : str) -> None:  # 启动游戏
            os.system(game_path)   

        try:
            temp_path : str = GetShortPathName(os.path.join(*var.SRF_INFO['PATH']['GAME_PATH']))  # 获取短路径名称
            threading.Thread(target = LaunchGame , args = (temp_path,)).start()
            
        except Exception as e:
            QMessageBox.critical(self , 'SRF-错误' , f'游戏启动失败 , 请检查游戏目录完整性。\n错误信息 : {e}')

    # 退出
    def __quit(self) -> None:
        """
        安全退出程序
        -用于异常退出

        param : None
        return : None
        """
        sys.exit(0)

    # 重写退出事件
    def closeEvent(self, event) -> None:
        """
        重写退出事件
        -当用户点击关闭按钮时 , 弹出提示框 , 询问是否退出

        param : event
        return : None
        """
        if QMessageBox.question(self, 'SRF-退出' , '是否退出 ?' , QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class sfr_var():  # 变量空间
    def __init__(self) -> None:
        self.PATH : str = os.getcwd()  # 当前路径
        self.SRF_INFO : dict = {}  # 软件信息
        self.SRF_REGEDIT_INFO : dict = {}  # 注册表信息

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


