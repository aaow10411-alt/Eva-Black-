
import base64, zlib, marshal, hashlib, sys, os
from Crypto.Cipher import AES

if sys.gettrace():
    os._exit(1)

def _base_key():
    s = b"\x13\x37EvaBlack\x99"
    for _ in range(120_000):
        s = hashlib.sha256(s).digest()
    return s

BASE_KEY = _base_key()

_B = b'R(w1%=@{ZlSR#NWJuR4NoQvjE!!Nt!MX+nsvUujW@59&3u~Y+z%Rv{L5wbTndwY2I@oumeCRo(3vx9*&Z04<VXLu~!W~LCyX$i}!{(l3$PwxpJpCeWO8u$qV1c311>osy^zPiEE*49!#L3HM=yJEXdMd2FV$aSQsT>%z_a^#pUcN&}gpApas1~tVfaD?Bf|5+o5sPfw)syAT$b44ndW6&i*(HJIZA)xz@BWvb_E+{P=mUBp5IHwB+%9RFJ!A&Oc)CIOLXp0Y6x*J-g{%9z$PWAQ9037o@My3f{ozW7Ess|KwgG{E?Dkgdl^)1a=@ThAgoB5t;hKdQK47RLwJC{M`m3{p8o4lERjTTu-m2M$DX&)C}Z(6Qxj$F76e%5b#Pz#b3i{xJiiTo_S)VE3nX}E=zo&V9zvCDxsBmS@T6zG241<<*KMuoIdn>XZDzMZL^m&@R5et`7PgS!jC2z=%bAI=Ar0HkX-=x6Fcx~jcIzIMD)!G(y^i4KmoOtQ_Ao;KN!G_x~D*5QK3;XZZ4(<3Eip%V|TdvqldGo-22Sz8S=0WDp<@W(9$C@%1sVsj*@9yyy{DdtlT7~7hpuwz4v@%#D*T{{JI)MWwPwHn8yC(|E<g+E6GyF`b3nkzHZgtt~T=X@P?M#sSuOd<W|6Dh%>y$Le5hQ5iUiA=spFVq5~t!|WpCgXSo<QOd7Ck^?&x64g^w0~|!S=5q|BMoJPc|AMD&$!6KA+=fjBHAvxI!~ejvaqx`B!HKgnCs+tp;jM7X!X-18byHYFl@y~Ep1>{>*>?kbPQ0^XZ#=vn!$_KN_q#e-*?_k{JS9gkgDg2SDVi>!2hCcC+(};f2zs;6$?^_$A-Z{jiH)RP1+fVt!mNnhEzE;du2FLbCT6)Bgn59UhM2U<mC?lz#MsBllross-_3XH1vj^-dMoZn|{cw5cscY@v`0ynr0?-Y$ssn(K3e2D^MAYq11tIBie6f8G)mBV@}GK)8_;)I;L?|fOA0DIx)-hDS_;fz6YMb<7JRkLA?TL1>jbEpP8V5&jwV=pK4E9`*!4nh0CEnBacF#c;d^c_kiHUg<ufb^VjHy%h?w*1Xn-aTBQt&@UjUUCEUBTIe?}E`M3C!?lKO@>Xq}NjR~#%FV}F+yZnlTUg$1wA<q#SWPaOWvc<wp%|Fi-xu=L{nO2HT*V(HwZI9QCz7@UqY8_Hp=KYVeiOI7`C1bf}gKwJ3&HVIPEE3m8eAGt>{yz390E%izaiNbDn>ne0g%(7eAo2(mdw6&G$vI;nm!E`WZo>P>`)E`KEs5*eNvmAQdcE6ZG9wQ*mg#-B+VdM{PYK>9q|~M(+JYnjDGQJmG2o5SRNO!MVjePOt<&v^&FJj}f(1Ja%^zvX#(kQM#|`aud@(LME=$C^t)($C>diJjI6I?lS(<<uGOUaV?g8hv4BOTs;GFD@-5TZ1S-VJ5W-3<*V_$5iO?DmP?meJ>S4A8H(5O5oX!=Bo!qbCLdzP_vShf$+fUr&w<MnJ=kZ+4$6i5|mbzirFT^kP@VD4tvnB`KH7|^V_NtZxEuhw*{-7%I5McRn!iX|-4MpyNVIKdcg#3i+r;#|9Zh1A>%dQ!NjZswy_d33BV4U11p3*KA*4n(BqcVwA}rOX>aqu;0n^_Gvb&nJo0e6&bowMQO!2ttc&v8s{#mMXrhuAh=Li2eY^ZRl_-H|a#jIUpwY{R!c?3GA|e7U%%{1vkI{E()wp1;Ds(M4pYNalCp%5%qPO&V$s9JOI6<p0<?H<b2@->O@_2$rjmCbWd-!A$6ls=tEnc+p&gr%UBIlu?xH0Rz~qvwyn4kwTh1;kEw)lNDl_{$+aLxZu^!{s|ad0mFn%Ff1>=I3M0Vw3wyakGg}7KF}CMrJo^jsJSy`y*X13A6g4!wM;sZi`aWT$0>3kGC+qCZWMN9~Ov%NwjqR9adLE0pTj$dcu}>N~o9L&Tmz<*4TFQp~Noq=Gmgut?-hrCV4~ATHR!0#|(Jz+gv;H(~$dLWHA72`H2bl2d9v51Q{^AF4EfZ(GuY>T{`w0y>SN4fvnL;!HYbsSzm?tg5{`ku^qzljLdr^a`c`IlBRw2L4{|hF#fTXJMTXOM<@B&ZL`<=`5yMmkuZxB9rjUzV#PdX=`IuDQp1PmcW|KZICIf>zHi{Y;yY?&2m#dV)6Wue;0F7BM=2?lELsdI`V2-PqBeQIR)qDR+XpRB)Q=tdLm8Z`9C-n3(oH-gi<dKJ)87w&M0j6z-Lq4e|pJ8;fC&yPsUrPB^+1E_ZIxh4TUA6rleFAv$N0PyWT7Vq;IK4J%QYwyQjg2d?@K%27s7U;$`E_Y}LMq*jzPJ9{hOOQ9|f3F}-<eY9!ikP(_!6j3ZA@^%#+~oy3?lj>rs5QX0UsTs?jb#wIdebq+er~chIdL^<F*<8{L>He^DjAA!=G_%hYCEL<k>=9I<^Zva!|4Q+OlqvfOn5~I9#~2Uk>|RN|MhQv6rb_3(H+X74y3<IWVwb{`>b$JSzr&1L#|oy9;~HE+fkXh{mqPCfWRc)6Un7}De|MQgUHE=L02cB-8uSz#sBu2$?_5V)ABM!FhW=5YlzK@NotPbJe_YMKt~%6#IY(dh>Jv`BrazsYkmQ3Y}sWDvGkU#q=krg&vR|A>sf^jtvkbY6ZLJ4nZa2dA{w850UkydJfo57C?@|M)acTwjYg_wg%@r}%8&*B7-svnS%`_AnX7S;Lj*t$(3S2Cp0)J{!R)+vzuA?k$#A5!&6IT@Yo(-5-QW{|a8xV$zRzFq9$bz0J7jHqBS2M^hKA(5FdGjyr*Nt;#kn^G60M66$Gn)#g>$v7|2mQOYB|MNzZu`1$KoFvoRuEdE!!P!gl3ljab|R(WGNOeM=7({6o8N~j(9hVRYvS75Q`Yos>EZ61y<apaiPhC2$RWjL0@Z~*-g%V>$rnQOEOj;Ef|xdEf$y?q*EBaw^O^lQ<w<V70jY1$n;|%B3J`33vCe*h&of|2+Nc&L1V*{!xIAnEO$7%n*'

raw = base64.b85decode(_B)

xor_key = raw[:32]
n = raw[32:44]
t = raw[44:60]
e = raw[60:]

data = AES.new(BASE_KEY, AES.MODE_GCM, nonce=n).decrypt_and_verify(e, t)

data = bytes(b ^ xor_key[i % 32] for i, b in enumerate(data))

payload = marshal.loads(zlib.decompress(data))

del raw, e, t, n, xor_key, data, _B

exec(payload, {})

del payload
