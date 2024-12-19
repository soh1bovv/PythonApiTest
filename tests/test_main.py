# #импортируем класс с мейна
# from main import Calculator
# import pytest
#
#
#
# #класс тестирования
# class TestCalculator:
#
# #тест с параметрами
#     @pytest.mark.parametrize("x,y,res",
#     [
#         (1,2,0.5), #параметры
#         (5,-1,-5)
#     ]
# )
#     def test_divide(self, x, y, res):
#         #проверка возвращаемого результата
#         assert Calculator().divide(x, y) == res
#
# # тест с параметрами
#     @pytest.mark.parametrize("x,y,res",
#     [
#         (1,2,3), #параметры
#         (5,-1,4)        ]
# )
#     def test_add(self,x,y,res):
#         # проверка возвращаемого результата
#             assert Calculator().add(x,y) == res