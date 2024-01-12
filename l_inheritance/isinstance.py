# isinstance: 객체간 타입 비교
class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(isinstance(a,A))
print(isinstance(b,B))

# 모든 자식은 부모타입(b는 B의 타입이기도 하고 A의 타입이기도 하다)
print(isinstance(b,A))
# 부모는 절대 자식타입이 될 수 없다.
print(isinstance(a, B))