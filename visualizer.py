import matplotlib.pyplot as plt
import pandas as pd

def create_sentiment_chart(df, output_filename="duygu_analizi_grafik.png"):
    """
    DataFrame'deki etiket dağılımını bir çubuk grafiğe dönüştürür
    ve bir dosyaya kaydeder.
    """
    if df is None or df.empty:
        print("Grafik oluşturulamadı: Geçersiz veri.")
        return

    print("Grafik oluşturuluyor...")
    
    duygu_dagilimi = df['Etiket'].value_counts()
    
    renk_paleti = {'POSITIVE': 'green', 'NEGATIVE': 'red', 'NEUTRAL': 'gray'}
    renkler = [renk_paleti.get(etiket, 'blue') for etiket in duygu_dagilimi.index]

    plt.figure(figsize=(10, 6))
    plt.bar(duygu_dagilimi.index, duygu_dagilimi.values, color=renkler)
    
    plt.title('Duygu Analizi Sonuç Grafiği', fontsize=16)
    plt.xlabel('Tespit Edilen Duygu', fontsize=12)
    plt.ylabel('Metin (Tweet) Sayısı', fontsize=12)
    
    for i, v in enumerate(duygu_dagilimi.values):
        plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    
    try:
        plt.savefig(output_filename)
        print(f"Grafik başarıyla '{output_filename}' olarak kaydedildi.")
    except Exception as e:
        print(f"Grafik kaydedilirken hata oluştu: {e}")