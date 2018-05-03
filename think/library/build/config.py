build = {
    'apps':[
        {

            # 生成应用公共文件
            'file' : ['__init__.py'],
            # 'dir'  : ['controller', 'model'],
            # 定义demo模块的自动生成 （按照实际定义的文件名生成）
            'admin'     : {
                'file'   : ['decorator.py','hooks.py','__init__.py'],
                'dir'    : [ 'controller', 'model','form'],
                'form'   : ['user', 'test'],
                'controller' : ['user', 'test'],
                'model'       : ['user', 'test'],
                'templates'   : ['user/index','test/index'],
                'static'      :  ['css/test.css','js/test.js']
            },
            'home'     : {
                'file'   : ['decorator.py','hooks.py','__init__.py'],
                'dir'    : [ 'controller', 'model','form'],
                'form'   : ['user', 'test'],
                'controller' : ['user', 'test'],
                'model'       : ['user', 'test'],
                'templates'   : ['user/index','test/index'],
                'static'      :  ['css/test.css','js/test.js','js/user.js']
            }
        }
    ]
}