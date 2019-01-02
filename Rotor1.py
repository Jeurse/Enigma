#lettre rentrée : i
texte=input ("saisir texte: ")
l=len (texte)
aa="a"#jj
bb="b"#uu
cc="c"#hh
dd="d"#ss
ee="e"#nn
ff="f"#pp
gg="g"#vv
hh="h"#cc
ii="i"#qq
jj="j"#ll
kk="k"#ww
ll="l"#rr
mm="m"#dd
nn="n"#xx
oo="o"#bb
pp="p"#tt
qq="q"#ff
rr="r"#ii
ss="s"#zz
tt="t"#ee
uu="u"#kk
vv="v"#oo
ww="w"#aa
xx="x"#yy
yy="y"#gg
zz="z"#mm

for i in texte:
    if i == aa:
        i,ww = ww,i

    else:
     if i == bb:
         i,oo = oo,i

     else:
      if i == cc:
          i,hh = hh,i

      else:
       if i == dd:
           i,mm = mm,i

        else:
         if i == ee:
             i,tt = tt,i

         else:
          if i == ff:
              i,qq = qq,i

          else:
           if i == gg:
               i,yy = yy,i

           else:
            if i == hh:
                i,cc = cc,i

            else:
             if i == ii:
                 i,rr = rr,i

             else:
              if i == jj:
                  i,aa = aa,i

              else:
               if i == kk:
                   i,uu = uu,i

               else:
                if i == ll:
                    i,jj = jj,i

                else:
                 if i == mm:
                     i,zz = zz,i

                 else:
                  if i == nn:
                      i,ee = ee,i

                  else:
                   if i == oo:
                       i,vv = vv,i

                   else:
                    if i == pp:
                        i,ff= ff,i

                    else:
                     if i == qq:
                         i,ii = ii,i

                     else:
                      if i == rr:
                          i,ll= ll,i

                      else:
                       if i == ss:
                           i,dd = dd,i

                       else:
                        if i == tt:
                            i,pp = pp,i

                        else:
                         if i == uu:
                             i,bb = bb,i

                         else:
                          if i == vv:
                              i,gg = gg,i

                          else:
                           if i == ww:
                               i,kk = kk,i

                           else:
                            if i == xx:
                                i,nn = nn,i

                            else:
                             if i == yy:
                                 i,xx = xx,i

                             else:
                              if i == zz:
                                  i,ss = ss,i
print(i)
