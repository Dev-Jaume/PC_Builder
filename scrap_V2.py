from classes import scrap_price, append_list_as_row
from datetime import datetime
from csv import writer

now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

cpu_preu, cpu_disponible = scrap_price("https://www.pccomponentes.com/amd-ryzen-9-5900x-37-ghz")
torre_preu, torre_disponible = scrap_price("https://www.pccomponentes.com/nzxt-h710i-cristal-templado-usb-31-rgb-blanco-mate")
placa_base_preu, placa_base_disponible = scrap_price("https://www.pccomponentes.com/gigabyte-x570-aorus-pro")
font_alimentacio_preu, font_alimentacio_disponible = scrap_price("https://www.pccomponentes.com/seasonic-prime-850w-80-plus-titanium-modular")
grafica_preu, grafica_disponible = scrap_price("https://www.pccomponentes.com/msi-geforce-rtx-3080-ventus-3x-oc-10gb-gddr6x")
refrigeracio_preu, refrigeracio_disponible = scrap_price("https://www.pccomponentes.com/corsair-h100i-rgb-platinum-kit-de-refrigeracion-liquida")
ram_preu, ram_disponible = scrap_price("https://www.pccomponentes.com/team-group-t-force-night-hawk-rgb-ddr4-3600-pc4-28000-16gb-2x8-cl18")
disc_dur_preu, disc_dur_disponible = scrap_price("https://www.pccomponentes.com/samsung-970-evo-plus-1tb-ssd-nvme-m2")

row_cpu = ['CPU', cpu_preu, cpu_disponible, dt_string]
row_torre = ['Torre', torre_preu, torre_disponible, dt_string]
row_placa_base = ['Placa_base', placa_base_preu, placa_base_disponible, dt_string]
row_font_alimentacio = ['Font_alimentació', font_alimentacio_preu, font_alimentacio_disponible, dt_string]
row_grafica = ['Targeta_gràfica', grafica_preu, grafica_disponible, dt_string]
row_refrigeracio = ['Refrigeració', refrigeracio_preu, refrigeracio_disponible, dt_string]
row_ram = ['RAM', ram_preu, ram_disponible, dt_string]
row_disc_dur = ['SSD', disc_dur_preu, disc_dur_disponible, dt_string]

llista_peces = [row_cpu, row_torre, row_placa_base, row_font_alimentacio, row_grafica, row_refrigeracio, row_ram, row_disc_dur]

for i in llista_peces:
    append_list_as_row('./dataset/PC_parts_price.csv', i)

