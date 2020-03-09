# Django学习笔记
django会为表自动添加一个主键列，如果存在主键列，将不会添加
属性命名的限制：不允许使用连续的下划线。
软件压缩原理：文本可通过转化类型获得极大的优化，比如文本里有个布尔值用的整型类型定义。
逻辑删除：重要数据作逻辑删除，不做物理删除，只是看不到了，但仍然存在。在django中是定义isDelete属性，默认为False。
## 字段类型：
- AutoField:一个根据实际ID自动增长的IntegerField,如果不指定主键，会增加该类型的列
- CharField:字符串字段，max_length用于指定字符长度
- IntegerField:整数字段
- TextField：大文本字段。一般超过4000使用，默认的表单控件为Textarea（文本域）
- DecimalField：十进制浮点数字段，max_digits指定位数总数，decimal_places指定小数点后位数
- FloatField：浮点数字段
- BooleanField: 布尔值字段
- NullBooleanField: 支持null、true、false三种值
- DateField：日期字段，使用datetime.date实例表示的日期,auto_now参数指定每次保存对象时，是否自动设置为当前时间。auto_now_add参数只设置第一次创建的时间
- TimeField：时间字段，参数同DateField
- DateTimeField：日期时间字段，参数同上
- FileField：一个上传文件的字段，一般不会直接存在数据库，一般存的是图片路径
- ImageField：继承了FileField的所有属性和方法，但对上传的对象进行校验
***
## 字段选项
- null: 若为True，将空值用null存在数据库中
- blank：若为True，则将空字符串存在数据库中
- db_column: 字段的名称，默认使用属性名
- db_index: 若为True，在表中会为此段创建索引，索引相当于让两个列表之间有某种关联，更便于查找
- default：用于设置默认值
- primary_key: 指定主键
- unique：指定字段必须有唯一值，即不能重复
***
## 关系
### 分类
- ForeignKey：一对多，字段定义在多的端中
- ManyToManyField: 多对多，字段定义在两段中
- OneToOneField: 一对一，字段定义在任意一端中
***
## 数据操作
Django默认通过模型的objects对象实现模型数据查询
有两种过滤器用于筛选记录：filter（符合条件）、exclude（不符合条件），可以链式调用