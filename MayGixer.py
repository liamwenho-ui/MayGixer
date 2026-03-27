import flet as ft

def main(page: ft.Page):
    page.title = "RGB Color Mixer"

    
    rgb_text = ft.Text(value="RGB(0, 0, 0)", size=20)

   
    def update_color(e):
        r = int(red_slider.value)
        g = int(green_slider.value)
        b = int(blue_slider.value)

       
        color = f"#{r:02x}{g:02x}{b:02x}"

    
        page.bgcolor = color

        
        rgb_text.value = f"RGB({r}, {g}, {b})"

        page.update()

   
    red_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
    green_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
    blue_slider = ft.Slider(min=0, max=255, value=0, on_change=update_color)
    page.theme_mode = "Light"

    

    
    page.add(
        ft.Text("Red"),
        red_slider,
        ft.Text("Green"),
        green_slider,
        ft.Text("Blue"),
        blue_slider,
        rgb_text
        
    )

ft.app(target=main)