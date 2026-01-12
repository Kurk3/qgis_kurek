"""
QGIS Python Script - Frontend Frameworks Pie Charts 2020-2025
COMPLETE VERSION - 21 európskych krajín + STYLING

Spusti v QGIS: Plugins -> Python Console -> Show Editor -> Load script -> Run
"""

from qgis.core import *
from qgis.utils import iface
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import QVariant, QSizeF

# Mapovanie názvov vrstiev na ISO kódy

LAYER_TO_ISO = {
# Pôvodných 10
"SVK_adm0": "SK",
"CZE_adm0": "CZ",
"POL_adm0": "PL",
"DEU_adm0": "DE",
"AUT_adm0": "AT",
"HUN_adm0": "HU",
"CHE_adm0": "CH",
"LUX_adm0": "LU",
"DNK_adm0": "DK",
"NOR_adm0": "NO",
# Nových 11
"ITA_adm0": "IT",
"HRV_adm0": "HR",
"PRT_adm0": "PT",
"ESP_adm0": "ES",
"IRL_adm0": "IE",
"GBR_adm0": "GB",
"FRA_adm0": "FR",
"BEL_adm0": "BE",
"NLD_adm0": "NL",
"FIN_adm0": "FI",
"SWE_adm0": "SE",
# Slovinsko
"SVN_adm0": "SI",
}

# Dáta pre frontend frameworks (v percentách)

