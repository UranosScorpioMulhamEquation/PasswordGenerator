import flet as ft

def generate_password(machine_id_hex):
    """
    نفس المعادلة حقتك بالضبط
    """
    if not machine_id_hex or not machine_id_hex.strip():
        return "Error", "Machine ID فاضي"

    machine_id_hex = machine_id_hex.strip()
    
    try:
        digits = ''.join(filter(str.isdigit, machine_id_hex))
        if not digits: 
            digits = str(int(machine_id_hex, 16))
            
        num = int(digits)
        result = round(abs(num / 2 * 3.14))
        return str(result)[:6], None # نجاح

    except ValueError:
        return "Error", "Machine ID غير صحيح: لازم يكون Hex او ارقام"
    except Exception as e:
        return "Error", f"خطأ غير متوقع: {e}"

def main(page: ft.Page):
    page.title = "Password Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    machine_id_input = ft.TextField(
        label="Paste Machine ID", 
        width=300,
        hint_text="Hex or numbers only"
    )
    result_text = ft.Text(value="", size=20, weight="bold")

    def button_clicked(e):
        password, error_msg = generate_password(machine_id_input.value)
        if error_msg:
            result_text.value = f"[خطأ] {error_msg}"
            result_text.color = "red"
        else:
            result_text.value = f"[تم] Activation Password: {password}"
            result_text.color = "blue"
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Password Generator Tool v2.0", size=24, weight="bold"),
                machine_id_input,
                ft.ElevatedButton("Generate", on_click=button_clicked, width=300),
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)