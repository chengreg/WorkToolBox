#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""**************************************************************************
*  Copyright @ 颐希科技 2023. All rights reserved.                            *
*                                                                            *
*                                                                            *
*                                                                            *
*  @file     pngToIcns.py                                                    *
*  @brief                                                                    *
*                                                                            *
*  @author   陈钢强                                                           *
*  @version  1.0.0.1(版本号)                                                  *
*  @date     2023/9/1 10:56                                                 *
*                                                                            *
*----------------------------------------------------------------------------*
*  Change History :                                                          *
*  <Date>     | <Version> | <Author>       | <Description>                   *
*----------------------------------------------------------------------------*
*  2023/9/1   | 1.0.0.1   | 陈钢强           | Create file                   *
*----------------------------------------------------------------------------*
*                                                                            *
***************************************************************************"""

import os
import subprocess


def png_to_icns(png_path):
    # 获取文件名和目录
    base_dir = os.path.dirname(png_path)
    base_name = os.path.splitext(os.path.basename(png_path))[0]
    iconset_path = os.path.join(base_dir, f"{base_name}.iconset")

    # 创建.iconset文件夹
    if not os.path.exists(iconset_path):
        os.makedirs(iconset_path)

    # 定义需要的尺寸和对应的文件名
    sizes = {
        "16x16": "icon_16x16.png",
        "32x32": "icon_16x16@2x.png",
        "32x32": "icon_32x32.png",
        "64x64": "icon_32x32@2x.png",
        "128x128": "icon_128x128.png",
        "256x256": "icon_128x128@2x.png",
        "256x256": "icon_256x256.png",
        "512x512": "icon_256x256@2x.png",
        "512x512": "icon_512x512.png",
        "1024x1024": "icon_512x512@2x.png"
    }

    # 使用sips工具调整图像尺寸
    for size, filename in sizes.items():
        output_path = os.path.join(iconset_path, filename)
        subprocess.run(["sips", "-z", size, png_path, "--out", output_path])

    # 使用iconutil工具生成.icns文件
    subprocess.run(["iconutil", "-c", "icns", iconset_path])

    # 如果需要，可以删除.iconset文件夹
    # subprocess.run(["rm", "-r", iconset_path])

    print(f"{base_name}.icns has been generated!")


if __name__ == '__main__':
    png_to_icns("/Users/chengangqiang/Downloads/test_icons/icon_1024x1024.png")