FRONTEND_DATA = {
2020: {
"SK": {"React": 27, "Angular": 28, "Vue": 12, "TypeScript": 0, "Svelte": 0},
"CZ": {"React": 39, "Angular": 45, "Vue": 11, "TypeScript": 0, "Svelte": 2},
"PL": {"React": 40, "Angular": 24, "Vue": 17, "TypeScript": 0, "Svelte": 9},
"AT": {"React": 38, "Angular": 25, "Vue": 17, "TypeScript": 14, "Svelte": 0},
"HU": {"React": 38, "Angular": 43, "Vue": 12, "TypeScript": 33, "Svelte": 0},
"DE": {"React": 46, "Angular": 39, "Vue": 9, "TypeScript": 0, "Svelte": 0},
"CH": {"React": 38, "Angular": 43, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 31, "Angular": 29, "Vue": 12, "TypeScript": 0, "Svelte": 0},
"DK": {"React": 38, "Angular": 23, "Vue": 17, "TypeScript": 0, "Svelte": 4},
"NO": {"React": 45, "Angular": 34, "Vue": 12, "TypeScript": 25, "Svelte": 0},
"IT": {"React": 36, "Angular": 25, "Vue": 17, "TypeScript": 0, "Svelte": 2},
"HR": {"React": 35, "Angular": 38, "Vue": 18, "TypeScript": 43, "Svelte": 0},
"PT": {"React": 38, "Angular": 26, "Vue": 18, "TypeScript": 0, "Svelte": 0},
"ES": {"React": 25, "Angular": 51, "Vue": 12, "TypeScript": 0, "Svelte": 0},
"IE": {"React": 38, "Angular": 33, "Vue": 7, "TypeScript": 25, "Svelte": 0},
"GB": {"React": 36, "Angular": 25, "Vue": 17, "TypeScript": 20, "Svelte": 0},
"FR": {"React": 38, "Angular": 25, "Vue": 17, "TypeScript": 0, "Svelte": 0},
"BE": {"React": 33, "Angular": 38, "Vue": 8, "TypeScript": 0, "Svelte": 0},
"NL": {"React": 36, "Angular": 25, "Vue": 17, "TypeScript": 0, "Svelte": 0},
"FI": {"React": 35, "Angular": 25, "Vue": 17, "TypeScript": 20, "Svelte": 0},
"SE": {"React": 38, "Angular": 23, "Vue": 17, "TypeScript": 0, "Svelte": 3},
"SI": {"React": 40, "Angular": 23, "Vue": 10, "TypeScript": 0, "Svelte": 0},
},
2021: {
"SK": {"React": 31, "Angular": 26, "Vue": 14, "TypeScript": 0, "Svelte": 0},
"CZ": {"React": 41, "Angular": 41, "Vue": 14, "TypeScript": 0, "Svelte": 2},
"PL": {"React": 42, "Angular": 22, "Vue": 19, "TypeScript": 0, "Svelte": 4},
"AT": {"React": 40, "Angular": 22, "Vue": 18, "TypeScript": 14, "Svelte": 0},
"HU": {"React": 40, "Angular": 40, "Vue": 13, "TypeScript": 38, "Svelte": 0},
"DE": {"React": 50, "Angular": 38, "Vue": 10, "TypeScript": 0, "Svelte": 2},
"CH": {"React": 38, "Angular": 43, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 34, "Angular": 26, "Vue": 14, "TypeScript": 21, "Svelte": 0},
"DK": {"React": 43, "Angular": 23, "Vue": 13, "TypeScript": 0, "Svelte": 7},
"NO": {"React": 50, "Angular": 32, "Vue": 11, "TypeScript": 35, "Svelte": 0},
"IT": {"React": 50, "Angular": 35, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"HR": {"React": 39, "Angular": 26, "Vue": 19, "TypeScript": 53, "Svelte": 0},
"PT": {"React": 43, "Angular": 24, "Vue": 21, "TypeScript": 0, "Svelte": 4},
"ES": {"React": 27, "Angular": 49, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"IE": {"React": 40, "Angular": 30, "Vue": 8, "TypeScript": 30, "Svelte": 0},
"GB": {"React": 40, "Angular": 25, "Vue": 17, "TypeScript": 30, "Svelte": 0},
"FR": {"React": 40, "Angular": 22, "Vue": 19, "TypeScript": 28, "Svelte": 0},
"BE": {"React": 38, "Angular": 33, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"NL": {"React": 40, "Angular": 23, "Vue": 19, "TypeScript": 31, "Svelte": 0},
"FI": {"React": 40, "Angular": 23, "Vue": 19, "TypeScript": 30, "Svelte": 0},
"SE": {"React": 41, "Angular": 24, "Vue": 19, "TypeScript": 0, "Svelte": 3},
"SI": {"React": 43, "Angular": 33, "Vue": 18, "TypeScript": 28, "Svelte": 0},
},
2022: {
"SK": {"React": 33, "Angular": 25, "Vue": 15, "TypeScript": 0, "Svelte": 2},
"CZ": {"React": 45, "Angular": 39, "Vue": 14, "TypeScript": 0, "Svelte": 2},
"PL": {"React": 44, "Angular": 22, "Vue": 20, "TypeScript": 0, "Svelte": 5},
"AT": {"React": 40, "Angular": 22, "Vue": 18, "TypeScript": 10, "Svelte": 3},
"HU": {"React": 45, "Angular": 38, "Vue": 13, "TypeScript": 43, "Svelte": 0},
"DE": {"React": 52, "Angular": 36, "Vue": 11, "TypeScript": 0, "Svelte": 2},
"CH": {"React": 38, "Angular": 43, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 36, "Angular": 25, "Vue": 16, "TypeScript": 25, "Svelte": 0},
"DK": {"React": 55, "Angular": 35, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"NO": {"React": 55, "Angular": 30, "Vue": 10, "TypeScript": 43, "Svelte": 0},
"IT": {"React": 45, "Angular": 40, "Vue": 10, "TypeScript": 0, "Svelte": 3},
"HR": {"React": 41, "Angular": 25, "Vue": 18, "TypeScript": 63, "Svelte": 0},
"PT": {"React": 38, "Angular": 14, "Vue": 12, "TypeScript": 0, "Svelte": 0},
"ES": {"React": 29, "Angular": 47, "Vue": 15, "TypeScript": 21, "Svelte": 0},
"IE": {"React": 45, "Angular": 30, "Vue": 10, "TypeScript": 40, "Svelte": 0},
"GB": {"React": 44, "Angular": 21, "Vue": 19, "TypeScript": 35, "Svelte": 0},
"FR": {"React": 41, "Angular": 20, "Vue": 17, "TypeScript": 33, "Svelte": 0},
"BE": {"React": 43, "Angular": 28, "Vue": 18, "TypeScript": 23, "Svelte": 0},
"NL": {"React": 43, "Angular": 21, "Vue": 19, "TypeScript": 35, "Svelte": 0},
"FI": {"React": 42, "Angular": 20, "Vue": 19, "TypeScript": 40, "Svelte": 0},
"SE": {"React": 43, "Angular": 23, "Vue": 13, "TypeScript": 0, "Svelte": 0},
"SI": {"React": 44, "Angular": 23, "Vue": 20, "TypeScript": 28, "Svelte": 5},
},
2023: {
"SK": {"React": 34, "Angular": 23, "Vue": 16, "TypeScript": 23, "Svelte": 0},
"CZ": {"React": 49, "Angular": 37, "Vue": 11, "TypeScript": 0, "Svelte": 2},
"PL": {"React": 42, "Angular": 19, "Vue": 18, "TypeScript": 0, "Svelte": 7},
"AT": {"React": 40, "Angular": 20, "Vue": 17, "TypeScript": 13, "Svelte": 6},
"HU": {"React": 47, "Angular": 36, "Vue": 14, "TypeScript": 48, "Svelte": 0},
"DE": {"React": 54, "Angular": 36, "Vue": 11, "TypeScript": 0, "Svelte": 3},
"CH": {"React": 43, "Angular": 45, "Vue": 17, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 37, "Angular": 24, "Vue": 15, "TypeScript": 28, "Svelte": 0},
"DK": {"React": 43, "Angular": 18, "Vue": 14, "TypeScript": 0, "Svelte": 6},
"NO": {"React": 60, "Angular": 28, "Vue": 9, "TypeScript": 50, "Svelte": 0},
"IT": {"React": 45, "Angular": 40, "Vue": 13, "TypeScript": 0, "Svelte": 6},
"HR": {"React": 41, "Angular": 23, "Vue": 17, "TypeScript": 68, "Svelte": 3},
"PT": {"React": 40, "Angular": 15, "Vue": 16, "TypeScript": 0, "Svelte": 6},
"ES": {"React": 31, "Angular": 45, "Vue": 16, "TypeScript": 25, "Svelte": 0},
"IE": {"React": 50, "Angular": 28, "Vue": 10, "TypeScript": 43, "Svelte": 0},
"GB": {"React": 41, "Angular": 17, "Vue": 16, "TypeScript": 0, "Svelte": 7},
"FR": {"React": 43, "Angular": 23, "Vue": 18, "TypeScript": 33, "Svelte": 3},
"BE": {"React": 45, "Angular": 23, "Vue": 23, "TypeScript": 28, "Svelte": 0},
"NL": {"React": 41, "Angular": 18, "Vue": 17, "TypeScript": 38, "Svelte": 0},
"FI": {"React": 73, "Angular": 20, "Vue": 7, "TypeScript": 60, "Svelte": 0},
"SE": {"React": 43, "Angular": 20, "Vue": 14, "TypeScript": 0, "Svelte": 3},
"SI": {"React": 45, "Angular": 24, "Vue": 13, "TypeScript": 35, "Svelte": 6},
},
2024: {
"SK": {"React": 36, "Angular": 22, "Vue": 15, "TypeScript": 25, "Svelte": 3},
"CZ": {"React": 52, "Angular": 35, "Vue": 10, "TypeScript": 0, "Svelte": 2},
"PL": {"React": 40, "Angular": 18, "Vue": 17, "TypeScript": 0, "Svelte": 8},
"AT": {"React": 38, "Angular": 20, "Vue": 16, "TypeScript": 13, "Svelte": 6},
"HU": {"React": 49, "Angular": 35, "Vue": 14, "TypeScript": 52, "Svelte": 2},
"DE": {"React": 57, "Angular": 34, "Vue": 10, "TypeScript": 0, "Svelte": 3},
"CH": {"React": 38, "Angular": 45, "Vue": 10, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 38, "Angular": 23, "Vue": 14, "TypeScript": 31, "Svelte": 4},
"DK": {"React": 40, "Angular": 18, "Vue": 13, "TypeScript": 0, "Svelte": 10},
"NO": {"React": 63, "Angular": 26, "Vue": 8, "TypeScript": 55, "Svelte": 2},
"IT": {"React": 55, "Angular": 35, "Vue": 10, "TypeScript": 0, "Svelte": 0},
"HR": {"React": 38, "Angular": 19, "Vue": 16, "TypeScript": 71, "Svelte": 4},
"PT": {"React": 39, "Angular": 22, "Vue": 13, "TypeScript": 43, "Svelte": 0},
"ES": {"React": 33, "Angular": 43, "Vue": 17, "TypeScript": 28, "Svelte": 0},
"IE": {"React": 55, "Angular": 23, "Vue": 8, "TypeScript": 45, "Svelte": 0},
"GB": {"React": 43, "Angular": 23, "Vue": 10, "TypeScript": 65, "Svelte": 3},
"FR": {"React": 38, "Angular": 18, "Vue": 14, "TypeScript": 33, "Svelte": 4},
"BE": {"React": 48, "Angular": 39, "Vue": 23, "TypeScript": 23, "Svelte": 0},
"NL": {"React": 40, "Angular": 17, "Vue": 15, "TypeScript": 39, "Svelte": 0},
"FI": {"React": 73, "Angular": 20, "Vue": 7, "TypeScript": 70, "Svelte": 0},
"SE": {"React": 62, "Angular": 20, "Vue": 8, "TypeScript": 60, "Svelte": 4},
"SI": {"React": 39, "Angular": 18, "Vue": 15, "TypeScript": 38, "Svelte": 8},
},
2025: {
"SK": {"React": 38, "Angular": 20, "Vue": 14, "TypeScript": 28, "Svelte": 4},
"CZ": {"React": 53, "Angular": 33, "Vue": 11, "TypeScript": 0, "Svelte": 3},
"PL": {"React": 40, "Angular": 17, "Vue": 16, "TypeScript": 0, "Svelte": 9},
"AT": {"React": 38, "Angular": 19, "Vue": 16, "TypeScript": 14, "Svelte": 7},
"HU": {"React": 51, "Angular": 34, "Vue": 14, "TypeScript": 55, "Svelte": 3},
"DE": {"React": 55, "Angular": 35, "Vue": 10, "TypeScript": 0, "Svelte": 3},
"CH": {"React": 38, "Angular": 45, "Vue": 10, "TypeScript": 0, "Svelte": 0},
"LU": {"React": 39, "Angular": 24, "Vue": 13, "TypeScript": 33, "Svelte": 5},
"DK": {"React": 40, "Angular": 18, "Vue": 15, "TypeScript": 0, "Svelte": 7},
"NO": {"React": 65, "Angular": 24, "Vue": 7, "TypeScript": 60, "Svelte": 2},
"IT": {"React": 48, "Angular": 38, "Vue": 10, "TypeScript": 0, "Svelte": 6},
"HR": {"React": 38, "Angular": 18, "Vue": 15, "TypeScript": 73, "Svelte": 4},
"PT": {"React": 42, "Angular": 19, "Vue": 15, "TypeScript": 49, "Svelte": 0},
"ES": {"React": 35, "Angular": 41, "Vue": 18, "TypeScript": 31, "Svelte": 5},
"IE": {"React": 55, "Angular": 23, "Vue": 8, "TypeScript": 45, "Svelte": 3},
"GB": {"React": 43, "Angular": 18, "Vue": 10, "TypeScript": 65, "Svelte": 3},
"FR": {"React": 39, "Angular": 23, "Vue": 10, "TypeScript": 38, "Svelte": 3},
"BE": {"React": 43, "Angular": 23, "Vue": 28, "TypeScript": 33, "Svelte": 0},
"NL": {"React": 40, "Angular": 18, "Vue": 16, "TypeScript": 39, "Svelte": 0},
"FI": {"React": 73, "Angular": 19, "Vue": 7, "TypeScript": 80, "Svelte": 0},
"SE": {"React": 63, "Angular": 23, "Vue": 10, "TypeScript": 65, "Svelte": 4},
"SI": {"React": 35, "Angular": 23, "Vue": 18, "TypeScript": 30, "Svelte": 0},
},
}

# Farby pre pie charty

COLORS = {
"React": QColor(33, 150, 243),      # modrá
"Angular": QColor(221, 0, 49),       # červená
"Vue": QColor(66, 184, 131),         # zelená
"TypeScript": QColor(49, 120, 198),  # tmavo modrá
"Svelte": QColor(255, 62, 0),        # oranžová
}

FRAMEWORKS = ["React", "Angular", "Vue", "TypeScript", "Svelte"]

# STYLING FARBY

COUNTRY_FILL_COLOR = '#F0F8FF'      # Veľmi jemná modrá (Alice Blue - skoro biela)
COUNTRY_OUTLINE_COLOR = '#1E3A5F'   # Tmavomodrá pre hranice
BACKGROUND_COLOR = '#FFFFFF'         # Biela pre pozadie

def style_base_layers():
"""Nastaví farby pre pôvodné vrstvy krajín"""
print("Nastavujem štýly pre vrstvy krajín...")

```
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() in LAYER_TO_ISO:
        symbol = QgsFillSymbol.createSimple({
            'color': COUNTRY_FILL_COLOR,
            'outline_color': COUNTRY_OUTLINE_COLOR,
            'outline_width': '0.5'
        })
        layer.renderer().setSymbol(symbol)
        layer.triggerRepaint()

print("  ✓ Štýly nastavené")

```

def set_background_color():
"""Nastaví biele pozadie projektu"""
print("Nastavujem pozadie projektu...")

```
QgsProject.instance().setBackgroundColor(QColor(BACKGROUND_COLOR))

print("  ✓ Pozadie nastavené na bielu")

```

def create_layer_for_year(year):
"""Vytvorí novú vrstvu pre daný rok so všetkými dátami"""
print(f"Vytváram vrstvu pre rok {year}...")

```
# Nájdi prvú vrstvu pre CRS
first_layer = None
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() in LAYER_TO_ISO:
        first_layer = layer
        break

if not first_layer:
    print("❌ Nenašiel som žiadne _adm0 vrstvy!")
    return None

crs = first_layer.crs().authid()

# Vytvor memory layer s poliami
fields_def = "field=ISO_A2:string"
for fw in FRAMEWORKS:
    fields_def += f"&field={fw}:integer"

uri = f"Polygon?crs={crs}&{fields_def}"
new_layer = QgsVectorLayer(uri, f"Frontend_{year}", "memory")

if not new_layer.isValid():
    print(f"❌ Nepodarilo sa vytvoriť vrstvu pre {year}")
    return None

dp = new_layer.dataProvider()
year_data = FRONTEND_DATA[year]

countries_added = 0

# Pridaj features z každej krajiny
for layer in QgsProject.instance().mapLayers().values():
    layer_name = layer.name()
    if layer_name not in LAYER_TO_ISO:
        continue

    iso_code = LAYER_TO_ISO[layer_name]

    for feature in layer.getFeatures():
        new_feat = QgsFeature(new_layer.fields())
        new_feat.setGeometry(feature.geometry())

        # Ak máme dáta pre túto krajinu
        if iso_code in year_data:
            country_data = year_data[iso_code]
            attrs = [iso_code]
            for fw in FRAMEWORKS:
                attrs.append(country_data.get(fw, 0))
        else:
            # Nemáme dáta - nulové hodnoty
            attrs = [iso_code, 0, 0, 0, 0, 0]

        new_feat.setAttributes(attrs)
        dp.addFeature(new_feat)
        countries_added += 1

new_layer.updateExtents()

# Nastav štýl pre novú vrstvu
symbol = QgsFillSymbol.createSimple({
    'color': COUNTRY_FILL_COLOR,
    'outline_color': COUNTRY_OUTLINE_COLOR,
    'outline_width': '0.5'
})
new_layer.renderer().setSymbol(symbol)

print(f"  ✓ Pridaných {countries_added} krajín")

return new_layer

```

def setup_pie_chart(layer, year):
"""Nastaví pie chart pre vrstvu"""

```
# Diagram settings
ds = QgsDiagramSettings()
ds.enabled = True
ds.font = QFont("Arial", 8)
ds.size = QSizeF(20, 20)
ds.sizeType = QgsUnitTypes.RenderMillimeters
ds.rotationOffset = 270
ds.minimumSize = 0
ds.opacity = 1.0
ds.penWidth = 0.5
ds.penColor = QColor(0, 0, 0)
ds.scaleByArea = True

# Kategórie
ds.categoryAttributes = FRAMEWORKS.copy()
ds.categoryColors = [COLORS[fw] for fw in FRAMEWORKS]
ds.categoryLabels = FRAMEWORKS.copy()

# Renderer
diagram = QgsPieDiagram()
renderer = QgsSingleCategoryDiagramRenderer()
renderer.setDiagram(diagram)
renderer.setDiagramSettings(ds)

# Placement
dls = QgsDiagramLayerSettings()
dls.placement = QgsDiagramLayerSettings.OverPoint
dls.showAllDiagrams = True
dls.priority = 5

# Aplikuj
layer.setDiagramRenderer(renderer)
layer.setDiagramLayerSettings(dls)

print(f"  ✓ Pie chart nastavený")

```

def main():
print("=" * 60)
print("Frontend Frameworks Pie Charts Generator")
print("COMPLETE VERSION - 22 krajín + STYLING")
print("=" * 60)

```
# Nastav pozadie
set_background_color()

# Nastav štýly pre pôvodné vrstvy
style_base_layers()

# Zisti koľko vrstiev máme
available_layers = []
for layer in QgsProject.instance().mapLayers().values():
    if layer.name() in LAYER_TO_ISO:
        available_layers.append(layer.name())

print(f"Nájdených {len(available_layers)} krajín")
print("-" * 60)

# Vytvor skupinu pre frontend vrstvy
root = QgsProject.instance().layerTreeRoot()
frontend_group = root.insertGroup(0, "frontend_technologies")
print("✓ Vytvorená skupina: frontend_technologies")

# Vytvor vrstvy pre každý rok
for year in [2020, 2021, 2022, 2023, 2024, 2025]:
    layer = create_layer_for_year(year)
    if layer:
        setup_pie_chart(layer, year)
        # Pridaj vrstvu do projektu
        QgsProject.instance().addMapLayer(layer, False)
        # Pridaj do skupiny
        frontend_group.addLayer(layer)
        print(f"✓ Hotová vrstva: Frontend_{year}")
    print("-" * 40)

print("=" * 60)
print("✓ HOTOVO!")
print("")
print("ŠTRUKTÚRA:")
print("  📁 frontend_technologies/")
print("     ├── Frontend_2020")
print("     ├── Frontend_2021")
print("     ├── Frontend_2022")
print("     ├── Frontend_2023")
print("     ├── Frontend_2024")
print("     └── Frontend_2025")
print("")
print("FARBY:")
print(f"  Krajiny: {COUNTRY_FILL_COLOR} (jemná modrá)")
print(f"  Hranice: {COUNTRY_OUTLINE_COLOR} (tmavomodrá)")
print(f"  Pozadie: {BACKGROUND_COLOR} (biela)")
print("")
print("22 krajín: SK, CZ, PL, DE, AT, HU, CH, LU, DK, NO,")
print("           IT, HR, PT, ES, IE, GB, FR, BE, NL, FI, SE, SI")
print("")
print("Prepínaj viditeľnosť vrstiev Frontend_2020 - Frontend_2025")
print("=" * 60)

iface.mapCanvas().refresh()

```

main()