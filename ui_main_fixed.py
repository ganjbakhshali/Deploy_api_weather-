# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 537)
        MainWindow.setStyleSheet(u"background-color:rgb(245, 250, 254)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(31, 149, 239)\n"
"}\n"
"QPushButton{\n"
"	color : white;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #F5FAFE;\n"
"    color: #1F95EF;\n"
"    font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.icon_only_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/icons/images/profile_pic2.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.btn_dash_1 = QPushButton(self.icon_only_widget)
        self.btn_dash_1.setObjectName(u"btn_dash_1")
        icon = QIcon()
        icon.addFile(u":/icons/images/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/images/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dash_1.setIcon(icon)
        self.btn_dash_1.setCheckable(True)
        self.btn_dash_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_dash_1)

        self.btn_prof_1 = QPushButton(self.icon_only_widget)
        self.btn_prof_1.setObjectName(u"btn_prof_1")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/images/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_prof_1.setIcon(icon1)
        self.btn_prof_1.setCheckable(True)
        self.btn_prof_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_prof_1)

        self.btn_mess_1 = QPushButton(self.icon_only_widget)
        self.btn_mess_1.setObjectName(u"btn_mess_1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/images/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_mess_1.setIcon(icon2)
        self.btn_mess_1.setCheckable(True)
        self.btn_mess_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_mess_1)

        self.btn_notif_1 = QPushButton(self.icon_only_widget)
        self.btn_notif_1.setObjectName(u"btn_notif_1")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/images/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_notif_1.setIcon(icon3)
        self.btn_notif_1.setCheckable(True)
        self.btn_notif_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_notif_1)

        self.btn_sett_1 = QPushButton(self.icon_only_widget)
        self.btn_sett_1.setObjectName(u"btn_sett_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_sett_1.setIcon(icon4)
        self.btn_sett_1.setCheckable(True)
        self.btn_sett_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_sett_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 176, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(31, 149, 239);\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	color : white;\n"
"	text-align: left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #F5FAFE;\n"
"    color: #1F95EF;\n"
"    font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/images/profile_pic2.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.btn_dash_2 = QPushButton(self.icon_name_widget)
        self.btn_dash_2.setObjectName(u"btn_dash_2")
        self.btn_dash_2.setIcon(icon)
        self.btn_dash_2.setCheckable(True)
        self.btn_dash_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_dash_2)

        self.btn_prof_2 = QPushButton(self.icon_name_widget)
        self.btn_prof_2.setObjectName(u"btn_prof_2")
        self.btn_prof_2.setIcon(icon1)
        self.btn_prof_2.setCheckable(True)
        self.btn_prof_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_prof_2)

        self.btn_mess_2 = QPushButton(self.icon_name_widget)
        self.btn_mess_2.setObjectName(u"btn_mess_2")
        self.btn_mess_2.setIcon(icon2)
        self.btn_mess_2.setCheckable(True)
        self.btn_mess_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_mess_2)

        self.btn_notif_2 = QPushButton(self.icon_name_widget)
        self.btn_notif_2.setObjectName(u"btn_notif_2")
        self.btn_notif_2.setIcon(icon3)
        self.btn_notif_2.setCheckable(True)
        self.btn_notif_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_notif_2)

        self.btn_sett_2 = QPushButton(self.icon_name_widget)
        self.btn_sett_2.setObjectName(u"btn_sett_2")
        self.btn_sett_2.setIcon(icon4)
        self.btn_sett_2.setCheckable(True)
        self.btn_sett_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_sett_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 176, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.icon_name_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.gridLayout_2 = QGridLayout(self.main_menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.heder_widget = QWidget(self.main_menu)
        self.heder_widget.setObjectName(u"heder_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.heder_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_menu = QPushButton(self.heder_widget)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"border:none")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon6)
        self.btn_menu.setIconSize(QSize(20, 20))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_menu)

        self.horizontalSpacer_2 = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.heder_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_search = QPushButton(self.heder_widget)
        self.btn_search.setObjectName(u"btn_search")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon7)
        self.btn_search.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_search)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.heder_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.gridLayout_2.addWidget(self.heder_widget, 0, 0, 1, 2)

        self.label_4 = QLabel(self.main_menu)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.main_menu)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)

        self.page_today = QStackedWidget(self.main_menu)
        self.page_today.setObjectName(u"page_today")
        self.page_today.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"QPushButton{\n"
