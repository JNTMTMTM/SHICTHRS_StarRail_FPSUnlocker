# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sfr_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_srf(object):
    def setupUi(self, srf):
        if not srf.objectName():
            srf.setObjectName(u"srf")
        srf.resize(379, 149)
        srf.setMinimumSize(QSize(0, 0))
        srf.setMaximumSize(QSize(10000, 1245124))
        self.tw_main = QTabWidget(srf)
        self.tw_main.setObjectName(u"tw_main")
        self.tw_main.setGeometry(QRect(0, 0, 381, 151))
        self.index_0 = QWidget()
        self.index_0.setObjectName(u"index_0")
        self.pbtn_index_0_unlock_fps = QPushButton(self.index_0)
        self.pbtn_index_0_unlock_fps.setObjectName(u"pbtn_index_0_unlock_fps")
        self.pbtn_index_0_unlock_fps.setEnabled(False)
        self.pbtn_index_0_unlock_fps.setGeometry(QRect(20, 92, 341, 29))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pbtn_index_0_unlock_fps.setFont(font)
        self.lb_index_0_graphics_index = QLabel(self.index_0)
        self.lb_index_0_graphics_index.setObjectName(u"lb_index_0_graphics_index")
        self.lb_index_0_graphics_index.setGeometry(QRect(10, 30, 341, 16))
        self.lb_index_0_regedit_path = QLabel(self.index_0)
        self.lb_index_0_regedit_path.setObjectName(u"lb_index_0_regedit_path")
        self.lb_index_0_regedit_path.setGeometry(QRect(10, 10, 341, 16))
        self.lb_index_0_current_fps = QLabel(self.index_0)
        self.lb_index_0_current_fps.setObjectName(u"lb_index_0_current_fps")
        self.lb_index_0_current_fps.setGeometry(QRect(10, 50, 341, 16))
        self.rb_index_0_unlock_120fps = QRadioButton(self.index_0)
        self.rb_index_0_unlock_120fps.setObjectName(u"rb_index_0_unlock_120fps")
        self.rb_index_0_unlock_120fps.setEnabled(False)
        self.rb_index_0_unlock_120fps.setGeometry(QRect(20, 70, 95, 19))
        self.rb_index_0_rlb_60fps = QRadioButton(self.index_0)
        self.rb_index_0_rlb_60fps.setObjectName(u"rb_index_0_rlb_60fps")
        self.rb_index_0_rlb_60fps.setEnabled(False)
        self.rb_index_0_rlb_60fps.setGeometry(QRect(120, 70, 95, 19))
        self.tw_main.addTab(self.index_0, "")
        self.index_1 = QWidget()
        self.index_1.setObjectName(u"index_1")
        self.lb_index_1_version_info = QLabel(self.index_1)
        self.lb_index_1_version_info.setObjectName(u"lb_index_1_version_info")
        self.lb_index_1_version_info.setGeometry(QRect(10, 10, 341, 16))
        self.lb_index_1_github_link = QLabel(self.index_1)
        self.lb_index_1_github_link.setObjectName(u"lb_index_1_github_link")
        self.lb_index_1_github_link.setGeometry(QRect(10, 30, 341, 16))
        self.pbtn_index_1_start_game = QPushButton(self.index_1)
        self.pbtn_index_1_start_game.setObjectName(u"pbtn_index_1_start_game")
        self.pbtn_index_1_start_game.setGeometry(QRect(20, 50, 341, 23))
        self.pbtn_index_1_restart_system = QPushButton(self.index_1)
        self.pbtn_index_1_restart_system.setObjectName(u"pbtn_index_1_restart_system")
        self.pbtn_index_1_restart_system.setGeometry(QRect(20, 73, 341, 23))
        self.pbtn_index_1_quit = QPushButton(self.index_1)
        self.pbtn_index_1_quit.setObjectName(u"pbtn_index_1_quit")
        self.pbtn_index_1_quit.setGeometry(QRect(20, 96, 341, 23))
        self.tw_main.addTab(self.index_1, "")

        self.retranslateUi(srf)

        self.tw_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(srf)
    # setupUi

    def retranslateUi(self, srf):
        srf.setWindowTitle(QCoreApplication.translate("srf", u"SHICTHRS-SFR", None))
        self.pbtn_index_0_unlock_fps.setText(QCoreApplication.translate("srf", u"\u4e00\u952e\u89e3\u9501", None))
        self.lb_index_0_graphics_index.setText(QCoreApplication.translate("srf", u"\u56fe\u5f62\u8bbe\u7f6e\u5f15\u5bfc : \u7b49\u5f85\u52a0\u8f7d", None))
        self.lb_index_0_regedit_path.setText(QCoreApplication.translate("srf", u"\u6ce8\u518c\u8868\u8def\u5f84 : \u7b49\u5f85\u52a0\u8f7d", None))
        self.lb_index_0_current_fps.setText(QCoreApplication.translate("srf", u"\u5f53\u524d\u5e27\u7387 : \u7b49\u5f85\u52a0\u8f7d", None))
        self.rb_index_0_unlock_120fps.setText(QCoreApplication.translate("srf", u"\u89e3\u9501120\u5e27", None))
        self.rb_index_0_rlb_60fps.setText(QCoreApplication.translate("srf", u"\u56de\u6eda\u81f360\u5e27", None))
        self.tw_main.setTabText(self.tw_main.indexOf(self.index_0), QCoreApplication.translate("srf", u"\u89e3\u9501\u5e27\u7387", None))
        self.lb_index_1_version_info.setText(QCoreApplication.translate("srf", u"\u7248\u672c\u4fe1\u606f : \u7b49\u5f85\u52a0\u8f7d", None))
        self.lb_index_1_github_link.setText(QCoreApplication.translate("srf", u"<html><head/><body><p>\u4ed3\u5e93\u5730\u5740 : \u7b49\u5f85\u52a0\u8f7d</p><p><br/></p></body></html>", None))
        self.pbtn_index_1_start_game.setText(QCoreApplication.translate("srf", u"\u542f\u52a8\u6e38\u620f", None))
        self.pbtn_index_1_restart_system.setText(QCoreApplication.translate("srf", u"\u91cd\u542f\u7cfb\u7edf", None))
        self.pbtn_index_1_quit.setText(QCoreApplication.translate("srf", u"\u5b89\u5168\u9000\u51fa", None))
        self.tw_main.setTabText(self.tw_main.indexOf(self.index_1), QCoreApplication.translate("srf", u"\u5de5\u5177", None))
    # retranslateUi

