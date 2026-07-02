import flet as ft
from datetime import date

def main(page: ft.Page):
    page.title = "Neptune-Haumea-Eris Radar"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    def run_usm_engine(birth_date):
        homo_k, eris_k, neptune_k, tolerance = 6.18, 9.3, 10.77, 0.3
        results = []
        
        for i in range(1, 85):
            homo_dev = abs((i / homo_k) - round(i / homo_k))
            eris_dev = abs((i / eris_k) - round(i / eris_k))
            neptune_dev = abs((i / neptune_k) - round(i / neptune_k))
            
            status = "CRITICAL" if (homo_dev <= tolerance and eris_dev <= tolerance and neptune_dev <= tolerance) else "Normal"
            
            offset_day = int(eris_dev * 30)
            offset_month = int(homo_dev * 12)
            
            new_day = birth_date.day + offset_day
            new_month = birth_date.month + offset_month
            new_year = birth_date.year + i
            
            while new_day > 30:
                new_day -= 30
                new_month += 1
            while new_month > 12:
                new_month -= 12
                new_year += 1
            
            results.append({
                "date": f"{new_year}-{new_month:02d}-{new_day:02d}",
                "age": i,
                "status": status
            })
        return results

    # UI Elements
    date_picker = ft.DatePicker(first_date=date(1900, 1, 1), last_date=date(2099, 12, 31))
    page.overlay.append(date_picker)
    
    date_button = ft.ElevatedButton("Select Birth Date", icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: date_picker.pick_date())
    result_column = ft.Column()

    def execute_analysis(e):
        if date_picker.value:
            data = run_usm_engine(date_picker.value)
            result_column.controls.clear()
            for row in data:
                color = ft.colors.RED_400 if row["status"] == "CRITICAL" else ft.colors.GREEN_400
                result_column.controls.append(
                    ft.Container(
                        ft.Text(f"Year {row['age']}: {row['date']} -> {row['status']}", color="white"),
                        bgcolor=color, padding=10, border_radius=5, margin=2
                    )
                )
            page.update()

    page.add(
        ft.Text("Neptune-Haumea-Eris Radar", size=20, weight="bold"),
        date_button,
        ft.ElevatedButton("Execute Analysis", on_click=execute_analysis),
        result_column
    )

ft.app(target=main)