"\n"
"	border:none;\n"
"\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 71, 16))
        self.lbl_today_temp = QLabel(self.page)
        self.lbl_today_temp.setObjectName(u"lbl_today_temp")
        self.lbl_today_temp.setGeometry(QRect(130, 30, 49, 16))
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 70, 71, 16))
        self.lbl_today_wind = QLabel(self.page)
        self.lbl_today_wind.setObjectName(u"lbl_today_wind")
        self.lbl_today_wind.setGeometry(QRect(130, 70, 49, 16))
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 110, 61, 16))
        self.lbl_description = QLabel(self.page)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setGeometry(QRect(130, 110, 49, 16))
        self.condition_img = QLabel(self.page)
        self.condition_img.setObjectName(u"condition_img")
        self.condition_img.setGeometry(QRect(60, 150, 181, 141))
        self.pushButton_16 = QPushButton(self.page)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(10, 30, 31, 24))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/temp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon9)
        self.pushButton_17 = QPushButton(self.page)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(10, 70, 31, 24))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/wind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon10)
        self.pushButton_18 = QPushButton(self.page)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(10, 110, 31, 24))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/condition.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon11)
        self.page_today.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_today.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.page_today, 2, 0, 1, 1)

        self.page_tomorrow = QStackedWidget(self.main_menu)
        self.page_tomorrow.setObjectName(u"page_tomorrow")
        self.page_tomorrow.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"\n"
"QPushButton{\n"
"\n"
"	border:none;\n"
"\n"
"\n"
"}")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lbl_tomorrow_temp = QLabel(self.page_3)
        self.lbl_tomorrow_temp.setObjectName(u"lbl_tomorrow_temp")
        self.lbl_tomorrow_temp.setGeometry(QRect(150, 30, 49, 16))
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 30, 81, 16))
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 70, 71, 16))
        self.lbl_tomorrow_wind = QLabel(self.page_3)
        self.lbl_tomorrow_wind.setObjectName(u"lbl_tomorrow_wind")
        self.lbl_tomorrow_wind.setGeometry(QRect(150, 70, 49, 16))
        self.pushButton_20 = QPushButton(self.page_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(10, 70, 31, 24))
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        self.pushButton_20.setIcon(icon10)
        self.pushButton_19 = QPushButton(self.page_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(10, 30, 31, 24))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        self.pushButton_19.setIcon(icon9)
        self.page_tomorrow.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_tomorrow.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.page_tomorrow, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_menu.toggled.connect(self.icon_only_widget.setHidden)
        self.btn_menu.toggled.connect(self.icon_name_widget.setVisible)
        self.btn_sett_1.toggled.connect(self.btn_sett_2.setChecked)
        self.btn_notif_1.toggled.connect(self.btn_notif_2.setChecked)
        self.btn_mess_1.toggled.connect(self.btn_mess_2.setChecked)
        self.btn_prof_1.toggled.connect(self.btn_prof_2.setChecked)
        self.btn_dash_1.toggled.connect(self.btn_dash_2.setChecked)
        self.btn_dash_2.toggled.connect(self.btn_dash_1.setChecked)
        self.btn_prof_2.toggled.connect(self.btn_prof_1.setChecked)
        self.btn_mess_2.toggled.connect(self.btn_mess_1.setChecked)
        self.btn_notif_2.toggled.connect(self.btn_notif_1.setChecked)
        self.btn_sett_2.toggled.connect(self.btn_sett_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.btn_dash_1.setText("")
        self.btn_prof_1.setText("")
        self.btn_mess_1.setText("")
        self.btn_notif_1.setText("")
        self.btn_sett_1.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.btn_dash_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_prof_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.btn_mess_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.btn_notif_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.btn_sett_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.btn_menu.setText("")
        self.btn_search.setText("")
        self.pushButton_15.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tomorrow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.lbl_today_temp.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Wind Speed:", None))
        self.lbl_today_wind.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Condition:", None))
        self.lbl_description.setText("")
        self.condition_img.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.lbl_tomorrow_temp.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Wind Speed:", None))
        self.lbl_tomorrow_wind.setText("")
        self.pushButton_20.setText("")
        self.pushButton_19.setText("")
    # retranslateUi

