# analyzer.py

import pandas as pd
from transformers import pipeline

class SentimentAnalyzer:
    """
    Duygu analizi modelini yükleyen ve analiz yapan sınıf.
    Modeli bir kez yükler ve hafızada tutar.
    """
    def __init__(self, model_name="savasy/bert-base-turkish-sentiment-cased"):
        print("Model yükleniyor...")
        try:
            self.sentiment_analyzer = pipeline(task="sentiment-analysis", model=model_name)
            print("Model başarıyla yüklendi.")
        except Exception as e:
            print(f"Hata: Model yüklenemedi. {e}")
            raise
            
    def analyze(self, metin_listesi):
        """
        Verilen metin listesini analiz eder ve sonuçları bir DataFrame'e dönüştürür.
        """
        print(f"\n{len(metin_listesi)} adet metin analiz ediliyor...")
        try:
            sonuclar = self.sentiment_analyzer(metin_listesi)
            print("Analiz tamamlandı.")
            
            islenmis_veriler = []
            for metin, sonuc in zip(metin_listesi, sonuclar):
                islenmis_veriler.append({
                    'Metin': metin,
                    'Etiket': sonuc['label'].upper(),
                    'Skor': sonuc['score']
                })
            
            df = pd.DataFrame(islenmis_veriler)
            return df
        except Exception as e:
            print(f"Analiz sırasında bir hata oluştu: {e}")
            return None