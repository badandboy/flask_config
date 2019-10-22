# flask_env
flask的多环境配置

遇到的问题：
开始没做多环境配置，比如开发环境，测试环境，生产环境等，把所有的配置都写config.py了，
包括
    数据库配置，
    redis配置，
    OSS配置，
    短信服务的配置等等，
支持数据库的半自动，就是数据库是有多个环境的配置的，但是需要修改代码去指定具体的某一个环境，当从开发环境到生产环境，启动项目时需要手动修改代码指定数据库的环境，而我们绝大部分又使用的版本管理工具，都是svn up 或者git pull的，这个时候再去修改代码显得不智能，需要在不同的环境切来切去，增加了成本，其他配置如OSS，redis，只有一个配置，而redis的配置在开发环境和生产环境的配置也基本是不一样的，无法根据多环境自动加载不同的配置

探索之路：
就去flask的官方网站看了一下，flask的配置支持多种方式，如常用的from_object,还有from_pyfile,from_json,from_envvar,from_mapping等等，就看了一下from_pyfile吧，他能够加载不同的py文件配置，设置系统的环境变量以后，比如window设置为develop，而测试服务器设置为test，生产服务器设置为production，这样我python代码里面通过读取当前环境的环境变量，去加载不同的py文件配置，这样不就OK了么，（window设置环境变量：我的电脑->属性->高级系统设置->环境变量,添加一个就可以了，比如FLASK_APP=develop，window需要重启电脑，python才能读取到正确的配置，linux可以编辑/etc/profile添加一行 export FLASK_APP=production，然后source /etc/profile使他生效），但是这样对于启动flask来说，是实现了多环境配置，但是对于其他的配置，OSS，redis，则不好实现多环境配置，我需要在引用redis的时候，再判断环境，再加载不同的配置，这样也很麻烦，再说我代码已经写完了，这样的话，我又要回去修改我的代码，这不是我想要的
  
 最后方案：
  最后就想了一种方案，既然我所有的配置都是从config.py读取的，那我在config.py上面再包一层，我配置多个.ini，通过os.getenv（“FLASK_APP”）获取环境变量，通过不同的环境变量，再通过configparser，读取不同的.ini配置，最后复制给config.py里面的配置，这样我数据库，OSS，redis都能实现多环境配置了，并且我以后再添加其他的配置的时候，只需要在.ini配置和config.py里面加一下就可以了，不需要手动改启动时的配置了.
