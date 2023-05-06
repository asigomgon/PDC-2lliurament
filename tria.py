import sys

# rep dues seqüències: primers -1 resta a discriminar entre múltiples i primers

def mots(seq):
    for línia in seq:
        for mot in línia.split():
            yield mot

def enters(seq):
    for e in mots(seq):
        yield int(e)

    
def tria():
    r"""
    Rep pel canal estàndard d'entrada la seqüència textual de línies que contenen un nombre. La seqüència de nombres la podem caracteritzar com:

    :math:`p_1\ p_2 \ldots p_e\ -1\ n_1\ n_2\ \ldots n_d` 

    on hi ha un únic nombre -1 que separa la seqüència en dos subseqüències de naturals: *esquerra* i *dreta*.

    L'*esquerra* conté els :math:`e` primers primers a partir del 2 (:math:`p_1=2`) i :math:`p_i<p_{i+1}\quad \forall i:1\le i < e`. 

    La dreta son tots els naturals creixents fins :math:`n_d` i no múltiples de cap :math:`p_i\quad  \forall i:1\le i \le e` i :math:`n_i<n_{i+1}\quad \forall i:1\le i < d` i :math:`n_1 > p_e`. 

    Pel canal estandard de sortida, obtindrem


    :math:`p_1\ p_2 \ldots p_{e + 1}\ -1\ m_1\ m_2\ \ldots m_r` 

    on 
    
    :math:`p_i> 0\quad 1\le i \le e` i :math:`p_i` son els :math:`e+1` primers primers a partir del 2 (:math:`p_1= 2`). És a dir, té un primer més que la subseqüència esquerra d'entrada; i 

    la nova part dreta segueix complint les mateixes propietats que la de l'entrada amb probablement menys nombres: cap múltiple de :math:`p_i\quad  \forall i:1\le i \le e` i :math:`m_i<m_{i+1}\quad \forall i:1\le i < d` i :math:`m_1 > p_{e+1}`. La nova part pot ser buïda si a l'entrada només havia un nombre: :math:`r\le d`.

    """
    primers = True
    seq = enters(sys.stdin)
    e = next(seq)
    while e != -1: # escrivim primers
        print(e)
        e = next(seq)
    p = next(seq) # nou primer
    print(p)
    print(-1) # separador
    for e in seq: #filtrem múltiples
        if (e % p) !=0:
            print(e)

if __name__ == '__main__':
    tria()

