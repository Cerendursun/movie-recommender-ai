https://movie-recommender-ai-6ussysbbczltc7rkzpcnpm.streamlit.app/
<img width="1919" height="908" alt="Ekran görüntüsü 2026-04-27 194121" src="https://github.com/user-attachments/assets/114b0805-4e06-478f-91b4-c9f461edfcb3" />
# 🎬 AI Film Öneri Sistemi

Bu proje, makine öğrenmesi kullanarak film önerileri yapan web tabanlı bir uygulamadır. Streamlit ile geliştirilmiştir ve modern, Netflix tarzı bir kullanıcı arayüzüne sahiptir.

## 🚀 Özellikler

- 🎯 TF-IDF ve Cosine Similarity ile film önerisi
- 🎬 OMDb API ile gerçek film posterleri
- 🎨 Modern ve responsive (mobil + masaüstü uyumlu) arayüz
- ⚡ Hızlı ve optimize edilmiş (RAM dostu)
- 🔍 Film seçimi için akıllı arama (autocomplete)

## 🧠 Nasıl Çalışır?

Bu sistem, doğal dil işleme (NLP) teknikleri kullanır:

- Film açıklamaları (overview) **TF-IDF** ile sayısal vektörlere dönüştürülür
- Filmler arası benzerlik **Cosine Similarity** ile hesaplanır
- Seçilen filme en benzer filmler kullanıcıya önerilir

## 🛠️ Kullanılan Teknolojiler

- Python
- Streamlit
- Pandas
- Scikit-learn
- OMDb API

## 📊 Veri Seti

- TMDB 5000 Movies Dataset
