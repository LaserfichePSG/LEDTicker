class Led_Config:
    def __init__(self):
            self.board_length = 300,
            self.board_height = 5,
            self.strip_options = {"led_pin": 18, "led_frequency": 800000, "led_dma": 5, "led_invert": False, "led_brightness": 150},
            self.display_count = 5,
            self.scroll_buffer = 0.1