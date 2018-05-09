This is COMP30024 Project B


PlayerFunction.py can be used as import package.

实质上，算法在极小极大的递归中维护两个额外的值：alpha和beta。alpha是Max的最小值（对Max来说，是其最大损失），beta是Minnie的最大值（对Max来说，是其最大得益）。一开始，alpha的取值为负无穷，beta的取值为正无穷。在极小极大递归的过程中，当极小极大值比alpha更大时，alpha被替换为该值（beta也是一样的，当算出的值比其更小时）。如果它们在某个时刻相交了（即alpha>=beta），那么当前查找的分支对于所有玩家都不会带来得益，因此可以被忽略掉，或裁剪掉。
