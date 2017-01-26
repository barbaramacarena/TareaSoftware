from calculo import Tarifa,calcularServicio,esFinDeSemana
import unittest
import datetime
import time
from datetime import datetime, date, time, timedelta

# Autores: Verónica Mazutiel , 13-10853
#          Bárbara Hernández , 11-10246

class TestCalculo(unittest.TestCase):
    def testMalicia1(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,19,15,53, 0)
        f2=datetime(2017,1,21,16,59,0)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 6700)
        
    def testMalicia2(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,19,16,1, 0)
        f2=datetime(2017,1,22,18,0,59)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 11800)
    
    def testMalicia3(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,16,10,0, 1)
        f2=datetime(2017,1,18,6,0,0)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 4400)
        
    def testMalicia4(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,19,16,0, 1)
        f2=datetime(2017,1,19,18,0,59)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 300)
        
    def testMinimo(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,26,6,0, 0)
        f2=datetime(2017,1,26,6,15,0)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 100)
        
    def testMaximo(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,24,13,0, 0)
        f2=datetime(2017,1,31,13,0,0)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 21600)
        
    def testEsquinaInf(self):
        tarifa= Tarifa(100,200)
        #Caso frontera
        f1= datetime(2017, 1, 23, 7, 0, 0)
        f2=datetime(2017,1,23,7,15,1)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 100)
        
    def testEsquinaSup(self):
        tarifa= Tarifa(100,200)
        f1=datetime(2017, 1,10,3,0, 0)
        f2=datetime(2017,1,17,2,59,59)
        self.assertEqual(calcularServicio(tarifa, [f1,f2]), 21600)
   
        
if __name__ == '__main__':
    unittest.main()