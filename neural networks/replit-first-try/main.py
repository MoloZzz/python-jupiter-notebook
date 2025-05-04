import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

# Завантаження словника IMDB
word_index = imdb.get_word_index()

# Завантаження моделі
model = load_model("model.h5")

# Обробка тексту
def preprocess(text):
    words = text.lower().split()
    seq = [word_index.get(word, 2) for word in words]  # 2 — <UNK>
    padded = sequence.pad_sequences([seq], maxlen=500)
    return padded

# Передбачення
def predict_sentiment(text):
    x = preprocess(text)
    prediction = model.predict(x)
    return "Позитивний відгук 👍" if prediction[0][0] > 0.5 else "Негативний відгук 👎"

# Інтерфейс
gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label="Введіть текст відгуку"),
    outputs=gr.Textbox(label="Результат"),
    title="Аналіз сентименту фільмів IMDB",
    description="Ця модель аналізує, чи є текст позитивним або негативним."
).launch()
