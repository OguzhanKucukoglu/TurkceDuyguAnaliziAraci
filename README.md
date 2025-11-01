# NLP Projesi: Türkçe Duygu Analizi Aracı

Bu proje, Python ve Hugging Face Transformers kütüphanesini kullanarak verilen Türkçe metinlerin (tweet, yorum vb.) duygu analizini (Pozitif, Negatif, Nötr) yapan bir komut satırı aracıdır.

![Örnek Grafik](duygu_grafik.png)  ## ✨ Özellikler

* `.txt` (satır satır) veya `.csv` (belirtilen sütundan) dosyalarından metin okuma.
* Güçlü `savasy/bert-base-turkish-sentiment-cased` modelini kullanarak yüksek doğruluklu analiz.
* Analiz sonuçlarını `.csv` dosyası olarak kaydetme.
* Sonuçların duygu dağılımını gösteren bir `.png` çubuk grafik oluşturma.

## 🚀 Kurulum

1.  **Projeyi klonlayın:**
    ```bash
    git clone [PROJENIZIN_GITHUB_LINKI]
    cd DuyguAnaliziProjesi
    ```

2.  **Sanal ortam oluşturun ve aktive edin:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\Activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Gerekli kütüphaneleri kurun:**
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Kullanım

Aracı `main.py` dosyası üzerinden komut satırı argümanları ile çalıştırabilirsiniz.

**Temel Kullanım:**

```bash
python main.py --input girdi_dosyasi.txt