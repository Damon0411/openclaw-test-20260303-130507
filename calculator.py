"""
简单的计算器模块
提供基本的数学运算和统计功能
"""

class Calculator:
    """计算器类"""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """加法"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """减法"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """乘法"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    
    @staticmethod
    def power(base: float, exponent: float) -> float:
        """幂运算"""
        return base ** exponent
    
    @staticmethod
    def sqrt(x: float) -> float:
        """平方根"""
        if x < 0:
            raise ValueError("负数没有实数平方根")
        return x ** 0.5


class Statistics:
    """统计工具类"""
    
    @staticmethod
    def mean(numbers: list) -> float:
        """计算平均值"""
        if not numbers:
            raise ValueError("数字列表不能为空")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def median(numbers: list) -> float:
        """计算中位数"""
        if not numbers:
            raise ValueError("数字列表不能为空")
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            mid1 = sorted_numbers[n // 2 - 1]
            mid2 = sorted_numbers[n // 2]
            return (mid1 + mid2) / 2
    
    @staticmethod
    def variance(numbers: list) -> float:
        """计算方差"""
        if len(numbers) < 2:
            raise ValueError("至少需要两个数字计算方差")
        
        mean_val = Statistics.mean(numbers)
        return sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
    
    @staticmethod
    def std_dev(numbers: list) -> float:
        """计算标准差"""
        return Statistics.variance(numbers) ** 0.5


def main():
    """主函数 - 演示使用"""
    print("=== Python 计算器演示 ===")
    
    calc = Calculator()
    stats = Statistics()
    
    # 基本运算演示
    print("\n1. 基本运算:")
    print(f"   5 + 3 = {calc.add(5, 3)}")
    print(f"   10 - 4 = {calc.subtract(10, 4)}")
    print(f"   6 * 7 = {calc.multiply(6, 7)}")
    print(f"   15 / 3 = {calc.divide(15, 3)}")
    print(f"   2^8 = {calc.power(2, 8)}")
    print(f"   √25 = {calc.sqrt(25)}")
    
    # 统计演示
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\n2. 统计计算 (数据: {numbers}):")
    print(f"   平均值: {stats.mean(numbers):.2f}")
    print(f"   中位数: {stats.median(numbers):.2f}")
    print(f"   方差: {stats.variance(numbers):.2f}")
    print(f"   标准差: {stats.std_dev(numbers):.2f}")
    
    print("\n=== 演示结束 ===")


if __name__ == "__main__":
    main()