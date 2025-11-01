# main.py

import argparse  # Komut satırı argümanları için
import pandas as pd
from analyzer import SentimentAnalyzer
from visualizer import create_sentiment_chart

def read_input_file(filepath, column_name): # Artık column_name parametresi alıyor
    try:
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
            if column_name not in df.columns: # Sütun adını değişkenden kontrol et
                print(f"Hata: '{filepath}' dosyasında '{column_name}' sütunu bulunamadı.")
                print(f"Bulunan sütunlar: {list(df.columns)}")
                return None
            return df[column_name].dropna().tolist() # Belirtilen sütunu al
        
        elif filepath.endswith('.txt'):
            # Her satırı bir metin olarak okur
            with open(filepath, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        else:
            print("Hata: Desteklenmeyen dosya formatı. Lütfen .txt veya .csv kullanın.")
            return None
    except FileNotFoundError:
        print(f"Hata: '{filepath}' dosyası bulunamadı.")
        return None
    except Exception as e:
        print(f"Dosya okunurken hata: {e}")
        return None

def main():
    # 1. Komut satırı argümanlarını tanımla
    parser = argparse.ArgumentParser(description="Türkçe metinler için duygu analizi aracı.")
    parser.add_argument(
        '-i', '--input', 
        required=True, 
        help="Analiz edilecek metinleri içeren dosya (.txt veya .csv)"
    )
    parser.add_argument(
        '-o', '--output', 
        default="sonuclar.csv", 
        help="Analiz sonuçlarının kaydedileceği CSV dosyası (varsayılan: sonuclar.csv)"
    )
    parser.add_argument(
        '-g', '--graph', 
        default="duygu_grafik.png", 
        help="Sonuç grafiğinin kaydedileceği resim dosyası (varsayılan: duygu_grafik.png)"
    )
    parser.add_argument(
    '-c', '--column',
    default="text",
    help="Eğer .csv dosyası kullanılıyorsa, analiz edilecek metni içeren sütunun adı (varsayılan: text)"
    )
    args = parser.parse_args()

    # 2. Girdi dosyasını oku
    print(f"Girdi dosyası okunuyor: {args.input}")
    metinler = read_input_file(args.input, args.column)
    
    if metinler is None or len(metinler) == 0:
        print("Analiz edilecek metin bulunamadı. Program sonlandırılıyor.")
        return

    # 3. Analiz motorunu başlat ve analiz yap
    try:
        analyzer = SentimentAnalyzer()
        results_df = analyzer.analyze(metinler)
    except Exception as e:
        print(f"Analiz işlemi başarısız oldu: {e}")
        return

    # 4. Sonuçları dosyaya kaydet
    if results_df is not None:
        try:
            results_df.to_csv(args.output, index=False, encoding='utf-8-sig')
            print(f"Analiz sonuçları '{args.output}' dosyasına kaydedildi.")
            
            # 5. Grafiği oluştur ve kaydet
            create_sentiment_chart(results_df, args.graph)
            
            print("\n--- İşlem Tamamlandı ---")
            print("Etiket Dağılımı:")
            print(results_df['Etiket'].value_counts())
            
        except Exception as e:
            print(f"Sonuçlar kaydedilirken bir hata oluştu: {e}")

if __name__ == "__main__":
    main()