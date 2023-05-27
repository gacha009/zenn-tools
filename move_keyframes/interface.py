# -*- coding: utf-8 -*-
__auther__  = 'name'
__version__ = '1.0.0'
__data__    = '2023/03/19'
# ==========================================================
import maya.cmds as cmds
import os
import sys
import ui_utility
import functions
reload(ui_utility)
reload(functions)
sys.dont_write_bytecode = True
# ==========================================================
# ui convert
BASEFOLDER = os.path.dirname(__file__)
UI_NAME = 'mainwindow.ui'
UI_PATH = os.path.join(BASEFOLDER, UI_NAME)
ui_utility.close_qt_window(UI_NAME)

FORM_CLASS, BASE_CLASS = ui_utility.ui_compiler(UI_PATH)

class MainWindow(FORM_CLASS, BASE_CLASS):

    def __init__(self, parent=None):

        # check if the UI is loaded within Maya.
        parent = ui_utility.get_maya_window()

        # initialise base class.(loads the ui elements into self)
        super(FORM_CLASS, self).__init__(parent)
        self.setupUi(self)

        # builtin UI functions
        self.setObjectName(UI_NAME)
        self.setWindowTitle(UI_NAME)
        
        self._connect_widgets()
        self.show()
    
    def _connect_widgets(self):
        self.pushButton.clicked.connect(self.move_allkeys)
    

    def move_allkeys(self):
        move_frame = self.lineEdit.text()
        functions.main(int(move_frame))
        

