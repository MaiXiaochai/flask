# Flask
+ `pipenv`使用

    + **创建虚拟环境**

        `pipenv --python 3.8`

    + **安装`Python`库，标记为开发环境**
       `pipenv install pylibs --dev`

    + **开发完成后**

        + 生成依赖(生成或者更新`pipfile.lock`)  
        `pipenv lock`
        + 在另一个开发环境部署
            + `pipenv install --dev`
            + 这时候会安装`pipfile`文件`[dev-packages]`区域下的包
        + 在生产环境部署
            + `pipenv install --ignore-pipfile`
            + 这时候会从`pipfile.lock`安装依赖包

    + 生成 `requirements.txt`  
        `pipenv lock -r [--dev] > requirements.txt`

+ `Pypi`阿里镜像
    + `https://mirrors.aliyun.com/pypi/simple/`