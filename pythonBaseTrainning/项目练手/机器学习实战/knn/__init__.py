# _*_ coding = utf-8 _*_
# @Date : 2021/12/3
# @Time : 13:27
# @NAME ：molin

'''
k-近邻算法步骤如下：

计算已知类别数据集中的点与当前点之间的距离；
按照距离递增次序排序；
选取与当前点距离最小的k个点；
确定前k个点所在类别的出现频率；
返回前k个点所出现频率最高的类别作为当前点的预测分类。
'''