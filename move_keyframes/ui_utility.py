# -*- coding: utf-8 -*-
""" 
UI に関するファンクション
"""

from PySide2 import QtWidgets
from pyside2uic import compileUi
from xml.etree.ElementTree import parse
from StringIO import StringIO


def close_qt_window(ui_name):
    """ ui_nameと同じ名前のwindowを閉じる """

    for widget in QtWidgets.QApplication.topLevelWidgets():

        if ui_name in widget.objectName():
            widget.close()
            widget.deleteLater()


def get_maya_window():
    """ 
    作成したUIが、mayaの後ろ側に行くのを防ぐために
    maya の Windowを取得する
    """
    for widget in QtWidgets.QApplication.allWidgets():
        
        try:
            if widget.objectName() == 'MayaWindow':
                return widget
        except:
            pass

    return None


def ui_compiler(ui_fullpath):
    """
    uiのコンパイル
    
    return:
        form_class
            uiのform class
        base_class
            uiのbase class
    """
    doc = parse(ui_fullpath)
    widget_class_name = doc.find('widget').get('class')
    form_class_name = doc.find('class').text

    with open(ui_fullpath, 'r') as f:
        o = StringIO()              # 空のStringIOオブジェクトを作成
        g = {}
        compileUi(f, o, indent=4)   # .uiファイルをpythonにコンバート
        code = o.getvalue()         # コンバートfileの中身全体を取得
        pyc = compile(code, '<string>', 'exec') # uiをコンパイル

        exec pyc in g               # 値を参照しながら、ファイルを実行(同時に値を格納)
        
        form_class = g['Ui_{}'.format(form_class_name)]
        base_class = getattr(QtWidgets, widget_class_name)
        return form_class, base_class
    return None, None