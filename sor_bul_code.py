import json
import tkinter as tk
from tkinter import messagebox

questions = [
    "is_food", "is_real", "is_male", "is_live",
    "is_teacher", "is_employee", "is_student",
    "is_management", "is_handsome", "is_beatiful"
]

questions_text = {
    "is_food": "Bu bir yiyecek mi?",
    "is_real": "Bu bir gerçek varlık mı?",
    "is_male": "Bu bir erkek mi?",
    "is_live": "Hala hayatta mı?",
    "is_teacher": "Akademisyen mi?",
    "is_employee": "Çalışan (Hizmetli) mi?",
    "is_student": "Öğrenci mi?",
    "is_management": "İdari yönetici mi?",
    "is_handsome": "Yakışıklı mı?",
    "is_beatiful": "Güzel mi?"
}

def load_characters():
    try:
        with open('characters.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_characters(data):
    with open('characters.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_questions():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("questions", questions), data.get("questions_text", questions_text)
    except FileNotFoundError:
        return questions, questions_text

def save_questions(questions_list, questions_dict):
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump({"questions": questions_list, "questions_text": questions_dict}, f, indent=4, ensure_ascii=False)

questions, questions_text = load_questions()

class SorBulApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Sor-Bul")
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        self.main_menu()

    def main_menu(self):
        self.clear_window()

        # Üstte bilgi mesajı için ayrı frame
        info_frame = tk.Frame(self.root, bg="#ffeeee", pady=10)
        info_frame.pack(fill="x")
        info_label = tk.Label(info_frame, text=(
            "Not: Eklemek istediğin karaktere özel bir soru varsa,\n"
            "önce 'Yeni Soru Ekle' bölümünü kullan!"),
            font=("Helvetica", 10, "bold"), fg="red", bg="#ffeeee", justify="center"
        )
        info_label.pack()

        # Ana içerik frame (butonlar vs)
        content_frame = tk.Frame(self.root, pady=15)
        content_frame.pack(fill="both", expand=True)

        tk.Label(content_frame, text="SOR-BUL", font=("Helvetica", 20, "bold")).pack(pady=10)

        tk.Button(content_frame, text="Karakter Tahmini Yap", command=self.start_game, width=30).pack(pady=7)
        tk.Button(content_frame, text="Yeni Karakter Ekle", command=self.add_character, width=30).pack(pady=7)
        tk.Button(content_frame, text="Yeni Soru Ekle", command=self.add_new_question, width=30).pack(pady=7)
        tk.Button(content_frame, text="Çıkış", command=self.root.quit, width=30).pack(pady=7)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self):
        self.user_answers = {}
        self.characters = load_characters()
        if not self.characters:
            messagebox.showinfo("Uyarı", "Henüz hiç karakter yok.")
            return
        self.original_characters = self.characters.copy()
        self.current_q_index = 0
        self.ask_question()

    def ask_question(self):
        self.clear_window()
        if self.current_q_index >= len(questions):
            self.show_result()
            return
        current_q = questions[self.current_q_index]
        tk.Label(self.root, text=questions_text.get(current_q, current_q), font=("Helvetica", 14)).pack(pady=20)
        tk.Button(self.root, text="Evet", width=10, command=lambda: self.answer(True)).pack(pady=5)
        tk.Button(self.root, text="Hayır", width=10, command=lambda: self.answer(False)).pack(pady=5)

    def answer(self, value):
        current_q = questions[self.current_q_index]
        self.user_answers[current_q] = value
        self.characters = [c for c in self.characters if c.get(current_q) == value]
        self.current_q_index += 1
        self.ask_question()

    def show_result(self):
        self.clear_window()
        if len(self.characters) == 1:
            name = self.characters[0]['name']
            msg = f"Karakterin bu mu? 👉 {name}"
        elif len(self.characters) > 1:
            best_score = 0
            best_match = None
            for character in self.original_characters:
                score = sum(character.get(k) == v for k, v in self.user_answers.items())
                if score > best_score:
                    best_score = score
                    best_match = character
            if best_match:
                msg = f"En yakın tahminim: 👉 {best_match['name']}"
            else:
                msg = "Karakter bulunamadı."
        else:
            msg = "Karakter bulunamadı."
        tk.Label(self.root, text=msg, font=("Helvetica", 14)).pack(pady=20)
        tk.Button(self.root, text="Ana Menü", command=self.main_menu).pack(pady=10)

    def add_character(self):
        self.clear_window()
        self.new_character = {}
        tk.Label(self.root, text="Karakterin adı:").pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()
        self.q_index = 0
        tk.Button(self.root, text="Devam", command=self.ask_add_questions).pack(pady=10)

    def ask_add_questions(self):
        name = self.entry_name.get().strip()
        if not name:
            messagebox.showerror("Hata", "Lütfen isim girin.")
            return
        self.new_character["name"] = name
        self.ask_next_feature()

    def ask_next_feature(self):
        self.clear_window()
        if self.q_index >= len(questions):
            data = load_characters()
            data.append(self.new_character)
            save_characters(data)
            messagebox.showinfo("Başarılı", "Karakter eklendi!")
            self.main_menu()
            return
        current_q = questions[self.q_index]
        tk.Label(self.root, text=questions_text.get(current_q, current_q), font=("Helvetica", 14)).pack(pady=20)
        tk.Button(self.root, text="Evet", width=10, command=lambda: self.save_feature(True)).pack(pady=5)
        tk.Button(self.root, text="Hayır", width=10, command=lambda: self.save_feature(False)).pack(pady=5)

    def save_feature(self, value):
        self.new_character[questions[self.q_index]] = value
        self.q_index += 1
        self.ask_next_feature()

    def add_new_question(self):
        self.clear_window()
        tk.Label(self.root, text="Yeni sorunun kısa anahtarını girin (örn: is_athlete):").pack(pady=5)
        self.new_question_key = tk.Entry(self.root)
        self.new_question_key.pack(pady=5)

        tk.Label(self.root, text="Yeni sorunun açıklamasını girin:").pack(pady=5)
        self.new_question_text = tk.Entry(self.root)
        self.new_question_text.pack(pady=5)

        tk.Button(self.root, text="Ekle", command=self.save_new_question).pack(pady=10)
        tk.Button(self.root, text="İptal", command=self.main_menu).pack()

    def save_new_question(self):
        key = self.new_question_key.get().strip()
        text = self.new_question_text.get().strip()

        if not key or not text:
            messagebox.showerror("Hata", "Lütfen her iki alanı da doldurun.")
            return

        if key in questions:
            messagebox.showerror("Hata", "Bu anahtar zaten var.")
            return

        questions.append(key)
        questions_text[key] = text

        save_questions(questions, questions_text)

        messagebox.showinfo("Başarılı", f"Yeni soru eklendi:\n{key} - {text}")

        self.main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = SorBulApp(root)
    root.mainloop()
