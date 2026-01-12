"""
QGIS Python Script - Backend Frameworks Pie Charts 2020-2025
22 europskych krajin - Najpopularnejsie backend technologie

Spusti v QGIS: Plugins -> Python Console -> Show Editor -> Load script -> Run
"""

from qgis.core import *
from qgis.utils import iface
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import QVariant, QSizeF

# Mapovanie nazvov vrstiev na ISO kody

LAYER_TO_ISO = {
    # Povodnych 10
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
    # Novych 11
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

# Data pre Backend frameworks (v percentach)
# Extrahovane z .md suborov pre kazdu krajinu

BACKEND_DATA = {
    2020: {
        "SK": {"Spring": 36, "Node": 14, "NET": 20, "Django": 3, "Laravel": 12},
        "CZ": {"Spring": 38, "Node": 20, "NET": 18, "Django": 8, "Laravel": 8},
        "PL": {"Spring": 30, "Node": 10, "NET": 15, "Django": 15, "Laravel": 12},
        "DE": {"Spring": 23, "Node": 14, "NET": 15, "Django": 7, "Laravel": 10},
        "AT": {"Spring": 32, "Node": 12, "NET": 23, "Django": 8, "Laravel": 12},
        "HU": {"Spring": 36, "Node": 12, "NET": 29, "Django": 5, "Laravel": 14},
        "CH": {"Spring": 28, "Node": 50, "NET": 15, "Django": 5, "Laravel": 7},
        "LU": {"Spring": 33, "Node": 13, "NET": 29, "Django": 3, "Laravel": 10},
        "DK": {"Spring": 25, "Node": 20, "NET": 18, "Django": 10, "Laravel": 8},
        "NO": {"Spring": 40, "Node": 10, "NET": 33, "Django": 8, "Laravel": 7},
        "IT": {"Spring": 25, "Node": 52, "NET": 15, "Django": 7, "Laravel": 10},
        "HR": {"Spring": 35, "Node": 15, "NET": 25, "Django": 8, "Laravel": 14},
        "PT": {"Spring": 22, "Node": 48, "NET": 15, "Django": 8, "Laravel": 18},
        "ES": {"Spring": 39, "Node": 16, "NET": 23, "Django": 5, "Laravel": 13},
        "IE": {"Spring": 30, "Node": 30, "NET": 25, "Django": 15, "Laravel": 10},
        "GB": {"Spring": 16, "Node": 40, "NET": 27, "Django": 9, "Laravel": 10},
        "FR": {"Spring": 20, "Node": 25, "NET": 10, "Django": 15, "Laravel": 20},
        "BE": {"Spring": 30, "Node": 15, "NET": 25, "Django": 10, "Laravel": 20},
        "NL": {"Spring": 37, "Node": 40, "NET": 23, "Django": 20, "Laravel": 24},
        "FI": {"Spring": 25, "Node": 20, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 30, "Node": 28, "NET": 20, "Django": 11, "Laravel": 9},
        "SI": {"Spring": 20, "Node": 30, "NET": 15, "Django": 8, "Laravel": 10},
    },
    2021: {
        "SK": {"Spring": 35, "Node": 15, "NET": 19, "Django": 4, "Laravel": 11},
        "CZ": {"Spring": 38, "Node": 20, "NET": 18, "Django": 8, "Laravel": 8},
        "PL": {"Spring": 32, "Node": 12, "NET": 15, "Django": 16, "Laravel": 12},
        "DE": {"Spring": 24, "Node": 16, "NET": 14, "Django": 8, "Laravel": 9},
        "AT": {"Spring": 30, "Node": 15, "NET": 24, "Django": 10, "Laravel": 12},
        "HU": {"Spring": 35, "Node": 13, "NET": 28, "Django": 6, "Laravel": 13},
        "CH": {"Spring": 28, "Node": 50, "NET": 12, "Django": 5, "Laravel": 7},
        "LU": {"Spring": 32, "Node": 15, "NET": 28, "Django": 4, "Laravel": 9},
        "DK": {"Spring": 25, "Node": 35, "NET": 15, "Django": 10, "Laravel": 8},
        "NO": {"Spring": 39, "Node": 9, "NET": 34, "Django": 10, "Laravel": 6},
        "IT": {"Spring": 25, "Node": 20, "NET": 15, "Django": 15, "Laravel": 10},
        "HR": {"Spring": 32, "Node": 20, "NET": 24, "Django": 10, "Laravel": 13},
        "PT": {"Spring": 24, "Node": 52, "NET": 18, "Django": 13, "Laravel": 16},
        "ES": {"Spring": 38, "Node": 17, "NET": 22, "Django": 6, "Laravel": 12},
        "IE": {"Spring": 30, "Node": 35, "NET": 25, "Django": 15, "Laravel": 10},
        "GB": {"Spring": 16, "Node": 47, "NET": 27, "Django": 9, "Laravel": 10},
        "FR": {"Spring": 20, "Node": 20, "NET": 10, "Django": 15, "Laravel": 25},
        "BE": {"Spring": 28, "Node": 18, "NET": 24, "Django": 12, "Laravel": 18},
        "NL": {"Spring": 35, "Node": 42, "NET": 25, "Django": 22, "Laravel": 22},
        "FI": {"Spring": 25, "Node": 20, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 30, "Node": 28, "NET": 20, "Django": 11, "Laravel": 9},
        "SI": {"Spring": 35, "Node": 30, "NET": 25, "Django": 15, "Laravel": 10},
    },
    2022: {
        "SK": {"Spring": 34, "Node": 16, "NET": 18, "Django": 5, "Laravel": 10},
        "CZ": {"Spring": 38, "Node": 23, "NET": 15, "Django": 10, "Laravel": 7},
        "PL": {"Spring": 32, "Node": 14, "NET": 16, "Django": 18, "Laravel": 10},
        "DE": {"Spring": 25, "Node": 17, "NET": 13, "Django": 9, "Laravel": 8},
        "AT": {"Spring": 30, "Node": 15, "NET": 24, "Django": 10, "Laravel": 12},
        "HU": {"Spring": 34, "Node": 14, "NET": 27, "Django": 7, "Laravel": 12},
        "CH": {"Spring": 28, "Node": 50, "NET": 10, "Django": 5, "Laravel": 7},
        "LU": {"Spring": 31, "Node": 16, "NET": 27, "Django": 5, "Laravel": 8},
        "DK": {"Spring": 30, "Node": 20, "NET": 25, "Django": 5, "Laravel": 3},
        "NO": {"Spring": 38, "Node": 9, "NET": 35, "Django": 12, "Laravel": 5},
        "IT": {"Spring": 25, "Node": 20, "NET": 10, "Django": 15, "Laravel": 15},
        "HR": {"Spring": 30, "Node": 22, "NET": 23, "Django": 12, "Laravel": 11},
        "PT": {"Spring": 15, "Node": 20, "NET": 25, "Django": 12, "Laravel": 10},
        "ES": {"Spring": 37, "Node": 18, "NET": 21, "Django": 7, "Laravel": 11},
        "IE": {"Spring": 30, "Node": 35, "NET": 25, "Django": 15, "Laravel": 10},
        "GB": {"Spring": 16, "Node": 47, "NET": 30, "Django": 14, "Laravel": 10},
        "FR": {"Spring": 22, "Node": 25, "NET": 10, "Django": 15, "Laravel": 18},
        "BE": {"Spring": 27, "Node": 20, "NET": 23, "Django": 14, "Laravel": 16},
        "NL": {"Spring": 35, "Node": 45, "NET": 26, "Django": 23, "Laravel": 21},
        "FI": {"Spring": 25, "Node": 25, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 30, "Node": 25, "NET": 20, "Django": 12, "Laravel": 9},
        "SI": {"Spring": 30, "Node": 35, "NET": 25, "Django": 15, "Laravel": 8},
    },
    2023: {
        "SK": {"Spring": 33, "Node": 17, "NET": 17, "Django": 6, "Laravel": 9},
        "CZ": {"Spring": 37, "Node": 25, "NET": 15, "Django": 12, "Laravel": 6},
        "PL": {"Spring": 30, "Node": 16, "NET": 18, "Django": 20, "Laravel": 8},
        "DE": {"Spring": 26, "Node": 18, "NET": 12, "Django": 10, "Laravel": 8},
        "AT": {"Spring": 28, "Node": 18, "NET": 15, "Django": 13, "Laravel": 10},
        "HU": {"Spring": 33, "Node": 15, "NET": 26, "Django": 8, "Laravel": 11},
        "CH": {"Spring": 31, "Node": 53, "NET": 10, "Django": 5, "Laravel": 5},
        "LU": {"Spring": 30, "Node": 17, "NET": 26, "Django": 6, "Laravel": 7},
        "DK": {"Spring": 20, "Node": 18, "NET": 15, "Django": 10, "Laravel": 5},
        "NO": {"Spring": 37, "Node": 8, "NET": 36, "Django": 15, "Laravel": 4},
        "IT": {"Spring": 25, "Node": 20, "NET": 15, "Django": 13, "Laravel": 15},
        "HR": {"Spring": 28, "Node": 23, "NET": 22, "Django": 13, "Laravel": 10},
        "PT": {"Spring": 14, "Node": 22, "NET": 24, "Django": 13, "Laravel": 13},
        "ES": {"Spring": 36, "Node": 19, "NET": 20, "Django": 10, "Laravel": 10},
        "IE": {"Spring": 25, "Node": 35, "NET": 20, "Django": 10, "Laravel": 8},
        "GB": {"Spring": 16, "Node": 47, "NET": 30, "Django": 14, "Laravel": 10},
        "FR": {"Spring": 20, "Node": 25, "NET": 10, "Django": 12, "Laravel": 15},
        "BE": {"Spring": 26, "Node": 22, "NET": 22, "Django": 16, "Laravel": 14},
        "NL": {"Spring": 33, "Node": 41, "NET": 27, "Django": 25, "Laravel": 20},
        "FI": {"Spring": 25, "Node": 20, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 25, "Node": 20, "NET": 15, "Django": 15, "Laravel": 8},
        "SI": {"Spring": 30, "Node": 35, "NET": 25, "Django": 20, "Laravel": 12},
    },
    2024: {
        "SK": {"Spring": 32, "Node": 18, "NET": 16, "Django": 7, "Laravel": 8},
        "CZ": {"Spring": 35, "Node": 27, "NET": 15, "Django": 13, "Laravel": 5},
        "PL": {"Spring": 28, "Node": 18, "NET": 14, "Django": 20, "Laravel": 7},
        "DE": {"Spring": 27, "Node": 20, "NET": 11, "Django": 16, "Laravel": 7},
        "AT": {"Spring": 28, "Node": 18, "NET": 24, "Django": 13, "Laravel": 8},
        "HU": {"Spring": 32, "Node": 16, "NET": 26, "Django": 9, "Laravel": 10},
        "CH": {"Spring": 30, "Node": 50, "NET": 8, "Django": 5, "Laravel": 8},
        "LU": {"Spring": 29, "Node": 18, "NET": 25, "Django": 7, "Laravel": 6},
        "DK": {"Spring": 25, "Node": 20, "NET": 18, "Django": 12, "Laravel": 8},
        "NO": {"Spring": 36, "Node": 8, "NET": 36, "Django": 18, "Laravel": 3},
        "IT": {"Spring": 27, "Node": 47, "NET": 15, "Django": 32, "Laravel": 10},
        "HR": {"Spring": 26, "Node": 24, "NET": 21, "Django": 14, "Laravel": 9},
        "PT": {"Spring": 20, "Node": 25, "NET": 30, "Django": 18, "Laravel": 12},
        "ES": {"Spring": 35, "Node": 20, "NET": 19, "Django": 9, "Laravel": 9},
        "IE": {"Spring": 25, "Node": 35, "NET": 15, "Django": 10, "Laravel": 5},
        "GB": {"Spring": 25, "Node": 35, "NET": 30, "Django": 20, "Laravel": 15},
        "FR": {"Spring": 25, "Node": 20, "NET": 15, "Django": 12, "Laravel": 10},
        "BE": {"Spring": 26, "Node": 23, "NET": 22, "Django": 17, "Laravel": 12},
        "NL": {"Spring": 32, "Node": 40, "NET": 28, "Django": 26, "Laravel": 19},
        "FI": {"Spring": 25, "Node": 20, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 30, "Node": 20, "NET": 15, "Django": 35, "Laravel": 5},
        "SI": {"Spring": 25, "Node": 40, "NET": 20, "Django": 22, "Laravel": 10},
    },
    2025: {
        "SK": {"Spring": 30, "Node": 20, "NET": 15, "Django": 8, "Laravel": 6},
        "CZ": {"Spring": 35, "Node": 25, "NET": 15, "Django": 10, "Laravel": 5},
        "PL": {"Spring": 27, "Node": 19, "NET": 13, "Django": 20, "Laravel": 6},
        "DE": {"Spring": 33, "Node": 23, "NET": 13, "Django": 17, "Laravel": 6},
        "AT": {"Spring": 28, "Node": 20, "NET": 24, "Django": 15, "Laravel": 8},
        "HU": {"Spring": 30, "Node": 15, "NET": 25, "Django": 10, "Laravel": 10},
        "CH": {"Spring": 30, "Node": 53, "NET": 8, "Django": 5, "Laravel": 3},
        "LU": {"Spring": 28, "Node": 24, "NET": 24, "Django": 8, "Laravel": 5},
        "DK": {"Spring": 25, "Node": 20, "NET": 15, "Django": 20, "Laravel": 10},
        "NO": {"Spring": 35, "Node": 8, "NET": 35, "Django": 20, "Laravel": 3},
        "IT": {"Spring": 25, "Node": 30, "NET": 15, "Django": 15, "Laravel": 10},
        "HR": {"Spring": 25, "Node": 25, "NET": 20, "Django": 15, "Laravel": 8},
        "PT": {"Spring": 22, "Node": 28, "NET": 32, "Django": 20, "Laravel": 8},
        "ES": {"Spring": 34, "Node": 22, "NET": 18, "Django": 10, "Laravel": 8},
        "IE": {"Spring": 25, "Node": 35, "NET": 15, "Django": 10, "Laravel": 5},
        "GB": {"Spring": 20, "Node": 30, "NET": 20, "Django": 15, "Laravel": 10},
        "FR": {"Spring": 25, "Node": 35, "NET": 18, "Django": 20, "Laravel": 12},
        "BE": {"Spring": 25, "Node": 24, "NET": 21, "Django": 18, "Laravel": 12},
        "NL": {"Spring": 30, "Node": 40, "NET": 28, "Django": 26, "Laravel": 18},
        "FI": {"Spring": 25, "Node": 20, "NET": 15, "Django": 10, "Laravel": 8},
        "SE": {"Spring": 23, "Node": 30, "NET": 25, "Django": 13, "Laravel": 8},
        "SI": {"Spring": 25, "Node": 30, "NET": 15, "Django": 25, "Laravel": 8},
    },
}

# Farby pre pie charty - Backend frameworks
COLORS = {
    "Spring": QColor(103, 178, 60),     # Zelena (Spring Boot green)
    "Node": QColor(104, 160, 66),       # Tmavo zelena (Node.js)
    "NET": QColor(81, 43, 212),         # Fialova (.NET purple)
    "Django": QColor(12, 75, 51),       # Tmavo zelena (Django)
    "Laravel": QColor(255, 45, 32),     # Cervena (Laravel red)
}

FRAMEWORKS = ["Spring", "Node", "NET", "Django", "Laravel"]

# STYLING FARBY
COUNTRY_FILL_COLOR = '#F0F8FF'      # Velmi jemna modra (Alice Blue - skoro biela)
COUNTRY_OUTLINE_COLOR = '#1E3A5F'   # Tmavomodra pre hranice
BACKGROUND_COLOR = '#FFFFFF'         # Biela pre pozadie


def style_base_layers():
    """Nastavi farby pre povodne vrstvy krajin"""
    print("Nastavujem styly pre vrstvy krajin...")

    for layer in QgsProject.instance().mapLayers().values():
        if layer.name() in LAYER_TO_ISO:
            symbol = QgsFillSymbol.createSimple({
                'color': COUNTRY_FILL_COLOR,
                'outline_color': COUNTRY_OUTLINE_COLOR,
                'outline_width': '0.5'
            })
            layer.renderer().setSymbol(symbol)
            layer.triggerRepaint()

    print("  Styly nastavene")


def set_background_color():
    """Nastavi biele pozadie projektu"""
    print("Nastavujem pozadie projektu...")

    QgsProject.instance().setBackgroundColor(QColor(BACKGROUND_COLOR))

    print("  Pozadie nastavene na bielu")


def create_layer_for_year(year):
    """Vytvori novu vrstvu pre dany rok so vsetkymi datami"""
    print(f"Vytvarame vrstvu pre rok {year}...")

    # Najdi prvu vrstvu pre CRS
    first_layer = None
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name() in LAYER_TO_ISO:
            first_layer = layer
            break

    if not first_layer:
        print("  Nenasiel som ziadne _adm0 vrstvy!")
        return None

    crs = first_layer.crs().authid()

    # Vytvor memory layer s poliami
    fields_def = "field=ISO_A2:string"
    for fw in FRAMEWORKS:
        fields_def += f"&field={fw}:integer"

    uri = f"Polygon?crs={crs}&{fields_def}"
    new_layer = QgsVectorLayer(uri, f"Backend_{year}", "memory")

    if not new_layer.isValid():
        print(f"  Nepodarilo sa vytvorit vrstvu pre {year}")
        return None

    dp = new_layer.dataProvider()
    year_data = BACKEND_DATA[year]

    countries_added = 0

    # Pridaj features z kazdej krajiny
    for layer in QgsProject.instance().mapLayers().values():
        layer_name = layer.name()
        if layer_name not in LAYER_TO_ISO:
            continue

        iso_code = LAYER_TO_ISO[layer_name]

        for feature in layer.getFeatures():
            new_feat = QgsFeature(new_layer.fields())
            new_feat.setGeometry(feature.geometry())

            # Ak mame data pre tuto krajinu
            if iso_code in year_data:
                country_data = year_data[iso_code]
                attrs = [iso_code]
                for fw in FRAMEWORKS:
                    attrs.append(country_data.get(fw, 0))
            else:
                # Nemame data - nulove hodnoty
                attrs = [iso_code, 0, 0, 0, 0, 0]

            new_feat.setAttributes(attrs)
            dp.addFeature(new_feat)
            countries_added += 1

    new_layer.updateExtents()

    # Nastav styl pre novu vrstvu
    symbol = QgsFillSymbol.createSimple({
        'color': COUNTRY_FILL_COLOR,
        'outline_color': COUNTRY_OUTLINE_COLOR,
        'outline_width': '0.5'
    })
    new_layer.renderer().setSymbol(symbol)

    print(f"  Pridanych {countries_added} krajin")

    return new_layer


def setup_pie_chart(layer, year):
    """Nastavi pie chart pre vrstvu"""

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

    # Kategorie
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

    print(f"  Pie chart nastaveny")


def main():
    print("=" * 60)
    print("Backend Frameworks Pie Charts Generator")
    print("22 krajin - Spring, Node.js, .NET, Django, Laravel")
    print("=" * 60)

    # Nastav pozadie
    set_background_color()

    # Nastav styly pre povodne vrstvy
    style_base_layers()

    # Zisti kolko vrstiev mame
    available_layers = []
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name() in LAYER_TO_ISO:
            available_layers.append(layer.name())

    print(f"Najdenych {len(available_layers)} krajin")
    print("-" * 60)

    # Vytvor skupinu pre backend vrstvy
    root = QgsProject.instance().layerTreeRoot()
    backend_group = root.insertGroup(0, "backend_technologies")
    print("Vytvorena skupina: backend_technologies")

    # Vytvor vrstvy pre kazdy rok
    for year in [2020, 2021, 2022, 2023, 2024, 2025]:
        layer = create_layer_for_year(year)
        if layer:
            setup_pie_chart(layer, year)
            # Pridaj vrstvu do projektu
            QgsProject.instance().addMapLayer(layer, False)
            # Pridaj do skupiny
            backend_group.addLayer(layer)
            print(f"Hotova vrstva: Backend_{year}")
        print("-" * 40)

    print("=" * 60)
    print("HOTOVO!")
    print("")
    print("STRUKTURA:")
    print("  backend_technologies/")
    print("     Backend_2020")
    print("     Backend_2021")
    print("     Backend_2022")
    print("     Backend_2023")
    print("     Backend_2024")
    print("     Backend_2025")
    print("")
    print("FARBY:")
    print("  Spring Boot: #67B23C (Zelena)")
    print("  Node.js:     #68A042 (Tmavo zelena)")
    print("  .NET:        #512BD4 (Fialova)")
    print("  Django:      #0C4B33 (Tmavo zelena)")
    print("  Laravel:     #FF2D20 (Cervena)")
    print("")
    print("22 krajin: SK, CZ, PL, DE, AT, HU, CH, LU, DK, NO,")
    print("           IT, HR, PT, ES, IE, GB, FR, BE, NL, FI, SE, SI")
    print("")
    print("TRENDY 2020-2025:")
    print("  - Spring Boot: Stabilny 25-35% v CEE, klesa v zapadnej EU")
    print("  - Node.js: Silny rast, az 50% v CH, NL, PT")
    print("  - .NET: Enterprise standard 15-30%")
    print("  - Django/Python: Prudky rast 2024-2025 (AI/ML boom)")
    print("  - Laravel: Klesa <15% (legacy)")
    print("")
    print("Prepinaj viditelnost vrstiev Backend_2020 - Backend_2025")
    print("=" * 60)

    iface.mapCanvas().refresh()


main()
