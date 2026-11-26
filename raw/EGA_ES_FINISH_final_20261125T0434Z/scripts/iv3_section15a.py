from iv3_review_blocks import reviewed_math
from iv3_manual import patch
# First call completed against the saved, reviewed block offsets.
patch('15.1.1','Podemos, pues, limitarnos al caso','Se puede, pues, limitar al caso')
patch('15.1.1.6',r'clases $\bmod\mathfrak{m}^2$',r'clases mod. $\mathfrak m^2$')
patch('15.2.4','divisores de cero','divisores de $0$')
patch('15.2.4','una curva con una cúspide,','una curva con una cúspide $y$,')
patch('15.2.4',r'el cuerpo de series formales de Laurent sobre $k$, y sea $A_0$ su anillo de valoración para la valoración discreta dada por el orden de una serie formal de Laurent',r'el cuerpo de las series formales sobre $k$, $A_0$ el anillo de valoración para $K_0$ correspondiente a la valoración discreta igual al \emph{orden} de las series formales')
patch('15.2.4',r"es el anillo de valoración discreta de $K$.",r"es el anillo de valoración discreta para $K$ correspondiente al orden de las series formales sobre $K$.")
patch('15.2.4',r'las condiciones~$1)$ y $2)$',r'las condiciones 1) y 2)')
patch('15.2.4','y quedamos de nuevo reducidos al caso','y se reduce de nuevo al caso')

