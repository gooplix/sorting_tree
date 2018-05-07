   def sort5d(a,b,c,d,e):
   # Sorts 5 numbers is descending order. Output is a five numbers sorted from largest to smallest
   # Usage:
   # sorted = sort5d(9,3,1,19,-8)
   # or
   # p0,p1,p2,p3,p4 = sort5d(9,3,1,19,-8)
    if a > b:
        # a > b
        if c > d:
            # a > b ; c > d
            if a > c:
                # a > c > d ; a > b; 15 returns
                if e > c:
                    if e > a:
                        # e > a > c > d; a > b
                        if b > d:
                            if b > c:
                                return e, a, b, c, d
                            else:
                                return e, a, c, b, d
                        else:
                            return e, a, c, d, b
                    else:
                        # a > e > c > d; a > b
                        if b > c:
                            if b > e:
                                return a, b, e, c, d
                            else:
                                return a, e, b, c, d
                        else:
                            if b > d:
                                return a, e, c, b, d
                            else:
                                return a, e, c, d, b
                else:
                    if e > d:
                        # a > c > e > d; a > b
                        if b > e:
                            if b > c:
                                return a, b, c, e, d
                            else:
                                return a, c, b, e, d
                        else:
                            if b > d:
                                return a, c, e, b, d
                            else:
                                return a, c, e, d, b
                    else:
                        # a > c > d > e ; a > b
                        if b > d:
                            if b > c:
                                return a, b, c, d, e
                            else:
                                return a, c, b, d, e
                        else:
                            if b > e:
                                return a, c, d, b, e
                            else:
                                return a, c, d, e, b
            else:
                # c > a > b ; c > d; 15 returns
                if e > a:
                    if e > c:
                        # e > c > a > b; c > d
                        if d > b:
                            if d > a:
                                return e, c, d, a, b
                            else:
                                return e, c, a, d, b
                        else:
                            return e, c, a, b, d
                    else:
                        # c > e > a > b; c > d
                        if d > a:
                            if d > e:
                                return c, d, e, a, b
                            else:
                                return c, e, d, a, b
                        else:
                            if d > b:
                                return c, e, a, d, b
                            else:
                                return c, e, a, b, d
                else:
                    if e > b:
                        # c > a > e > b; c > d
                        if d > e:
                            if d > a:
                                return c, d, a, e, b
                            else:
                                return c, a, d, e, b
                        else:
                            if d > b:
                                return c, a, e, d, b
                            else:
                                return c, a, e, b, d
                    else:
                        # c > a > b > e ; c > d
                        if d > b:
                            if d > a:
                                return c, d, a, b, e
                            else:
                                return c, a, d, b, e
                        else:
                            if d > e:
                                return c, a, b, d, e
                            else:
                                return c, a, b, e, d
        else:
            # a > b ; d > c
            if a > d:
                # a > d > c ; a > b; 15 returns
                if e > d:
                    if e > a:
                        # e > a > d > c; a > b
                        if b > c:
                            if b > d:
                                return e, a, b, d, c
                            else:
                                return e, a, d, b, c
                        else:
                            return e, a, d, c, b
                    else:
                        # a > e > d > c; a > b
                        if b > d:
                            if b > e:
                                return a, b, e, d, c
                            else:
                                return a, e, b, d, c
                        else:
                            if b > c:
                                return a, e, d, b, c
                            else:
                                return a, e, d, c, b
                else:
                    if e > c:
                        # a > d > e > c; a > b
                        if b > e:
                            if b > d:
                                return a, b, d, e, c
                            else:
                                return a, d, b, e, c
                        else:
                            if b > c:
                                return a, d, e, b, c
                            else:
                                return a, d, e, c, b
                    else:
                        # a > d > c > e ; a > b
                        if b > c:
                            if b > d:
                                return a, b, d, c, e
                            else:
                                return a, d, b, c, e
                        else:
                            if b > e:
                                return a, d, c, b, e
                            else:
                                return a, d, c, e, b
            else:
                # d > a > b ; d > c; 15 returns
                if e > a:
                    if e > d:
                        # e > d > a > b; d > c
                        if c > b:
                            if c > a:
                                return e, d, c, a, b
                            else:
                                return e, d, a, c, b
                        else:
                            return e, d, a, b, c
                    else:
                        # d > e > a > b; d > c
                        if c > a:
                            if c > e:
                                return d, c, e, a, b
                            else:
                                return d, e, c, a, b
                        else:
                            if c > b:
                                return d, e, a, c, b
                            else:
                                return d, e, a, b, c
                else:
                    if e > b:
                        # d > a > e > b; d > c
                        if c > e:
                            if c > a:
                                return d, c, a, e, b
                            else:
                                return d, a, c, e, b
                        else:
                            if c > b:
                                return d, a, e, c, b
                            else:
                                return d, a, e, b, c
                    else:
                        # d > a > b > e ; d > c
                        if c > b:
                            if c > a:
                                return d, c, a, b, e
                            else:
                                return d, a, c, b, e
                        else:
                            if c > e:
                                return d, a, b, c, e
                            else:
                                return d, a, b, e, c
    else:
        # b > a
        if c > d:
            # b > a ; c > d
            if b > c:
                # b > c > d ; b > a; 15 returns
                if e > c:
                    if e > b:
                        # e > b > c > d; b > a
                        if a > d:
                            if a > c:
                                return e, b, a, c, d
                            else:
                                return e, b, c, a, d
                        else:
                            return e, b, c, d, a
                    else:
                        # b > e > c > d; b > a
                        if a > c:
                            if a > e:
                                return b, a, e, c, d
                            else:
                                return b, e, a, c, d
                        else:
                            if a > d:
                                return b, e, c, a, d
                            else:
                                return b, e, c, d, a
                else:
                    if e > d:
                        # b > c > e > d; b > a
                        if a > e:
                            if a > c:
                                return b, a, c, e, d
                            else:
                                return b, c, a, e, d
                        else:
                            if a > d:
                                return b, c, e, a, d
                            else:
                                return b, c, e, d, a
                    else:
                        # b > c > d > e ; b > a
                        if a > d:
                            if a > c:
                                return b, a, c, d, e
                            else:
                                return b, c, a, d, e
                        else:
                            if a > e:
                                return b, c, d, a, e
                            else:
                                return b, c, d, e, a
            else:
                # c > b > a ; c > d; 15 returns
                if e > b:
                    if e > c:
                        # e > c > b > a; c > d
                        if d > a:
                            if d > b:
                                return e, c, d, b, a
                            else:
                                return e, c, b, d, a
                        else:
                            return e, c, b, a, d
                    else:
                        # c > e > b > a; c > d
                        if d > b:
                            if d > e:
                                return c, d, e, b, a
                            else:
                                return c, e, d, b, a
                        else:
                            if d > a:
                                return c, e, b, d, a
                            else:
                                return c, e, b, a, d
                else:
                    if e > a:
                        # c > b > e > a; c > d
                        if d > e:
                            if d > b:
                                return c, d, b, e, a
                            else:
                                return c, b, d, e, a
                        else:
                            if d > a:
                                return c, b, e, d, a
                            else:
                                return c, b, e, a, d
                    else:
                        # c > b > a > e ; c > d
                        if d > a:
                            if d > b:
                                return c, d, b, a, e
                            else:
                                return c, b, d, a, e
                        else:
                            if d > e:
                                return c, b, a, d, e
                            else:
                                return c, b, a, e, d
        else:
            # b > a ; d > c
            if b > d:
                # b > d > c ; b > a; 15 returns
                if e > d:
                    if e > b:
                        # e > b > d > c; b > a
                        if a > c:
                            if a > d:
                                return e, b, a, d, c
                            else:
                                return e, b, d, a, c
                        else:
                            return e, b, d, c, a
                    else:
                        # b > e > d > c; b > a
                        if a > d:
                            if a > e:
                                return b, a, e, d, c
                            else:
                                return b, e, a, d, c
                        else:
                            if a > c:
                                return b, e, d, a, c
                            else:
                                return b, e, d, c, a
                else:
                    if e > c:
                        # b > d > e > c; b > a
                        if a > e:
                            if a > d:
                                return b, a, d, e, c
                            else:
                                return b, d, a, e, c
                        else:
                            if a > c:
                                return b, d, e, a, c
                            else:
                                return b, d, e, c, a
                    else:
                        # b > d > c > e ; b > a
                        if a > c:
                            if a > d:
                                return b, a, d, c, e
                            else:
                                return b, d, a, c, e
                        else:
                            if a > e:
                                return b, d, c, a, e
                            else:
                                return b, d, c, e, a
            else:
                # d > b > a ; d > c; 15 returns
                if e > b:
                    if e > d:
                        # e > d > b > a; d > c
                        if c > a:
                            if c > b:
                                return e, d, c, b, a
                            else:
                                return e, d, b, c, a
                        else:
                            return e, d, b, a, c
                    else:
                        # d > e > b > a; d > c
                        if c > b:
                            if c > e:
                                return d, c, e, b, a
                            else:
                                return d, e, c, b, a
                        else:
                            if c > a:
                                return d, e, b, c, a
                            else:
                                return d, e, b, a, c
                else:
                    if e > a:
                        # d > b > e > a; d > c
                        if c > e:
                            if c > b:
                                return d, c, b, e, a
                            else:
                                return d, b, c, e, a
                        else:
                            if c > a:
                                return d, b, e, c, a
                            else:
                                return d, b, e, a, c
                    else:
                        # d > b > a > e ; d > c
                        if c > a:
                            if c > b:
                                return d, c, b, a, e
                            else:
                                return d, b, c, a, e
                        else:
                            if c > e:
                                return d, b, a, c, e
                            else:
                                return d, b, a, e, c
