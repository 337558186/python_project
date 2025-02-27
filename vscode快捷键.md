koroFileHeader插件
    文件头部注释快捷键  ctrl+win+i
    函数注释注释快捷键  ctrl+win+t


     
    //自动生成注解
    "fileheader.configObj": {
        "createFileTime": true, //设置为true则为文件新建时候作为date，否则注释生成时间为date
        "autoAdd": true, //自动生成注释
        "annotationStr": {
            "head": "/*",
            "middle": " * @",
            "end": " */",
            "use": true //设置自定义注释可用
        }
    },
    //头部注释(ctrl + win + t)
    "fileheader.customMade": {
        "Description": "",
        "Author": "duke0552",
        "version": "",
        "Date": "Do not edit"
    },
    //方法(函数)注释(ctrl + win + i)
    "fileheader.cursorMode": {
        "description": "",
        "param": "", // param 开启函数参数自动提取 需要将光标放在函数行或者函数上方的空白行
        "return": ""
    },
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "editor.fontSize": 15



ctrl+I   coplite快捷键