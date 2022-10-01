# 四川大学JW系统验证码 训练集
## 更新
+ 已经基于本仓库内的生成方法生成了10w个数据集训练的深度学习模型，并已经发布到pip（PYPI），在有pytorch的基础上可以通过`pip install scu_captcha`以下载使用。 

    [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=SunnyHaze&repo=scu-captcha)](https://github.com/SunnyHaze/scu-captcha)
+ 10w数据集百度网盘链接：
  + 链接：https://pan.baidu.com/s/1fqOLhP7FSb6oa61NAa4CIQ 
  + 提取码：7gjy
## 简介
+ 本仓库中含有 10000 条四川大学JW系统验证码，并已经打上对应的标签

![](README_IMG/预览.png)

+ 验证码中只包含如下字符：`2345678abcdefgmnpwxy`，共20个字符随机排列组合生成的4位验证码，与教务处生成的验证码的定义域**完全匹配**。
+ 数据集采用谷歌的[Kaptcha](https://code.google.com/archive/p/kaptcha/)生成。
+ 实际使用时魔改了此Github仓库的代码用于渲染生成：

   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=oopsguy&repo=kaptcha-spring-boot)](https://github.com/oopsguy/kaptcha-spring-boot)
   
   >因为魔改实在过于丑陋，就不放本人的源代码在这里了。
 
+ 可以用于深度学习的训练集，尝试构建Hack JWC的深度学习模型

## 使用
+ 验证码图片存储于[IMAGES.zip](IMAGES.zip)中
+ 标签集合存于[label.csv](label.csv)中，每一行是`[图片序号, 验证码对应字符串]` 的列表，可以用Python的如下方法读取：
```python
import csv
data = []
# 读取数据
with open("label.csv", 'r', newline="" , encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
# 预览数据
for line in data:
    print(line)
```
序号与`IMAGES.zip`；里的文件名一一对应。

当然，如果需要进行深度学习还需要进行训练集测试集划分，随机抽取等等操作，请自行处理，祝君好运~
