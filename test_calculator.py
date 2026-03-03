"""
计算器模块的单元测试
"""

import pytest
import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import Calculator, Statistics


class TestCalculator:
    """测试计算器类"""
    
    def test_add(self):
        """测试加法"""
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0
        assert Calculator.add(2.5, 3.5) == 6.0
    
    def test_subtract(self):
        """测试减法"""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(3, 5) == -2
        assert Calculator.subtract(0, 0) == 0
    
    def test_multiply(self):
        """测试乘法"""
        assert Calculator.multiply(3, 4) == 12
        assert Calculator.multiply(-2, 3) == -6
        assert Calculator.multiply(0, 5) == 0
    
    def test_divide(self):
        """测试除法"""
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(7, 2) == 3.5
        
        # 测试除零异常
        with pytest.raises(ValueError, match="除数不能为零"):
            Calculator.divide(5, 0)
    
    def test_power(self):
        """测试幂运算"""
        assert Calculator.power(2, 3) == 8
        assert Calculator.power(5, 0) == 1
        assert Calculator.power(4, 0.5) == 2
    
    def test_sqrt(self):
        """测试平方根"""
        assert Calculator.sqrt(9) == 3
        assert Calculator.sqrt(0) == 0
        assert Calculator.sqrt(2.25) == 1.5
        
        # 测试负数平方根异常
        with pytest.raises(ValueError, match="负数没有实数平方根"):
            Calculator.sqrt(-1)


class TestStatistics:
    """测试统计类"""
    
    def test_mean(self):
        """测试平均值"""
        assert Statistics.mean([1, 2, 3, 4, 5]) == 3
        assert Statistics.mean([10]) == 10
        assert Statistics.mean([-1, 0, 1]) == 0
        
        # 测试空列表异常
        with pytest.raises(ValueError, match="数字列表不能为空"):
            Statistics.mean([])
    
    def test_median(self):
        """测试中位数"""
        # 奇数个元素
        assert Statistics.median([1, 3, 2]) == 2
        assert Statistics.median([5, 2, 1, 4, 3]) == 3
        
        # 偶数个元素
        assert Statistics.median([1, 2, 3, 4]) == 2.5
        assert Statistics.median([10, 20, 30, 40]) == 25
        
        # 测试空列表异常
        with pytest.raises(ValueError, match="数字列表不能为空"):
            Statistics.median([])
    
    def test_variance(self):
        """测试方差"""
        # 简单测试
        assert Statistics.variance([1, 2, 3, 4, 5]) == 2.0
        assert Statistics.variance([10, 20]) == 25.0
        
        # 测试边界条件
        with pytest.raises(ValueError, match="至少需要两个数字计算方差"):
            Statistics.variance([5])
        
        with pytest.raises(ValueError, match="至少需要两个数字计算方差"):
            Statistics.variance([])
    
    def test_std_dev(self):
        """测试标准差"""
        # 标准差是方差的平方根
        numbers = [1, 2, 3, 4, 5]
        variance = Statistics.variance(numbers)
        std_dev = Statistics.std_dev(numbers)
        assert std_dev == pytest.approx(variance ** 0.5)
        
        # 具体值测试
        assert Statistics.std_dev([1, 2, 3, 4, 5]) == pytest.approx(1.41421356)


def test_integration():
    """集成测试 - 测试多个功能组合"""
    # 创建测试数据
    numbers = [2, 4, 6, 8, 10]
    
    # 使用计算器进行运算
    sum_result = Calculator.add(Calculator.add(numbers[0], numbers[1]), 
                               Calculator.add(numbers[2], numbers[3]))
    
    # 使用统计工具
    mean_result = Statistics.mean(numbers)
    median_result = Statistics.median(numbers)
    
    # 验证结果
    assert sum_result == 20
    assert mean_result == 6
    assert median_result == 6
    
    print("集成测试通过!")


if __name__ == "__main__":
    """直接运行测试"""
    print("运行计算器单元测试...")
    
    # 创建测试实例
    test_calc = TestCalculator()
    test_stats = TestStatistics()
    
    # 运行计算器测试
    test_calc.test_add()
    test_calc.test_subtract()
    test_calc.test_multiply()
    test_calc.test_divide()
    test_calc.test_power()
    test_calc.test_sqrt()
    
    # 运行统计测试
    test_stats.test_mean()
    test_stats.test_median()
    test_stats.test_variance()
    test_stats.test_std_dev()
    
    # 运行集成测试
    test_integration()
    
    print("所有测试通过! ✅")