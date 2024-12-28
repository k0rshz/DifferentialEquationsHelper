import gradio as gr
import requests

FLASK_SERVER_URL = "http://localhost:5000"

def solve_equation(equation):
    try:
        response = requests.post("http://localhost:8000/solve_equation", json={"equation": equation})
        if response.status_code == 200:
            return response.json().get("solution", "Решение не найдено.")
        else:
            return "Ошибка при решении уравнения."
    except Exception as e:
        return f"Произошла ошибка: {e}"

def upload_and_recognize(image):
    try:
        with open(image, "rb") as img_file:
            response = requests.post(f"{FLASK_SERVER_URL}/predict", files={"image": img_file})
        if response.status_code == 200:
            recognized_equation = response.json().get("prediction", "Не удалось распознать уравнение.")
            return recognized_equation
        else:
            return f"Ошибка при распознавании изображения: {response.status_code}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

def clear_textbox():
    return "", ""


custom_css = """
.gradio-container {
    background-image: url("https://i.yapx.ru/YRvZP.jpg");
    background-size: 100% auto;
    background-size: cover;
    background-position: center;
}
.gr-title {
    font-size: 2.5em; 
    font-weight: bold; 
    color: #FFFFFF; 
    text-shadow: 2px 2px 5px #000;
}

.gr-subtitle {
    font-size: 1.5em; 
    font-weight: 600; 
    color: #FFFFFF; 
    text-shadow: 1px 1px 3px #555;
}

.gr-label {
    font-size: 1.2em;
    font-weight: 500;
    color: #FFFFFF;
}
"""

with gr.Blocks(css=custom_css) as interface:
    gr.Markdown(
        "<div class='gr-title'>Помощник в решении дифференциальных уравнений</div>"
    )

    with gr.Row():
        with gr.Column():
            gr.Markdown(
                "<div class='gr-subtitle'>Загрузка изображения</div>"
            )
            image_input = gr.Image(
                label="Загрузите изображение с уравнением", type="filepath", interactive=True, elem_classes="gr-label"
            )

            recognize_button = gr.Button(
                "Распознать уравнение", elem_id="recognize-btn"
            )

        with gr.Column():
            gr.Markdown(
                "<div class='gr-subtitle'>Решение уравнения</div>"
            )
            equation_input = gr.Textbox(
                label="Уравнение", placeholder="Введите или вставьте уравнение", elem_classes="gr-label"
            )
            solution_output = gr.Textbox(
                label="Решение уравнения",
                placeholder="Здесь будет решение",
                interactive=False,
                elem_classes="gr-label",
            )

            with gr.Row():
                solve_button = gr.Button("Решить уравнение", elem_id="solve-btn")
                clear_button = gr.Button("Очистить", elem_id="clear-btn")

    recognize_button.click(
        fn=upload_and_recognize,
        inputs=image_input,
        outputs=equation_input,
        show_progress=True,
    )
    solve_button.click(
        fn=solve_equation,
        inputs=equation_input,
        outputs=solution_output,
        show_progress=True,
    )
    clear_button.click(
        fn=clear_textbox,
        inputs=[],
        outputs=[equation_input, solution_output],
    )

interface.launch(show_api=False)
