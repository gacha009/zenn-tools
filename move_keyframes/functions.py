# -*- coding: utf-8 -*-
import maya.cmds as cmds


def main(move_frame):
    """ timeslider上のkeyを指定のフレーム数移動させる """
    start_frame = cmds.playbackOptions(q=True, minTime=True)
    end_frame   = cmds.playbackOptions(q=True, maxTime=True)

    # シーン内のアニメーションカーブをすべて取得
    anim_curves = cmds.ls(type='animCurve') 

    for ac in anim_curves:
        is_ref = cmds.referenceQuery(ac, isNodeReferenced=True)
        
        if is_ref:
            """ animCurveがリファレンスの場合はエラーになるので、対象外にする """
            continue

        cmds.keyframe(
            ac, 
            edit=True, 
            relative=True, 
            option='move', 
            time=(start_frame, end_frame),
            timeChange=move_frame)

    print('success: move all keyframes.')