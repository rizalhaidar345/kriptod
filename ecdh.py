def ECDH(n, g):
    x = int(input("Masukkan bilangan acak x: "))
    y = int(input("Masukkan bilangan acak y: "))
    Xn = pow(g, x)%n
    Yn = pow(g, y)%n
    K = pow(Yn, x)%n
    K2 = pow(Xn, y)%n
    if K == K2:
        print("Kunci rahasia: {}".format(K))
    else:
        print("Kunci rahasia tidak sama")
    return K

ECDH(97, 5)