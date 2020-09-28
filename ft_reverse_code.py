def ft_bin_num(a):
    if a < 0:
        a *= -1
    desit = 1
    it = 0
    while a > 0:
        it += a % 2 * desit
        desit *= 10
        a //= 2
    return it


def ft_len_num(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    return i


def ft_straight_code(y):
    dvoi = ft_bin_num(y)
    dlin = ft_len_num(dvoi)
    if y < 0:
        dvoi = dvoi + 10000000
        return dvoi
    else:
        return dvoi


def ft_reverse_code(q):
    prum = ft_straight_code(q)
    pov = prum
    chis = 0
    dell = 1
    while pov > 0:
        if (prum // dell) % 10 == 1:
            prum = prum - (1 * dell)
        elif (prum // dell) % 10 == 0:
            prum = prum + (1 * dell)
        pov = pov // 10
        dell *= 10
    return prum
        
