# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1588, 1047)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.parameters_tab = QtWidgets.QWidget()
        self.parameters_tab.setObjectName("parameters_tab")
        self.picoharp_box = QtWidgets.QGroupBox(self.parameters_tab)
        self.picoharp_box.setGeometry(QtCore.QRect(10, 70, 321, 401))
        self.picoharp_box.setObjectName("picoharp_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.picoharp_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 130, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ch0_level = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_ch0_level.setObjectName("label_ch0_level")
        self.verticalLayout_3.addWidget(self.label_ch0_level)
        self.ch0_level = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ch0_level.setObjectName("ch0_level")
        self.verticalLayout_3.addWidget(self.ch0_level)
        self.label_ch1_level = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_ch1_level.setObjectName("label_ch1_level")
        self.verticalLayout_3.addWidget(self.label_ch1_level)
        self.ch1_level = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ch1_level.setObjectName("ch1_level")
        self.verticalLayout_3.addWidget(self.ch1_level)
        self.label_ch0_zerox = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_ch0_zerox.setObjectName("label_ch0_zerox")
        self.verticalLayout_3.addWidget(self.label_ch0_zerox)
        self.ch0_zerox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ch0_zerox.setObjectName("ch0_zerox")
        self.verticalLayout_3.addWidget(self.ch0_zerox)
        self.label_ch1_zerox = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_ch1_zerox.setObjectName("label_ch1_zerox")
        self.verticalLayout_3.addWidget(self.label_ch1_zerox)
        self.ch1_zerox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.ch1_zerox.setObjectName("ch1_zerox")
        self.verticalLayout_3.addWidget(self.ch1_zerox)
        self.label_syncdiv = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_syncdiv.setObjectName("label_syncdiv")
        self.verticalLayout_3.addWidget(self.label_syncdiv)
        self.syncdiv = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.syncdiv.setObjectName("syncdiv")
        self.verticalLayout_3.addWidget(self.syncdiv)
        self.label_binning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_binning.setObjectName("label_binning")
        self.verticalLayout_3.addWidget(self.label_binning)
        self.binning = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.binning.setObjectName("binning")
        self.verticalLayout_3.addWidget(self.binning)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.picoharp_box)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 20, 156, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_dll_version = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_dll_version.setObjectName("label_dll_version")
        self.verticalLayout_4.addWidget(self.label_dll_version)
        self.dll_version = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dll_version.setReadOnly(True)
        self.dll_version.setObjectName("dll_version")
        self.verticalLayout_4.addWidget(self.dll_version)
        self.label_initialization_status = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_initialization_status.setObjectName("label_initialization_status")
        self.verticalLayout_4.addWidget(self.label_initialization_status)
        self.initialization_status = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.initialization_status.setReadOnly(True)
        self.initialization_status.setObjectName("initialization_status")
        self.verticalLayout_4.addWidget(self.initialization_status)
        self.label_calibration = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_calibration.setObjectName("label_calibration")
        self.verticalLayout_4.addWidget(self.label_calibration)
        self.calibration = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.calibration.setReadOnly(True)
        self.calibration.setObjectName("calibration")
        self.verticalLayout_4.addWidget(self.calibration)
        self.label_device_index = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_device_index.setObjectName("label_device_index")
        self.verticalLayout_4.addWidget(self.label_device_index)
        self.device_index = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.device_index.setAutoFillBackground(False)
        self.device_index.setReadOnly(False)
        self.device_index.setObjectName("device_index")
        self.verticalLayout_4.addWidget(self.device_index)
        self.stop_on_overflow = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.stop_on_overflow.setObjectName("stop_on_overflow")
        self.verticalLayout_4.addWidget(self.stop_on_overflow)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.parameters_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 291, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_data_folder = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_data_folder.setObjectName("label_data_folder")
        self.verticalLayout_6.addWidget(self.label_data_folder)
        self.data_folder = QtWidgets.QWidget(self.verticalLayoutWidget_4)
        self.data_folder.setObjectName("data_folder")
        self.verticalLayout_6.addWidget(self.data_folder)
        self.settings_box = QtWidgets.QGroupBox(self.parameters_tab)
        self.settings_box.setGeometry(QtCore.QRect(350, 70, 321, 401))
        self.settings_box.setObjectName("settings_box")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.settings_box)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 291, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_xy_resolution = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_xy_resolution.setObjectName("label_xy_resolution")
        self.verticalLayout_5.addWidget(self.label_xy_resolution)
        self.xy_resolution = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.xy_resolution.setObjectName("xy_resolution")
        self.verticalLayout_5.addWidget(self.xy_resolution)
        self.label_z_resolution = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_z_resolution.setObjectName("label_z_resolution")
        self.verticalLayout_5.addWidget(self.label_z_resolution)
        self.z_resolution = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.z_resolution.setObjectName("z_resolution")
        self.verticalLayout_5.addWidget(self.z_resolution)
        self.label_time_measurement = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_time_measurement.setObjectName("label_time_measurement")
        self.verticalLayout_5.addWidget(self.label_time_measurement)
        self.time_measurement = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.time_measurement.setObjectName("time_measurement")
        self.verticalLayout_5.addWidget(self.time_measurement)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_scan_countrate_rep_numb = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_scan_countrate_rep_numb.setObjectName("label_scan_countrate_rep_numb")
        self.horizontalLayout_2.addWidget(self.label_scan_countrate_rep_numb)
        self.label_scan_histogram_rep_numb = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_scan_histogram_rep_numb.setObjectName("label_scan_histogram_rep_numb")
        self.horizontalLayout_2.addWidget(self.label_scan_histogram_rep_numb)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scan_countrate_rep_numb = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.scan_countrate_rep_numb.setObjectName("scan_countrate_rep_numb")
        self.horizontalLayout_3.addWidget(self.scan_countrate_rep_numb)
        self.scan_histogram_rep_numb = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.scan_histogram_rep_numb.setObjectName("scan_histogram_rep_numb")
        self.horizontalLayout_3.addWidget(self.scan_histogram_rep_numb)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.label_histogram_aqc_time = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_histogram_aqc_time.setObjectName("label_histogram_aqc_time")
        self.verticalLayout_5.addWidget(self.label_histogram_aqc_time)
        self.histogram_aqc_time = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.histogram_aqc_time.setObjectName("histogram_aqc_time")
        self.verticalLayout_5.addWidget(self.histogram_aqc_time)
        self.label_map_point_aqc_time = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_map_point_aqc_time.setObjectName("label_map_point_aqc_time")
        self.verticalLayout_5.addWidget(self.label_map_point_aqc_time)
        self.map_point_aqc_time = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.map_point_aqc_time.setObjectName("map_point_aqc_time")
        self.verticalLayout_5.addWidget(self.map_point_aqc_time)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.parameters_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(690, 90, 211, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.precise_scan = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.precise_scan.setObjectName("precise_scan")
        self.verticalLayout.addWidget(self.precise_scan)
        self.scan_histogram = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.scan_histogram.setObjectName("scan_histogram")
        self.verticalLayout.addWidget(self.scan_histogram)
        self.save_fit_only = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.save_fit_only.setObjectName("save_fit_only")
        self.verticalLayout.addWidget(self.save_fit_only)
        self.tabWidget.addTab(self.parameters_tab, "")
        self.maps_tab = QtWidgets.QWidget()
        self.maps_tab.setObjectName("maps_tab")
        self.xy_box = QtWidgets.QGroupBox(self.maps_tab)
        self.xy_box.setGeometry(QtCore.QRect(10, 50, 601, 411))
        self.xy_box.setTitle("")
        self.xy_box.setObjectName("xy_box")
        self.xy_wtf = QtWidgets.QPushButton(self.xy_box)
        self.xy_wtf.setGeometry(QtCore.QRect(110, 120, 41, 41))
        self.xy_wtf.setObjectName("xy_wtf")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.xy_box)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 95, 135))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.xy_hand = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.xy_hand.setObjectName("xy_hand")
        self.verticalLayout_10.addWidget(self.xy_hand)
        self.xy_zoom = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.xy_zoom.setObjectName("xy_zoom")
        self.verticalLayout_10.addWidget(self.xy_zoom)
        self.xy_location = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.xy_location.setObjectName("xy_location")
        self.verticalLayout_10.addWidget(self.xy_location)
        self.xy_center = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.xy_center.setObjectName("xy_center")
        self.verticalLayout_10.addWidget(self.xy_center)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.xy_box)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 210, 141, 152))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.xy_scan = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.xy_scan.setObjectName("xy_scan")
        self.verticalLayout_11.addWidget(self.xy_scan)
        self.xy_save = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.xy_save.setObjectName("xy_save")
        self.verticalLayout_11.addWidget(self.xy_save)
        self.xy_load = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.xy_load.setObjectName("xy_load")
        self.verticalLayout_11.addWidget(self.xy_load)
        self.label_xy_layer = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_xy_layer.setObjectName("label_xy_layer")
        self.verticalLayout_11.addWidget(self.label_xy_layer)
        self.xy_layer = QtWidgets.QSpinBox(self.verticalLayoutWidget_10)
        self.xy_layer.setObjectName("xy_layer")
        self.verticalLayout_11.addWidget(self.xy_layer)
        self.xy_coordinates = QtWidgets.QTextBrowser(self.xy_box)
        self.xy_coordinates.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.xy_coordinates.setObjectName("xy_coordinates")
        self.xy_map = QtWidgets.QGroupBox(self.xy_box)
        self.xy_map.setGeometry(QtCore.QRect(160, 10, 431, 391))
        self.xy_map.setObjectName("xy_map")
        self.xy_plot = QtWidgets.QWidget(self.xy_map)
        self.xy_plot.setGeometry(QtCore.QRect(10, 20, 411, 361))
        self.xy_plot.setObjectName("xy_plot")
        self.wavefrom_box = QtWidgets.QGroupBox(self.maps_tab)
        self.wavefrom_box.setGeometry(QtCore.QRect(620, 470, 601, 411))
        self.wavefrom_box.setTitle("")
        self.wavefrom_box.setObjectName("wavefrom_box")
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.wavefrom_box)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(10, 200, 141, 135))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.wg_current = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.wg_current.setObjectName("wg_current")
        self.verticalLayout_17.addWidget(self.wg_current)
        self.wg_collect = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.wg_collect.setObjectName("wg_collect")
        self.verticalLayout_17.addWidget(self.wg_collect)
        self.wg_clear = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.wg_clear.setObjectName("wg_clear")
        self.verticalLayout_17.addWidget(self.wg_clear)
        self.wg_save = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.wg_save.setObjectName("wg_save")
        self.verticalLayout_17.addWidget(self.wg_save)
        self.verticalLayoutWidget_22 = QtWidgets.QWidget(self.wavefrom_box)
        self.verticalLayoutWidget_22.setGeometry(QtCore.QRect(10, 10, 95, 135))
        self.verticalLayoutWidget_22.setObjectName("verticalLayoutWidget_22")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_22)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.wg_hand = QtWidgets.QPushButton(self.verticalLayoutWidget_22)
        self.wg_hand.setObjectName("wg_hand")
        self.verticalLayout_24.addWidget(self.wg_hand)
        self.wg_zoom = QtWidgets.QPushButton(self.verticalLayoutWidget_22)
        self.wg_zoom.setObjectName("wg_zoom")
        self.verticalLayout_24.addWidget(self.wg_zoom)
        self.wg_location = QtWidgets.QPushButton(self.verticalLayoutWidget_22)
        self.wg_location.setObjectName("wg_location")
        self.verticalLayout_24.addWidget(self.wg_location)
        self.wg_center = QtWidgets.QPushButton(self.verticalLayoutWidget_22)
        self.wg_center.setObjectName("wg_center")
        self.verticalLayout_24.addWidget(self.wg_center)
        self.wg_coordinates = QtWidgets.QTextBrowser(self.wavefrom_box)
        self.wg_coordinates.setGeometry(QtCore.QRect(10, 160, 141, 31))
        self.wg_coordinates.setObjectName("wg_coordinates")
        self.wg_wtf = QtWidgets.QPushButton(self.wavefrom_box)
        self.wg_wtf.setGeometry(QtCore.QRect(110, 110, 41, 41))
        self.wg_wtf.setObjectName("wg_wtf")
        self.wg_graph_box = QtWidgets.QGroupBox(self.wavefrom_box)
        self.wg_graph_box.setGeometry(QtCore.QRect(160, 10, 431, 391))
        self.wg_graph_box.setObjectName("wg_graph_box")
        self.wg_plot = QtWidgets.QWidget(self.wg_graph_box)
        self.wg_plot.setGeometry(QtCore.QRect(10, 20, 411, 361))
        self.wg_plot.setObjectName("wg_plot")
        self.xz_box = QtWidgets.QGroupBox(self.maps_tab)
        self.xz_box.setGeometry(QtCore.QRect(10, 470, 601, 411))
        self.xz_box.setTitle("")
        self.xz_box.setObjectName("xz_box")
        self.xz_wtf = QtWidgets.QPushButton(self.xz_box)
        self.xz_wtf.setGeometry(QtCore.QRect(110, 120, 41, 41))
        self.xz_wtf.setObjectName("xz_wtf")
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.xz_box)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(10, 20, 95, 135))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.xz_hand = QtWidgets.QPushButton(self.verticalLayoutWidget_17)
        self.xz_hand.setObjectName("xz_hand")
        self.verticalLayout_19.addWidget(self.xz_hand)
        self.xz_zoom = QtWidgets.QPushButton(self.verticalLayoutWidget_17)
        self.xz_zoom.setObjectName("xz_zoom")
        self.verticalLayout_19.addWidget(self.xz_zoom)
        self.xz_location = QtWidgets.QPushButton(self.verticalLayoutWidget_17)
        self.xz_location.setObjectName("xz_location")
        self.verticalLayout_19.addWidget(self.xz_location)
        self.xz_center = QtWidgets.QPushButton(self.verticalLayoutWidget_17)
        self.xz_center.setObjectName("xz_center")
        self.verticalLayout_19.addWidget(self.xz_center)
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(self.xz_box)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(10, 210, 141, 152))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.xz_scan = QtWidgets.QPushButton(self.verticalLayoutWidget_18)
        self.xz_scan.setObjectName("xz_scan")
        self.verticalLayout_20.addWidget(self.xz_scan)
        self.xz_save = QtWidgets.QPushButton(self.verticalLayoutWidget_18)
        self.xz_save.setObjectName("xz_save")
        self.verticalLayout_20.addWidget(self.xz_save)
        self.xz_load = QtWidgets.QPushButton(self.verticalLayoutWidget_18)
        self.xz_load.setObjectName("xz_load")
        self.verticalLayout_20.addWidget(self.xz_load)
        self.label_xz_layer = QtWidgets.QLabel(self.verticalLayoutWidget_18)
        self.label_xz_layer.setObjectName("label_xz_layer")
        self.verticalLayout_20.addWidget(self.label_xz_layer)
        self.xz_layer = QtWidgets.QSpinBox(self.verticalLayoutWidget_18)
        self.xz_layer.setObjectName("xz_layer")
        self.verticalLayout_20.addWidget(self.xz_layer)
        self.xz_coordinates = QtWidgets.QTextBrowser(self.xz_box)
        self.xz_coordinates.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.xz_coordinates.setObjectName("xz_coordinates")
        self.xz_map = QtWidgets.QGroupBox(self.xz_box)
        self.xz_map.setGeometry(QtCore.QRect(160, 10, 431, 391))
        self.xz_map.setObjectName("xz_map")
        self.xz_plot = QtWidgets.QWidget(self.xz_map)
        self.xz_plot.setGeometry(QtCore.QRect(10, 20, 411, 361))
        self.xz_plot.setObjectName("xz_plot")
        self.yz_box = QtWidgets.QGroupBox(self.maps_tab)
        self.yz_box.setGeometry(QtCore.QRect(620, 50, 601, 411))
        self.yz_box.setTitle("")
        self.yz_box.setObjectName("yz_box")
        self.yz_wtf = QtWidgets.QPushButton(self.yz_box)
        self.yz_wtf.setGeometry(QtCore.QRect(110, 120, 41, 41))
        self.yz_wtf.setObjectName("yz_wtf")
        self.verticalLayoutWidget_19 = QtWidgets.QWidget(self.yz_box)
        self.verticalLayoutWidget_19.setGeometry(QtCore.QRect(10, 20, 95, 135))
        self.verticalLayoutWidget_19.setObjectName("verticalLayoutWidget_19")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_19)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.yz_hand = QtWidgets.QPushButton(self.verticalLayoutWidget_19)
        self.yz_hand.setObjectName("yz_hand")
        self.verticalLayout_21.addWidget(self.yz_hand)
        self.yz_zoom = QtWidgets.QPushButton(self.verticalLayoutWidget_19)
        self.yz_zoom.setObjectName("yz_zoom")
        self.verticalLayout_21.addWidget(self.yz_zoom)
        self.yz_location = QtWidgets.QPushButton(self.verticalLayoutWidget_19)
        self.yz_location.setObjectName("yz_location")
        self.verticalLayout_21.addWidget(self.yz_location)
        self.yz_center = QtWidgets.QPushButton(self.verticalLayoutWidget_19)
        self.yz_center.setObjectName("yz_center")
        self.verticalLayout_21.addWidget(self.yz_center)
        self.verticalLayoutWidget_20 = QtWidgets.QWidget(self.yz_box)
        self.verticalLayoutWidget_20.setGeometry(QtCore.QRect(10, 210, 141, 152))
        self.verticalLayoutWidget_20.setObjectName("verticalLayoutWidget_20")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.yz_scan = QtWidgets.QPushButton(self.verticalLayoutWidget_20)
        self.yz_scan.setObjectName("yz_scan")
        self.verticalLayout_22.addWidget(self.yz_scan)
        self.yz_save = QtWidgets.QPushButton(self.verticalLayoutWidget_20)
        self.yz_save.setObjectName("yz_save")
        self.verticalLayout_22.addWidget(self.yz_save)
        self.yz_load = QtWidgets.QPushButton(self.verticalLayoutWidget_20)
        self.yz_load.setObjectName("yz_load")
        self.verticalLayout_22.addWidget(self.yz_load)
        self.label_yz_layer = QtWidgets.QLabel(self.verticalLayoutWidget_20)
        self.label_yz_layer.setObjectName("label_yz_layer")
        self.verticalLayout_22.addWidget(self.label_yz_layer)
        self.yz_layer = QtWidgets.QSpinBox(self.verticalLayoutWidget_20)
        self.yz_layer.setObjectName("yz_layer")
        self.verticalLayout_22.addWidget(self.yz_layer)
        self.yz_coordinates = QtWidgets.QTextBrowser(self.yz_box)
        self.yz_coordinates.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.yz_coordinates.setObjectName("yz_coordinates")
        self.yz_map = QtWidgets.QGroupBox(self.yz_box)
        self.yz_map.setGeometry(QtCore.QRect(160, 10, 431, 391))
        self.yz_map.setObjectName("yz_map")
        self.yz_plot = QtWidgets.QWidget(self.yz_map)
        self.yz_plot.setGeometry(QtCore.QRect(10, 20, 411, 361))
        self.yz_plot.setObjectName("yz_plot")
        self.parameters_box = QtWidgets.QGroupBox(self.maps_tab)
        self.parameters_box.setGeometry(QtCore.QRect(1230, 470, 281, 411))
        self.parameters_box.setTitle("")
        self.parameters_box.setObjectName("parameters_box")
        self.gridLayoutWidget = QtWidgets.QWidget(self.parameters_box)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_values = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_values.setObjectName("label_values")
        self.gridLayout.addWidget(self.label_values, 2, 1, 1, 1)
        self.values = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.values.setObjectName("values")
        self.gridLayout.addWidget(self.values, 3, 1, 1, 1)
        self.parameters = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.parameters.setObjectName("parameters")
        self.gridLayout.addWidget(self.parameters, 3, 0, 1, 1)
        self.fit_model = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.fit_model.setObjectName("fit_model")
        self.gridLayout.addWidget(self.fit_model, 1, 1, 1, 1)
        self.label_parameters = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_parameters.setObjectName("label_parameters")
        self.gridLayout.addWidget(self.label_parameters, 2, 0, 1, 1)
        self.label_fit_model = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fit_model.setObjectName("label_fit_model")
        self.gridLayout.addWidget(self.label_fit_model, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.maps_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_layer = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_layer.setObjectName("label_layer")
        self.horizontalLayout.addWidget(self.label_layer)
        self.layer = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.layer.setObjectName("layer")
        self.horizontalLayout.addWidget(self.layer)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.maps_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_scan_mode = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_scan_mode.setObjectName("label_scan_mode")
        self.horizontalLayout_5.addWidget(self.label_scan_mode)
        self.scan_mode = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.scan_mode.setObjectName("scan_mode")
        self.horizontalLayout_5.addWidget(self.scan_mode)
        self.tabWidget.addTab(self.maps_tab, "")
        self.time_trace_tab = QtWidgets.QWidget()
        self.time_trace_tab.setObjectName("time_trace_tab")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.time_trace_tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 168, 82))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_countrate_rep_numb = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_countrate_rep_numb.setObjectName("label_countrate_rep_numb")
        self.verticalLayout_8.addWidget(self.label_countrate_rep_numb)
        self.countrate_rep_numb = QtWidgets.QSpinBox(self.verticalLayoutWidget_6)
        self.countrate_rep_numb.setObjectName("countrate_rep_numb")
        self.verticalLayout_8.addWidget(self.countrate_rep_numb)
        self.scan = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.scan.setObjectName("scan")
        self.verticalLayout_8.addWidget(self.scan)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.time_trace_tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(200, 20, 171, 81))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.show_last = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.show_last.setObjectName("show_last")
        self.horizontalLayout_4.addWidget(self.show_last)
        self.numb_sec = QtWidgets.QSpinBox(self.verticalLayoutWidget_7)
        self.numb_sec.setProperty("value", 5)
        self.numb_sec.setObjectName("numb_sec")
        self.horizontalLayout_4.addWidget(self.numb_sec)
        self.seconds = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.seconds.setObjectName("seconds")
        self.horizontalLayout_4.addWidget(self.seconds)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.save_trace = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.save_trace.setObjectName("save_trace")
        self.verticalLayout_9.addWidget(self.save_trace)
        self.plot_box = QtWidgets.QGroupBox(self.time_trace_tab)
        self.plot_box.setGeometry(QtCore.QRect(10, 110, 1541, 771))
        self.plot_box.setObjectName("plot_box")
        self.plot_widget = QtWidgets.QWidget(self.plot_box)
        self.plot_widget.setGeometry(QtCore.QRect(10, 20, 1521, 741))
        self.plot_widget.setObjectName("plot_widget")
        self.tabWidget.addTab(self.time_trace_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1588, 26))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionDark_mode = QtWidgets.QAction(MainWindow)
        self.actionDark_mode.setCheckable(True)
        self.actionDark_mode.setObjectName("actionDark_mode")
        self.menuView.addAction(self.actionDark_mode)
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picoharp_box.setTitle(_translate("MainWindow", "PicoHarp"))
        self.label_ch0_level.setText(_translate("MainWindow", "Ch0 Level"))
        self.label_ch1_level.setText(_translate("MainWindow", "Ch1 Level"))
        self.label_ch0_zerox.setText(_translate("MainWindow", "Ch0 Zerox"))
        self.label_ch1_zerox.setText(_translate("MainWindow", "Ch1 Zerox"))
        self.label_syncdiv.setText(_translate("MainWindow", "Syncdiv"))
        self.label_binning.setText(_translate("MainWindow", "Binning (ps)"))
        self.label_dll_version.setText(_translate("MainWindow", "DLL Version (must be 3.0)"))
        self.label_initialization_status.setText(_translate("MainWindow", "Initialization Status"))
        self.label_calibration.setText(_translate("MainWindow", "Calibration"))
        self.label_device_index.setText(_translate("MainWindow", "Device Index"))
        self.stop_on_overflow.setText(_translate("MainWindow", "Stop On Overflow"))
        self.label_data_folder.setText(_translate("MainWindow", "Data Folder"))
        self.settings_box.setTitle(_translate("MainWindow", "Settings"))
        self.label_xy_resolution.setText(_translate("MainWindow", "XY Resolution (um)"))
        self.label_z_resolution.setText(_translate("MainWindow", "Z Resolution (um)"))
        self.label_time_measurement.setText(_translate("MainWindow", "Time Measurement"))
        self.label_scan_countrate_rep_numb.setText(_translate("MainWindow", "<html><head/><body><p>Scan CountRate<br/>Repetition number</p></body></html>"))
        self.label_scan_histogram_rep_numb.setText(_translate("MainWindow", "<html><head/><body><p>Scan Histogram<br/>Repetition number</p></body></html>"))
        self.label_histogram_aqc_time.setText(_translate("MainWindow", "Histogram Aqcuisition time (ms)"))
        self.label_map_point_aqc_time.setText(_translate("MainWindow", "Map Point Aqcuisition time (ms)"))
        self.precise_scan.setText(_translate("MainWindow", "Precise scan"))
        self.scan_histogram.setText(_translate("MainWindow", "Scan Histogram"))
        self.save_fit_only.setText(_translate("MainWindow", "Save Fit only"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parameters_tab), _translate("MainWindow", "Parameters"))
        self.xy_wtf.setText(_translate("MainWindow", "?"))
        self.xy_hand.setText(_translate("MainWindow", "hand"))
        self.xy_zoom.setText(_translate("MainWindow", "zoom"))
        self.xy_location.setText(_translate("MainWindow", "location"))
        self.xy_center.setText(_translate("MainWindow", "center"))
        self.xy_scan.setText(_translate("MainWindow", "XY Scan"))
        self.xy_save.setText(_translate("MainWindow", "Save XY Map"))
        self.xy_load.setText(_translate("MainWindow", "Load XY Map"))
        self.label_xy_layer.setText(_translate("MainWindow", "Layer XY"))
        self.xy_map.setTitle(_translate("MainWindow", "XY Map"))
        self.wg_current.setText(_translate("MainWindow", "Current"))
        self.wg_collect.setText(_translate("MainWindow", "Collect"))
        self.wg_clear.setText(_translate("MainWindow", "Clear"))
        self.wg_save.setText(_translate("MainWindow", "Save"))
        self.wg_hand.setText(_translate("MainWindow", "hand"))
        self.wg_zoom.setText(_translate("MainWindow", "zoom"))
        self.wg_location.setText(_translate("MainWindow", "location"))
        self.wg_center.setText(_translate("MainWindow", "center"))
        self.wg_wtf.setText(_translate("MainWindow", "?"))
        self.wg_graph_box.setTitle(_translate("MainWindow", "Wavefrom Graph"))
        self.xz_wtf.setText(_translate("MainWindow", "?"))
        self.xz_hand.setText(_translate("MainWindow", "hand"))
        self.xz_zoom.setText(_translate("MainWindow", "zoom"))
        self.xz_location.setText(_translate("MainWindow", "location"))
        self.xz_center.setText(_translate("MainWindow", "center"))
        self.xz_scan.setText(_translate("MainWindow", "XZ Scan"))
        self.xz_save.setText(_translate("MainWindow", "Save XZ Map"))
        self.xz_load.setText(_translate("MainWindow", "Load XZ Map"))
        self.label_xz_layer.setText(_translate("MainWindow", "Layer XZ"))
        self.xz_map.setTitle(_translate("MainWindow", "XZ Map"))
        self.yz_wtf.setText(_translate("MainWindow", "?"))
        self.yz_hand.setText(_translate("MainWindow", "hand"))
        self.yz_zoom.setText(_translate("MainWindow", "zoom"))
        self.yz_location.setText(_translate("MainWindow", "location"))
        self.yz_center.setText(_translate("MainWindow", "center"))
        self.yz_scan.setText(_translate("MainWindow", "YZ Scan"))
        self.yz_save.setText(_translate("MainWindow", "Save YZ Map"))
        self.yz_load.setText(_translate("MainWindow", "Load YZ Map"))
        self.label_yz_layer.setText(_translate("MainWindow", "Layer YZ"))
        self.yz_map.setTitle(_translate("MainWindow", "YZ Map"))
        self.label_values.setText(_translate("MainWindow", "Values and Errors"))
        self.label_parameters.setText(_translate("MainWindow", "Parameters"))
        self.label_fit_model.setText(_translate("MainWindow", "Fit Model"))
        self.label_layer.setText(_translate("MainWindow", "Layer"))
        self.label_scan_mode.setText(_translate("MainWindow", "Scan Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maps_tab), _translate("MainWindow", "Maps"))
        self.label_countrate_rep_numb.setText(_translate("MainWindow", "Countrate Repetition Number"))
        self.scan.setText(_translate("MainWindow", "Scan"))
        self.show_last.setText(_translate("MainWindow", "Show last "))
        self.seconds.setText(_translate("MainWindow", "seconds"))
        self.save_trace.setText(_translate("MainWindow", "Save Trace"))
        self.plot_box.setTitle(_translate("MainWindow", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.time_trace_tab), _translate("MainWindow", "Time Trace"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionDark_mode.setText(_translate("MainWindow", "Dark mode"))