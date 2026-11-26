from iv3_review_blocks import reviewed_math
from iv3_manual import patch
reviewed_math([1,4,6,7,8,9,10,14,15,17,20,21,22,23,24])
patch('15.7.1',r'la restricción de $f$ a $Z$',r'la restricción $Z\to Y$ de $f$ a $Z$')
patch('15.7.2',r'la restricción $f^{-1}(U)\to U$ de $f$ será propia',r'la restricción $f^{-1}(U)\to U$ será propia')
patch('15.7.4',r'$\mathbf{0}_{\mathrm{III}},~9.2.2$',r'$\mathbf{0}_{\mathrm{III}}$, 9.2.2')
patch('15.7.4',r'por la definición de una parte propia sobre $Y$',r'por la definición de una parte propia')
patch('15.7.6',r'observemos primero que \emph{a)} implica que $f(X)$ es localmente cerrado en $Y$.',r'observemos primero que \emph{a)} implica que $h(Z)$ es localmente cerrado en $Y$ y $g(X)$ cerrado en $Z$, y por tanto $f(X)$ es localmente cerrado en $Y$;')
patch('15.7.6',r"$g_0:X\to Z'$",r"$g_0$ es un morfismo de $X$ en $Z'$")
patch('15.7.7',r'$\mathbf{0}_{\mathrm{III}},~10.3.1$',r'$\mathbf{0}_{\mathrm{III}}$, 10.3.1')
patch('15.7.9',r'$\mathbf{0}_{\mathrm{I}},~7.3.5$',r'$\mathbf{0}_{\mathrm{I}}$, 7.3.5')
patch('15.7.9','nos limitaremos en adelante al caso','podemos limitarnos al caso')
patch('15.7.9',r'una partición de $Z$ en dos partes abiertas y cerradas.',r'una partición de $Z$ en dos partes abiertas y cerradas en $Z$.')
patch('15.7.9',r'$\mathbf{0}_{\mathrm{III}},~9.2.5$',r'$\mathbf{0}_{\mathrm{III}}$, 9.2.5')
patch('15.7.9',r'que solo satisface las condiciones (i) \emph{y} (iii)',r'que satisface las \emph{dos únicas condiciones} (i) \emph{y} (iii)')
patch('15.7.9','Sea $A_1$ un anillo de valoración discreta completo',r'Sea $A_1$ un anillo de valoración discreta \emph{completo}')
patch('15.7.11','Estas observaciones muestran que quedamos reducidos a probar','Estas observaciones muestran que se reduce a probar')
patch('15.7.11','Probemos ahora el','Señalemos ahora el')

