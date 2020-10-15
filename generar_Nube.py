# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 07:32:07 2019

@author: Ing. Industrial
"""

from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

def generar_Nube(texto):
    matplotlib.use("Qt5Agg")
    Nube=WordCloud(background_color="white",stopwords={"ou","ao","um","on","os","das","that","da","PME","was","uma","com","ha","was","do","na","em","ha","más","es","which","other","from","an","a","as","with","from","will","it","be","by","are","for","is","to","this","and","of","esta","es","the","in","ESTE","todo","donde","toda","este","así","no","se","le","les","como","con","sus","su","porque", "esto","estos", "vez","que","una","su","tu","al","del","a","en","desde","el","la","un","los","las","entre","de","para","nos","les","te","por"})
    Nube_generada=Nube.generate(texto)
    plt.imshow(Nube_generada)
    plt.axis("off")
    plt.show()
    return str(Nube.process_text(texto))

