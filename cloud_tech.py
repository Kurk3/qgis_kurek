"""
QGIS Python Script - Cloud Technologies Pie Charts 2020-2025
22 europskych krajin - Najpopularnejsie cloud technologie

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

# Data pre Cloud technologies (v percentach)
# Extrahovane z .md suborov pre kazdu krajinu
# TOP 5: AWS, Azure, Docker, Kubernetes, GCP

CLOUD_DATA = {
    2020: {
        # Slovakia: AWS 18, Azure 16, Docker 15, K8s 8, GCP 5
        "SK": {"AWS": 18, "Azure": 16, "Docker": 15, "K8s": 8, "GCP": 5},
        # Czech: AWS 35, Docker 30, Azure 25, K8s 20, GCP 8
        "CZ": {"AWS": 35, "Azure": 25, "Docker": 30, "K8s": 20, "GCP": 8},
        # Poland: AWS 40, Azure 32, Docker 25, K8s 8, GCP 12
        "PL": {"AWS": 40, "Azure": 32, "Docker": 25, "K8s": 8, "GCP": 12},
        # Germany: AWS 38, Azure 20, Docker 45, K8s 15, GCP 16
        "DE": {"AWS": 38, "Azure": 20, "Docker": 45, "K8s": 15, "GCP": 16},
        # Austria: AWS 38, Azure 23, Docker 15, K8s 8, GCP 10
        "AT": {"AWS": 38, "Azure": 23, "Docker": 15, "K8s": 8, "GCP": 10},
        # Hungary: Azure 47, AWS 26, Docker 35, K8s 28, GCP 6
        "HU": {"AWS": 26, "Azure": 47, "Docker": 35, "K8s": 28, "GCP": 6},
        # Switzerland: Azure 40, AWS 30, Docker 21, K8s 30, GCP 8
        "CH": {"AWS": 30, "Azure": 40, "Docker": 21, "K8s": 30, "GCP": 8},
        # Luxembourg: AWS 28, Azure 26, Docker 20, K8s 10, GCP 6
        "LU": {"AWS": 28, "Azure": 26, "Docker": 20, "K8s": 10, "GCP": 6},
        # Denmark: AWS 40, Azure 25, Docker 50, K8s 25, GCP 15
        "DK": {"AWS": 40, "Azure": 25, "Docker": 50, "K8s": 25, "GCP": 15},
        # Norway: Azure 36, AWS 28, Docker 35, K8s 22, GCP 4
        "NO": {"AWS": 28, "Azure": 36, "Docker": 35, "K8s": 22, "GCP": 4},
        # Italy: AWS 32, Azure 18, Docker 40, K8s 15, GCP 9
        "IT": {"AWS": 32, "Azure": 18, "Docker": 40, "K8s": 15, "GCP": 9},
        # Croatia: AWS 25, Azure 20, Docker 20, K8s 5, GCP 8
        "HR": {"AWS": 25, "Azure": 20, "Docker": 20, "K8s": 5, "GCP": 8},
        # Portugal: AWS 42, Azure 28, Docker 35, K8s 20, GCP 18
        "PT": {"AWS": 42, "Azure": 28, "Docker": 35, "K8s": 20, "GCP": 18},
        # Spain: AWS 20, Azure 18, Docker 18, K8s 10, GCP 7
        "ES": {"AWS": 20, "Azure": 18, "Docker": 18, "K8s": 10, "GCP": 7},
        # Ireland: AWS 35, Azure 25, Docker 55, K8s 8, GCP 8
        "IE": {"AWS": 35, "Azure": 25, "Docker": 55, "K8s": 8, "GCP": 8},
        # UK: AWS 33, Azure 18, Docker 50, K8s 16, GCP 8
        "GB": {"AWS": 33, "Azure": 18, "Docker": 50, "K8s": 16, "GCP": 8},
        # France: AWS 35, Azure 30, Docker 50, K8s 40, GCP 10
        "FR": {"AWS": 35, "Azure": 30, "Docker": 50, "K8s": 40, "GCP": 10},
        # Belgium: AWS 50, Azure 35, Docker 40, K8s 35, GCP 15
        "BE": {"AWS": 50, "Azure": 35, "Docker": 40, "K8s": 35, "GCP": 15},
        # Netherlands: AWS 48, Azure 25, Docker 55, K8s 22, GCP 20
        "NL": {"AWS": 48, "Azure": 25, "Docker": 55, "K8s": 22, "GCP": 20},
        # Finland: Azure 45, AWS 35, Docker 35, K8s 12, GCP 15
        "FI": {"AWS": 35, "Azure": 45, "Docker": 35, "K8s": 12, "GCP": 15},
        # Sweden: AWS 45, Azure 35, Docker 40, K8s 20, GCP 10
        "SE": {"AWS": 45, "Azure": 35, "Docker": 40, "K8s": 20, "GCP": 10},
        # Slovenia: Docker 25, AWS 20, Azure 15, K8s 10, GCP 5
        "SI": {"AWS": 20, "Azure": 15, "Docker": 25, "K8s": 10, "GCP": 5},
    },
    2021: {
        "SK": {"AWS": 20, "Azure": 18, "Docker": 20, "K8s": 10, "GCP": 6},
        "CZ": {"AWS": 38, "Azure": 28, "Docker": 35, "K8s": 20, "GCP": 8},
        "PL": {"AWS": 42, "Azure": 34, "Docker": 35, "K8s": 20, "GCP": 14},
        "DE": {"AWS": 40, "Azure": 22, "Docker": 48, "K8s": 20, "GCP": 18},
        "AT": {"AWS": 35, "Azure": 26, "Docker": 15, "K8s": 12, "GCP": 11},
        "HU": {"AWS": 27, "Azure": 48, "Docker": 40, "K8s": 33, "GCP": 7},
        "CH": {"AWS": 30, "Azure": 40, "Docker": 25, "K8s": 30, "GCP": 8},
        "LU": {"AWS": 30, "Azure": 28, "Docker": 25, "K8s": 15, "GCP": 7},
        "DK": {"AWS": 40, "Azure": 25, "Docker": 60, "K8s": 30, "GCP": 10},
        "NO": {"AWS": 30, "Azure": 40, "Docker": 48, "K8s": 32, "GCP": 5},
        "IT": {"AWS": 32, "Azure": 20, "Docker": 45, "K8s": 20, "GCP": 10},
        "HR": {"AWS": 35, "Azure": 30, "Docker": 35, "K8s": 15, "GCP": 8},
        "PT": {"AWS": 48, "Azure": 30, "Docker": 42, "K8s": 26, "GCP": 22},
        "ES": {"AWS": 22, "Azure": 19, "Docker": 22, "K8s": 12, "GCP": 8},
        "IE": {"AWS": 35, "Azure": 25, "Docker": 69, "K8s": 15, "GCP": 8},
        "GB": {"AWS": 33, "Azure": 22, "Docker": 48, "K8s": 16, "GCP": 10},
        "FR": {"AWS": 40, "Azure": 18, "Docker": 45, "K8s": 15, "GCP": 10},
        "BE": {"AWS": 52, "Azure": 38, "Docker": 50, "K8s": 35, "GCP": 18},
        "NL": {"AWS": 45, "Azure": 35, "Docker": 60, "K8s": 40, "GCP": 20},
        "FI": {"AWS": 40, "Azure": 50, "Docker": 48, "K8s": 16, "GCP": 18},
        "SE": {"AWS": 45, "Azure": 35, "Docker": 48, "K8s": 25, "GCP": 10},
        "SI": {"AWS": 35, "Azure": 30, "Docker": 40, "K8s": 25, "GCP": 12},
    },
    2022: {
        "SK": {"AWS": 22, "Azure": 19, "Docker": 25, "K8s": 12, "GCP": 7},
        "CZ": {"AWS": 38, "Azure": 28, "Docker": 40, "K8s": 30, "GCP": 8},
        "PL": {"AWS": 40, "Azure": 35, "Docker": 50, "K8s": 30, "GCP": 15},
        "DE": {"AWS": 42, "Azure": 24, "Docker": 55, "K8s": 25, "GCP": 20},
        "AT": {"AWS": 35, "Azure": 26, "Docker": 25, "K8s": 12, "GCP": 11},
        "HU": {"AWS": 28, "Azure": 49, "Docker": 44, "K8s": 38, "GCP": 8},
        "CH": {"AWS": 30, "Azure": 40, "Docker": 30, "K8s": 30, "GCP": 8},
        "LU": {"AWS": 32, "Azure": 30, "Docker": 30, "K8s": 18, "GCP": 8},
        "DK": {"AWS": 40, "Azure": 30, "Docker": 50, "K8s": 30, "GCP": 10},
        "NO": {"AWS": 32, "Azure": 43, "Docker": 58, "K8s": 42, "GCP": 6},
        "IT": {"AWS": 33, "Azure": 21, "Docker": 50, "K8s": 25, "GCP": 11},
        "HR": {"AWS": 38, "Azure": 33, "Docker": 45, "K8s": 25, "GCP": 10},
        "PT": {"AWS": 40, "Azure": 25, "Docker": 30, "K8s": 25, "GCP": 15},
        "ES": {"AWS": 24, "Azure": 20, "Docker": 28, "K8s": 15, "GCP": 9},
        "IE": {"AWS": 35, "Azure": 25, "Docker": 55, "K8s": 20, "GCP": 10},
        "GB": {"AWS": 32, "Azure": 21, "Docker": 60, "K8s": 25, "GCP": 9},
        "FR": {"AWS": 30, "Azure": 30, "Docker": 50, "K8s": 40, "GCP": 15},
        "BE": {"AWS": 50, "Azure": 42, "Docker": 60, "K8s": 50, "GCP": 20},
        "NL": {"AWS": 48, "Azure": 24, "Docker": 60, "K8s": 38, "GCP": 22},
        "FI": {"AWS": 40, "Azure": 50, "Docker": 53, "K8s": 20, "GCP": 18},
        "SE": {"AWS": 35, "Azure": 38, "Docker": 50, "K8s": 30, "GCP": 12},
        "SI": {"AWS": 35, "Azure": 25, "Docker": 50, "K8s": 30, "GCP": 10},
    },
    2023: {
        "SK": {"AWS": 24, "Azure": 20, "Docker": 28, "K8s": 15, "GCP": 8},
        "CZ": {"AWS": 40, "Azure": 30, "Docker": 45, "K8s": 45, "GCP": 8},
        "PL": {"AWS": 38, "Azure": 36, "Docker": 60, "K8s": 38, "GCP": 16},
        "DE": {"AWS": 44, "Azure": 26, "Docker": 60, "K8s": 28, "GCP": 23},
        "AT": {"AWS": 32, "Azure": 30, "Docker": 28, "K8s": 22, "GCP": 15},
        "HU": {"AWS": 29, "Azure": 50, "Docker": 48, "K8s": 42, "GCP": 9},
        "CH": {"AWS": 32, "Azure": 40, "Docker": 56, "K8s": 40, "GCP": 12},
        "LU": {"AWS": 35, "Azure": 32, "Docker": 35, "K8s": 22, "GCP": 9},
        "DK": {"AWS": 40, "Azure": 30, "Docker": 40, "K8s": 30, "GCP": 15},
        "NO": {"AWS": 34, "Azure": 46, "Docker": 68, "K8s": 52, "GCP": 7},
        "IT": {"AWS": 40, "Azure": 25, "Docker": 55, "K8s": 30, "GCP": 20},
        "HR": {"AWS": 40, "Azure": 35, "Docker": 50, "K8s": 28, "GCP": 12},
        "PT": {"AWS": 42, "Azure": 26, "Docker": 35, "K8s": 25, "GCP": 18},
        "ES": {"AWS": 26, "Azure": 22, "Docker": 32, "K8s": 18, "GCP": 10},
        "IE": {"AWS": 35, "Azure": 30, "Docker": 53, "K8s": 30, "GCP": 12},
        "GB": {"AWS": 48, "Azure": 26, "Docker": 60, "K8s": 35, "GCP": 24},
        "FR": {"AWS": 35, "Azure": 25, "Docker": 40, "K8s": 25, "GCP": 12},
        "BE": {"AWS": 48, "Azure": 26, "Docker": 53, "K8s": 62, "GCP": 23},
        "NL": {"AWS": 48, "Azure": 26, "Docker": 63, "K8s": 42, "GCP": 23},
        "FI": {"AWS": 40, "Azure": 50, "Docker": 58, "K8s": 25, "GCP": 20},
        "SE": {"AWS": 40, "Azure": 35, "Docker": 60, "K8s": 25, "GCP": 12},
        "SI": {"AWS": 45, "Azure": 25, "Docker": 55, "K8s": 30, "GCP": 20},
    },
    2024: {
        "SK": {"AWS": 26, "Azure": 21, "Docker": 32, "K8s": 18, "GCP": 9},
        "CZ": {"AWS": 40, "Azure": 30, "Docker": 50, "K8s": 55, "GCP": 10},
        "PL": {"AWS": 36, "Azure": 38, "Docker": 70, "K8s": 45, "GCP": 17},
        "DE": {"AWS": 44, "Azure": 26, "Docker": 65, "K8s": 32, "GCP": 25},
        "AT": {"AWS": 30, "Azure": 32, "Docker": 30, "K8s": 25, "GCP": 15},
        "HU": {"AWS": 30, "Azure": 50, "Docker": 52, "K8s": 45, "GCP": 10},
        "CH": {"AWS": 32, "Azure": 40, "Docker": 56, "K8s": 40, "GCP": 12},
        "LU": {"AWS": 37, "Azure": 33, "Docker": 38, "K8s": 25, "GCP": 10},
        "DK": {"AWS": 40, "Azure": 30, "Docker": 50, "K8s": 30, "GCP": 15},
        "NO": {"AWS": 36, "Azure": 48, "Docker": 75, "K8s": 60, "GCP": 8},
        "IT": {"AWS": 30, "Azure": 28, "Docker": 43, "K8s": 28, "GCP": 25},
        "HR": {"AWS": 40, "Azure": 35, "Docker": 53, "K8s": 33, "GCP": 16},
        "PT": {"AWS": 35, "Azure": 28, "Docker": 55, "K8s": 30, "GCP": 20},
        "ES": {"AWS": 28, "Azure": 24, "Docker": 37, "K8s": 22, "GCP": 11},
        "IE": {"AWS": 40, "Azure": 35, "Docker": 60, "K8s": 50, "GCP": 15},
        "GB": {"AWS": 50, "Azure": 40, "Docker": 65, "K8s": 45, "GCP": 15},
        "FR": {"AWS": 30, "Azure": 25, "Docker": 55, "K8s": 35, "GCP": 12},
        "BE": {"AWS": 49, "Azure": 48, "Docker": 59, "K8s": 65, "GCP": 25},
        "NL": {"AWS": 48, "Azure": 28, "Docker": 65, "K8s": 45, "GCP": 25},
        "FI": {"AWS": 40, "Azure": 50, "Docker": 65, "K8s": 30, "GCP": 20},
        "SE": {"AWS": 35, "Azure": 40, "Docker": 50, "K8s": 30, "GCP": 15},
        "SI": {"AWS": 45, "Azure": 28, "Docker": 55, "K8s": 35, "GCP": 22},
    },
    2025: {
        "SK": {"AWS": 28, "Azure": 22, "Docker": 35, "K8s": 20, "GCP": 10},
        "CZ": {"AWS": 40, "Azure": 30, "Docker": 50, "K8s": 55, "GCP": 12},
        "PL": {"AWS": 35, "Azure": 39, "Docker": 75, "K8s": 50, "GCP": 19},
        "DE": {"AWS": 44, "Azure": 27, "Docker": 88, "K8s": 35, "GCP": 24},
        "AT": {"AWS": 28, "Azure": 38, "Docker": 30, "K8s": 28, "GCP": 16},
        "HU": {"AWS": 32, "Azure": 50, "Docker": 58, "K8s": 48, "GCP": 10},
        "CH": {"AWS": 30, "Azure": 40, "Docker": 56, "K8s": 40, "GCP": 12},
        "LU": {"AWS": 39, "Azure": 34, "Docker": 40, "K8s": 28, "GCP": 11},
        "DK": {"AWS": 40, "Azure": 30, "Docker": 55, "K8s": 35, "GCP": 15},
        "NO": {"AWS": 35, "Azure": 50, "Docker": 80, "K8s": 65, "GCP": 8},
        "IT": {"AWS": 30, "Azure": 20, "Docker": 71, "K8s": 76, "GCP": 11},
        "HR": {"AWS": 40, "Azure": 35, "Docker": 55, "K8s": 35, "GCP": 15},
        "PT": {"AWS": 38, "Azure": 30, "Docker": 60, "K8s": 35, "GCP": 20},
        "ES": {"AWS": 30, "Azure": 26, "Docker": 40, "K8s": 24, "GCP": 12},
        "IE": {"AWS": 40, "Azure": 35, "Docker": 60, "K8s": 50, "GCP": 15},
        "GB": {"AWS": 45, "Azure": 40, "Docker": 65, "K8s": 50, "GCP": 15},
        "FR": {"AWS": 30, "Azure": 22, "Docker": 65, "K8s": 76, "GCP": 10},
        "BE": {"AWS": 50, "Azure": 48, "Docker": 75, "K8s": 70, "GCP": 25},
        "NL": {"AWS": 48, "Azure": 28, "Docker": 65, "K8s": 45, "GCP": 24},
        "FI": {"AWS": 38, "Azure": 52, "Docker": 65, "K8s": 36, "GCP": 22},
        "SE": {"AWS": 40, "Azure": 35, "Docker": 70, "K8s": 35, "GCP": 15},
        "SI": {"AWS": 40, "Azure": 25, "Docker": 40, "K8s": 35, "GCP": 20},
    },
}

# Farby pre pie charty - Cloud technologies
COLORS = {
    "AWS": QColor(255, 153, 0),       # Oranzova (AWS orange)
    "Azure": QColor(0, 120, 212),     # Modra (Azure blue)
    "Docker": QColor(13, 183, 237),   # Svetlo modra (Docker blue)
    "K8s": QColor(50, 108, 229),      # Modra (Kubernetes blue)
    "GCP": QColor(234, 67, 53),       # Cervena (Google red)
}

TECHNOLOGIES = ["AWS", "Azure", "Docker", "K8s", "GCP"]

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
    for tech in TECHNOLOGIES:
        fields_def += f"&field={tech}:integer"

    uri = f"Polygon?crs={crs}&{fields_def}"
    new_layer = QgsVectorLayer(uri, f"Cloud_{year}", "memory")

    if not new_layer.isValid():
        print(f"  Nepodarilo sa vytvorit vrstvu pre {year}")
        return None

    dp = new_layer.dataProvider()
    year_data = CLOUD_DATA[year]

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
                for tech in TECHNOLOGIES:
                    attrs.append(country_data.get(tech, 0))
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
    ds.categoryAttributes = TECHNOLOGIES.copy()
    ds.categoryColors = [COLORS[tech] for tech in TECHNOLOGIES]
    ds.categoryLabels = TECHNOLOGIES.copy()

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
    print("Cloud Technologies Pie Charts Generator")
    print("22 krajin - AWS, Azure, Docker, Kubernetes, GCP")
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

    # Vytvor skupinu pre cloud vrstvy
    root = QgsProject.instance().layerTreeRoot()
    cloud_group = root.insertGroup(0, "cloud_technologies")
    print("Vytvorena skupina: cloud_technologies")

    # Vytvor vrstvy pre kazdy rok
    for year in [2020, 2021, 2022, 2023, 2024, 2025]:
        layer = create_layer_for_year(year)
        if layer:
            setup_pie_chart(layer, year)
            # Pridaj vrstvu do projektu
            QgsProject.instance().addMapLayer(layer, False)
            # Pridaj do skupiny
            cloud_group.addLayer(layer)
            print(f"Hotova vrstva: Cloud_{year}")
        print("-" * 40)

    print("=" * 60)
    print("HOTOVO!")
    print("")
    print("STRUKTURA:")
    print("  cloud_technologies/")
    print("     Cloud_2020")
    print("     Cloud_2021")
    print("     Cloud_2022")
    print("     Cloud_2023")
    print("     Cloud_2024")
    print("     Cloud_2025")
    print("")
    print("FARBY:")
    print("  AWS:        #FF9900 (Oranzova)")
    print("  Azure:      #0078D4 (Modra)")
    print("  Docker:     #0DB7ED (Svetlo modra)")
    print("  Kubernetes: #326CE5 (Modra)")
    print("  GCP:        #EA4335 (Cervena)")
    print("")
    print("22 krajin: SK, CZ, PL, DE, AT, HU, CH, LU, DK, NO,")
    print("           IT, HR, PT, ES, IE, GB, FR, BE, NL, FI, SE, SI")
    print("")
    print("KLUCOVE TRENDY 2020-2025:")
    print("  - Azure dominancia: NO (50%), FI (52%), HU (50%)")
    print("  - Docker: Univerzalna adopcia 65-88%")
    print("  - Kubernetes: +300% rast (8% -> 50%)")
    print("  - AWS: Stabilny lider 35-50%")
    print("  - GCP: Rastie pomaly 8-25%")
    print("")
    print("Prepinaj viditelnost vrstiev Cloud_2020 - Cloud_2025")
    print("=" * 60)

    iface.mapCanvas().refresh()


main()
