import figure_lib as liba

# test1 right triangle

a = liba.DataFigure(3, 4, 5, 0)
print("---> right Triangle")
a.check_type()
#test2 random triangle
print("---> random Triangle")
a = liba.DataFigure(6, 4, 5, 0)
a.check_type()
#test3 circle
print("---> circle")
a = liba.DataFigure(0, 0, 0, 5)
a.check_type()
#test4 type error cheking
print("---> type error cheking")
a = liba.DataFigure("привет", 0, 0, 5)
a.check_type()
#test5 random numbers checking
print("---> random numbers checking")
a = liba.DataFigure(4, 0, 0, 5)
a.check_type()