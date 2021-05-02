# -*- coding: utf-8 -*- 
from distutils.core import setup, Extension
 
#生成一个扩展模块
pht_module = Extension('_Tool', #模块名称，必须要有下划线
                    sources=['Tool_wrap.cxx', #封装后的接口cxx文件
                            'Tool.cpp' #以下为原始代码所依赖的文件
                            ],
                        )
 
setup(name = 'Tool',    #打包后的名称
        version = '0.1',
        author = 'SWIG Docs',
        description = 'Simple swig pht from docs',
        ext_modules = [pht_module], #与上面的扩展模块名称一致
        py_modules = ['Tool'], #需要打包的模块列表
    )