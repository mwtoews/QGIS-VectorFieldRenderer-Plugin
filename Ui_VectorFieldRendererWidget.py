# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\OSGeo4W\apps\qgis-dev\python\plugins\VectorFieldRenderer\Ui_VectorFieldRendererWidget.ui'
#
# Created: Fri Feb 12 11:12:11 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_VectorFieldRendererWidget(object):
    def setupUi(self, VectorFieldRendererWidget):
        VectorFieldRendererWidget.setObjectName("VectorFieldRendererWidget")
        VectorFieldRendererWidget.resize(510, 396)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VectorFieldRendererWidget.sizePolicy().hasHeightForWidth())
        VectorFieldRendererWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QtGui.QVBoxLayout(VectorFieldRendererWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uHelpLayout = QtGui.QHBoxLayout()
        self.uHelpLayout.setContentsMargins(-1, -1, 0, -1)
        self.uHelpLayout.setObjectName("uHelpLayout")
        self.uVectorFieldTypeGroupBox = QtGui.QGroupBox(VectorFieldRendererWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uVectorFieldTypeGroupBox.sizePolicy().hasHeightForWidth())
        self.uVectorFieldTypeGroupBox.setSizePolicy(sizePolicy)
        self.uVectorFieldTypeGroupBox.setObjectName("uVectorFieldTypeGroupBox")
        self.uFieldTypeLayout = QtGui.QHBoxLayout(self.uVectorFieldTypeGroupBox)
        self.uFieldTypeLayout.setObjectName("uFieldTypeLayout")
        self.uFieldTypeCartesian = QtGui.QRadioButton(self.uVectorFieldTypeGroupBox)
        self.uFieldTypeCartesian.setChecked(True)
        self.uFieldTypeCartesian.setObjectName("uFieldTypeCartesian")
        self.uFieldTypeLayout.addWidget(self.uFieldTypeCartesian)
        self.uFieldTypePolar = QtGui.QRadioButton(self.uVectorFieldTypeGroupBox)
        self.uFieldTypePolar.setObjectName("uFieldTypePolar")
        self.uFieldTypeLayout.addWidget(self.uFieldTypePolar)
        self.uFieldTypeHeight = QtGui.QRadioButton(self.uVectorFieldTypeGroupBox)
        self.uFieldTypeHeight.setObjectName("uFieldTypeHeight")
        self.uFieldTypeLayout.addWidget(self.uFieldTypeHeight)
        self.uHelpLayout.addWidget(self.uVectorFieldTypeGroupBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.uHelpLayout.addItem(spacerItem)
        self.uHelpButton = QtGui.QPushButton(VectorFieldRendererWidget)
        self.uHelpButton.setObjectName("uHelpButton")
        self.uHelpLayout.addWidget(self.uHelpButton)
        self.uHelpLayout.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.uHelpLayout)
        self.uVectorFieldGrid = QtGui.QGridLayout()
        self.uVectorFieldGrid.setObjectName("uVectorFieldGrid")
        self.uXFieldLabel = QtGui.QLabel(VectorFieldRendererWidget)
        self.uXFieldLabel.setObjectName("uXFieldLabel")
        self.uVectorFieldGrid.addWidget(self.uXFieldLabel, 0, 0, 1, 1)
        self.uXField = QtGui.QComboBox(VectorFieldRendererWidget)
        self.uXField.setObjectName("uXField")
        self.uVectorFieldGrid.addWidget(self.uXField, 0, 2, 1, 1)
        self.uYFieldLabel = QtGui.QLabel(VectorFieldRendererWidget)
        self.uYFieldLabel.setObjectName("uYFieldLabel")
        self.uVectorFieldGrid.addWidget(self.uYFieldLabel, 1, 0, 1, 1)
        self.uYField = QtGui.QComboBox(VectorFieldRendererWidget)
        self.uYField.setObjectName("uYField")
        self.uVectorFieldGrid.addWidget(self.uYField, 1, 2, 1, 1)
        self.uArrowScaleLabel = QtGui.QLabel(VectorFieldRendererWidget)
        self.uArrowScaleLabel.setObjectName("uArrowScaleLabel")
        self.uVectorFieldGrid.addWidget(self.uArrowScaleLabel, 2, 0, 1, 1)
        self.uArrowScaleLayout = QtGui.QHBoxLayout()
        self.uArrowScaleLayout.setObjectName("uArrowScaleLayout")
        self.uArrowScale = QtGui.QLineEdit(VectorFieldRendererWidget)
        self.uArrowScale.setObjectName("uArrowScale")
        self.uArrowScaleLayout.addWidget(self.uArrowScale)
        self.uScaleUnits = QtGui.QPushButton(VectorFieldRendererWidget)
        self.uScaleUnits.setMinimumSize(QtCore.QSize(100, 0))
        self.uScaleUnits.setObjectName("uScaleUnits")
        self.uArrowScaleLayout.addWidget(self.uScaleUnits)
        self.uScaleGroupLabel = QtGui.QLabel(VectorFieldRendererWidget)
        self.uScaleGroupLabel.setObjectName("uScaleGroupLabel")
        self.uArrowScaleLayout.addWidget(self.uScaleGroupLabel)
        self.uScaleGroup = QtGui.QLineEdit(VectorFieldRendererWidget)
        self.uScaleGroup.setObjectName("uScaleGroup")
        self.uArrowScaleLayout.addWidget(self.uScaleGroup)
        self.uVectorFieldGrid.addLayout(self.uArrowScaleLayout, 2, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.uVectorFieldGrid)
        self.uAngleFormatLayout = QtGui.QHBoxLayout()
        self.uAngleFormatLayout.setContentsMargins(0, -1, 0, -1)
        self.uAngleFormatLayout.setObjectName("uAngleFormatLayout")
        self.uOrientationGroupBox = QtGui.QGroupBox(VectorFieldRendererWidget)
        self.uOrientationGroupBox.setEnabled(False)
        self.uOrientationGroupBox.setObjectName("uOrientationGroupBox")
        self.uOrientationLayout = QtGui.QHBoxLayout(self.uOrientationGroupBox)
        self.uOrientationLayout.setSpacing(6)
        self.uOrientationLayout.setMargin(9)
        self.uOrientationLayout.setObjectName("uOrientationLayout")
        self.uAngleOrientationEast = QtGui.QRadioButton(self.uOrientationGroupBox)
        self.uAngleOrientationEast.setChecked(True)
        self.uAngleOrientationEast.setObjectName("uAngleOrientationEast")
        self.uOrientationLayout.addWidget(self.uAngleOrientationEast)
        self.uAngleOrientationNorth = QtGui.QRadioButton(self.uOrientationGroupBox)
        self.uAngleOrientationNorth.setObjectName("uAngleOrientationNorth")
        self.uOrientationLayout.addWidget(self.uAngleOrientationNorth)
        self.uAngleFormatLayout.addWidget(self.uOrientationGroupBox)
        self.uAngleUnitsGroupBox = QtGui.QGroupBox(VectorFieldRendererWidget)
        self.uAngleUnitsGroupBox.setEnabled(False)
        self.uAngleUnitsGroupBox.setObjectName("uAngleUnitsGroupBox")
        self.uAngleUnitsLayout = QtGui.QHBoxLayout(self.uAngleUnitsGroupBox)
        self.uAngleUnitsLayout.setContentsMargins(-1, 9, -1, 9)
        self.uAngleUnitsLayout.setObjectName("uAngleUnitsLayout")
        self.uAngleUnitsDegrees = QtGui.QRadioButton(self.uAngleUnitsGroupBox)
        self.uAngleUnitsDegrees.setChecked(True)
        self.uAngleUnitsDegrees.setObjectName("uAngleUnitsDegrees")
        self.uAngleUnitsLayout.addWidget(self.uAngleUnitsDegrees)
        self.uAngleUnitsRadians = QtGui.QRadioButton(self.uAngleUnitsGroupBox)
        self.uAngleUnitsRadians.setEnabled(False)
        self.uAngleUnitsRadians.setObjectName("uAngleUnitsRadians")
        self.uAngleUnitsLayout.addWidget(self.uAngleUnitsRadians)
        self.uAngleFormatLayout.addWidget(self.uAngleUnitsGroupBox)
        self.verticalLayout_4.addLayout(self.uAngleFormatLayout)
        self.uArrowFormatGroup = QtGui.QGroupBox(VectorFieldRendererWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uArrowFormatGroup.sizePolicy().hasHeightForWidth())
        self.uArrowFormatGroup.setSizePolicy(sizePolicy)
        self.uArrowFormatGroup.setObjectName("uArrowFormatGroup")
        self.uArrowFormatLayout = QtGui.QVBoxLayout(self.uArrowFormatGroup)
        self.uArrowFormatLayout.setMargin(0)
        self.uArrowFormatLayout.setObjectName("uArrowFormatLayout")
        self.uArrowUnitsLayout = QtGui.QHBoxLayout()
        self.uArrowUnitsLayout.setObjectName("uArrowUnitsLayout")
        self.uOutputUnitLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uOutputUnitLabel.setObjectName("uOutputUnitLabel")
        self.uArrowUnitsLayout.addWidget(self.uOutputUnitLabel)
        self.uOutputUnits = QtGui.QPushButton(self.uArrowFormatGroup)
        self.uOutputUnits.setMinimumSize(QtCore.QSize(100, 0))
        self.uOutputUnits.setObjectName("uOutputUnits")
        self.uArrowUnitsLayout.addWidget(self.uOutputUnits)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.uArrowUnitsLayout.addItem(spacerItem1)
        self.uArrowFormatLayout.addLayout(self.uArrowUnitsLayout)
        self.uArrowSizeLayout = QtGui.QHBoxLayout()
        self.uArrowSizeLayout.setObjectName("uArrowSizeLayout")
        self.uArrowSizeLayoutLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowSizeLayoutLabel.setObjectName("uArrowSizeLayoutLabel")
        self.uArrowSizeLayout.addWidget(self.uArrowSizeLayoutLabel)
        self.uArrowHeadSizeLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowHeadSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uArrowHeadSizeLabel.setObjectName("uArrowHeadSizeLabel")
        self.uArrowSizeLayout.addWidget(self.uArrowHeadSizeLabel)
        self.uArrowHeadSize = QtGui.QDoubleSpinBox(self.uArrowFormatGroup)
        self.uArrowHeadSize.setSingleStep(0.1)
        self.uArrowHeadSize.setObjectName("uArrowHeadSize")
        self.uArrowSizeLayout.addWidget(self.uArrowHeadSize)
        self.uArrowHeadMaxSizeLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowHeadMaxSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uArrowHeadMaxSizeLabel.setObjectName("uArrowHeadMaxSizeLabel")
        self.uArrowSizeLayout.addWidget(self.uArrowHeadMaxSizeLabel)
        self.uArrowHeadMaxSize = QtGui.QDoubleSpinBox(self.uArrowFormatGroup)
        self.uArrowHeadMaxSize.setObjectName("uArrowHeadMaxSize")
        self.uArrowSizeLayout.addWidget(self.uArrowHeadMaxSize)
        self.uArrowBaseSizeLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowBaseSizeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uArrowBaseSizeLabel.setObjectName("uArrowBaseSizeLabel")
        self.uArrowSizeLayout.addWidget(self.uArrowBaseSizeLabel)
        self.uArrowBaseSize = QtGui.QDoubleSpinBox(self.uArrowFormatGroup)
        self.uArrowBaseSize.setObjectName("uArrowBaseSize")
        self.uArrowSizeLayout.addWidget(self.uArrowBaseSize)
        self.uArrowWidthLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowWidthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.uArrowWidthLabel.setObjectName("uArrowWidthLabel")
        self.uArrowSizeLayout.addWidget(self.uArrowWidthLabel)
        self.uArrowWidth = QtGui.QDoubleSpinBox(self.uArrowFormatGroup)
        self.uArrowWidth.setObjectName("uArrowWidth")
        self.uArrowSizeLayout.addWidget(self.uArrowWidth)
        self.uArrowFormatLayout.addLayout(self.uArrowSizeLayout)
        self.uArrowColorLayout = QtGui.QHBoxLayout()
        self.uArrowColorLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.uArrowColorLayout.setContentsMargins(-1, 0, -1, -1)
        self.uArrowColorLayout.setObjectName("uArrowColorLayout")
        self.uArrowColorLayoutLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uArrowColorLayoutLabel.setObjectName("uArrowColorLayoutLabel")
        self.uArrowColorLayout.addWidget(self.uArrowColorLayoutLabel)
        self.uArrowColorLabel = QtGui.QLabel(self.uArrowFormatGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uArrowColorLabel.sizePolicy().hasHeightForWidth())
        self.uArrowColorLabel.setSizePolicy(sizePolicy)
        self.uArrowColorLabel.setObjectName("uArrowColorLabel")
        self.uArrowColorLayout.addWidget(self.uArrowColorLabel)
        self.uArrowColor = QgsColorButtonV2(self.uArrowFormatGroup)
        self.uArrowColor.setObjectName("uArrowColor")
        self.uArrowColorLayout.addWidget(self.uArrowColor)
        self.uBaseColorLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uBaseColorLabel.setObjectName("uBaseColorLabel")
        self.uArrowColorLayout.addWidget(self.uBaseColorLabel)
        self.uBaseColor = QgsColorButtonV2(self.uArrowFormatGroup)
        self.uBaseColor.setObjectName("uBaseColor")
        self.uArrowColorLayout.addWidget(self.uBaseColor)
        self.uBaseBorderColorLabel = QtGui.QLabel(self.uArrowFormatGroup)
        self.uBaseBorderColorLabel.setObjectName("uBaseBorderColorLabel")
        self.uArrowColorLayout.addWidget(self.uBaseBorderColorLabel)
        self.uBaseBorderColor = QgsColorButtonV2(self.uArrowFormatGroup)
        self.uBaseBorderColor.setObjectName("uBaseBorderColor")
        self.uArrowColorLayout.addWidget(self.uBaseBorderColor)
        self.uArrowColorLayout.setStretch(0, 1)
        self.uArrowColorLayout.setStretch(2, 1)
        self.uArrowColorLayout.setStretch(4, 1)
        self.uArrowColorLayout.setStretch(6, 1)
        self.uArrowFormatLayout.addLayout(self.uArrowColorLayout)
        self.verticalLayout_4.addWidget(self.uArrowFormatGroup)
        self.uLegendGroup = QtGui.QGroupBox(VectorFieldRendererWidget)
        self.uLegendGroup.setObjectName("uLegendGroup")
        self.uLegendLayout = QtGui.QHBoxLayout(self.uLegendGroup)
        self.uLegendLayout.setObjectName("uLegendLayout")
        self.uLegendTextLabel = QtGui.QLabel(self.uLegendGroup)
        self.uLegendTextLabel.setObjectName("uLegendTextLabel")
        self.uLegendLayout.addWidget(self.uLegendTextLabel)
        self.uLegendText = QtGui.QLineEdit(self.uLegendGroup)
        self.uLegendText.setObjectName("uLegendText")
        self.uLegendLayout.addWidget(self.uLegendText)
        self.uScaleBoxTextLabel = QtGui.QLabel(self.uLegendGroup)
        self.uScaleBoxTextLabel.setObjectName("uScaleBoxTextLabel")
        self.uLegendLayout.addWidget(self.uScaleBoxTextLabel)
        self.uScaleBoxText = QtGui.QLineEdit(self.uLegendGroup)
        self.uScaleBoxText.setObjectName("uScaleBoxText")
        self.uLegendLayout.addWidget(self.uScaleBoxText)
        self.uShowScaleBoxLabel = QtGui.QLabel(self.uLegendGroup)
        self.uShowScaleBoxLabel.setObjectName("uShowScaleBoxLabel")
        self.uLegendLayout.addWidget(self.uShowScaleBoxLabel)
        self.uShowInScaleBox = QtGui.QCheckBox(self.uLegendGroup)
        self.uShowInScaleBox.setObjectName("uShowInScaleBox")
        self.uLegendLayout.addWidget(self.uShowInScaleBox)
        self.verticalLayout_4.addWidget(self.uLegendGroup)
        self.uXFieldLabel.setBuddy(self.uXField)
        self.uYFieldLabel.setBuddy(self.uYField)
        self.uArrowScaleLabel.setBuddy(self.uArrowScale)
        self.uScaleGroupLabel.setBuddy(self.uScaleGroup)
        self.uOutputUnitLabel.setBuddy(self.uOutputUnits)
        self.uArrowSizeLayoutLabel.setBuddy(self.uArrowHeadSize)
        self.uArrowHeadSizeLabel.setBuddy(self.uArrowHeadSize)
        self.uArrowHeadMaxSizeLabel.setBuddy(self.uArrowHeadMaxSize)
        self.uArrowBaseSizeLabel.setBuddy(self.uArrowBaseSize)
        self.uArrowWidthLabel.setBuddy(self.uArrowWidth)
        self.uArrowColorLayoutLabel.setBuddy(self.uArrowColor)
        self.uArrowColorLabel.setBuddy(self.uArrowColor)
        self.uBaseColorLabel.setBuddy(self.uBaseColor)
        self.uBaseBorderColorLabel.setBuddy(self.uBaseBorderColor)
        self.uLegendTextLabel.setBuddy(self.uLegendText)
        self.uScaleBoxTextLabel.setBuddy(self.uScaleBoxText)
        self.uShowScaleBoxLabel.setBuddy(self.uShowInScaleBox)

        self.retranslateUi(VectorFieldRendererWidget)
        QtCore.QMetaObject.connectSlotsByName(VectorFieldRendererWidget)
        VectorFieldRendererWidget.setTabOrder(self.uFieldTypeCartesian, self.uFieldTypePolar)
        VectorFieldRendererWidget.setTabOrder(self.uFieldTypePolar, self.uFieldTypeHeight)
        VectorFieldRendererWidget.setTabOrder(self.uFieldTypeHeight, self.uHelpButton)
        VectorFieldRendererWidget.setTabOrder(self.uHelpButton, self.uXField)
        VectorFieldRendererWidget.setTabOrder(self.uXField, self.uYField)
        VectorFieldRendererWidget.setTabOrder(self.uYField, self.uArrowScale)
        VectorFieldRendererWidget.setTabOrder(self.uArrowScale, self.uScaleUnits)
        VectorFieldRendererWidget.setTabOrder(self.uScaleUnits, self.uScaleGroup)
        VectorFieldRendererWidget.setTabOrder(self.uScaleGroup, self.uAngleOrientationEast)
        VectorFieldRendererWidget.setTabOrder(self.uAngleOrientationEast, self.uAngleOrientationNorth)
        VectorFieldRendererWidget.setTabOrder(self.uAngleOrientationNorth, self.uAngleUnitsDegrees)
        VectorFieldRendererWidget.setTabOrder(self.uAngleUnitsDegrees, self.uAngleUnitsRadians)
        VectorFieldRendererWidget.setTabOrder(self.uAngleUnitsRadians, self.uOutputUnits)
        VectorFieldRendererWidget.setTabOrder(self.uOutputUnits, self.uArrowHeadSize)
        VectorFieldRendererWidget.setTabOrder(self.uArrowHeadSize, self.uArrowHeadMaxSize)
        VectorFieldRendererWidget.setTabOrder(self.uArrowHeadMaxSize, self.uArrowBaseSize)
        VectorFieldRendererWidget.setTabOrder(self.uArrowBaseSize, self.uArrowWidth)
        VectorFieldRendererWidget.setTabOrder(self.uArrowWidth, self.uArrowColor)
        VectorFieldRendererWidget.setTabOrder(self.uArrowColor, self.uBaseColor)
        VectorFieldRendererWidget.setTabOrder(self.uBaseColor, self.uBaseBorderColor)
        VectorFieldRendererWidget.setTabOrder(self.uBaseBorderColor, self.uLegendText)
        VectorFieldRendererWidget.setTabOrder(self.uLegendText, self.uScaleBoxText)
        VectorFieldRendererWidget.setTabOrder(self.uScaleBoxText, self.uShowInScaleBox)

    def retranslateUi(self, VectorFieldRendererWidget):
        VectorFieldRendererWidget.setWindowTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.uVectorFieldTypeGroupBox.setTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Vector field type", None, QtGui.QApplication.UnicodeUTF8))
        self.uFieldTypeCartesian.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Cartesian (XY) field", None, QtGui.QApplication.UnicodeUTF8))
        self.uFieldTypePolar.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Polar (length,angle) field", None, QtGui.QApplication.UnicodeUTF8))
        self.uFieldTypeHeight.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Height only", None, QtGui.QApplication.UnicodeUTF8))
        self.uHelpButton.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.uXFieldLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "X attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.uXField.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the X/length field", None, QtGui.QApplication.UnicodeUTF8))
        self.uYFieldLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Y attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.uYField.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the y/angle field", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowScaleLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Scale:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.uScaleUnits.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Millimeter", None, QtGui.QApplication.UnicodeUTF8))
        self.uScaleGroupLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "    Scale group", None, QtGui.QApplication.UnicodeUTF8))
        self.uOrientationGroupBox.setTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Angle orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleOrientationEast.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the angle orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleOrientationEast.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "North from east", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleOrientationNorth.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the angle orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleOrientationNorth.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "East from north", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleUnitsGroupBox.setTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Angle units", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleUnitsDegrees.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the angle units", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleUnitsDegrees.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleUnitsRadians.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Select the angle units", None, QtGui.QApplication.UnicodeUTF8))
        self.uAngleUnitsRadians.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Radians", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowFormatGroup.setTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Arrow format", None, QtGui.QApplication.UnicodeUTF8))
        self.uOutputUnitLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Units:", None, QtGui.QApplication.UnicodeUTF8))
        self.uOutputUnits.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Millimeter", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowSizeLayoutLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowHeadSizeLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Head (relative)", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowHeadSize.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Arrow head size as a multiple of the length", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowHeadMaxSizeLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Head (maximum)", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowHeadMaxSize.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Maximum arrow head size", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowBaseSizeLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowBaseSize.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Size of the arrow base symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowWidthLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowWidth.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Width of the arrow shaft", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowColorLayoutLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Colours:", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowColorLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowColor.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Change the arrow colour", None, QtGui.QApplication.UnicodeUTF8))
        self.uArrowColor.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseColorLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseColor.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Change the base symbol colour", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseColor.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseBorderColorLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Base border", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseBorderColor.setToolTip(QtGui.QApplication.translate("VectorFieldRendererWidget", "Change the base border colour", None, QtGui.QApplication.UnicodeUTF8))
        self.uBaseBorderColor.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "change", None, QtGui.QApplication.UnicodeUTF8))
        self.uLegendGroup.setTitle(QtGui.QApplication.translate("VectorFieldRendererWidget", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.uLegendTextLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Legend text: ", None, QtGui.QApplication.UnicodeUTF8))
        self.uScaleBoxTextLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Scale box text: ", None, QtGui.QApplication.UnicodeUTF8))
        self.uShowScaleBoxLabel.setText(QtGui.QApplication.translate("VectorFieldRendererWidget", "Show?", None, QtGui.QApplication.UnicodeUTF8))

from qgis.gui import QgsColorButtonV2