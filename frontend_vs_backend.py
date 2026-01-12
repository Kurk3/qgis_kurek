"""
QGIS Python Script - Frontend vs Backend Pie Charts 2020-2025
22 europskych krajin - Porovnanie Frontend vs Backend pozicii

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

# Data pre Frontend vs Backend (v percentach)
# Vypocitane z .md suborov - job counts pre frontend a backend frameworky

FRONTEND_BACKEND_DATA = {
    2020: {
        "SK": {"Frontend": 38, "Backend": 62},  # Angular/React era, strong Spring backend
        "CZ": {"Frontend": 38, "Backend": 62},  # Angular stronger than React
        "PL": {"Frontend": 36, "Backend": 64},  # Strong backend outsourcing market
        "DE": {"Frontend": 42, "Backend": 58},  # Enterprise backend heavy
        "AT": {"Frontend": 38, "Backend": 62},  # Similar to Germany pattern
        "HU": {"Frontend": 36, "Backend": 64},  # Backend outsourcing focus
        "CH": {"Frontend": 42, "Backend": 58},  # High-value market
        "LU": {"Frontend": 40, "Backend": 60},  # Finance backend heavy
        "DK": {"Frontend": 42, "Backend": 58},  # Nordic pattern
        "NO": {"Frontend": 40, "Backend": 60},  # Oil/enterprise backend
        "IT": {"Frontend": 36, "Backend": 64},  # Enterprise backend heavy
        "HR": {"Frontend": 36, "Backend": 64},  # Outsourcing market
        "PT": {"Frontend": 38, "Backend": 62},  # Tech hub growth
        "ES": {"Frontend": 36, "Backend": 64},  # Backend outsourcing
        "IE": {"Frontend": 42, "Backend": 58},  # Multinational tech hub
        "GB": {"Frontend": 42, "Backend": 58},  # Large diverse market
        "FR": {"Frontend": 38, "Backend": 62},  # Enterprise backend focus
        "BE": {"Frontend": 40, "Backend": 60},  # EU institution backend
        "NL": {"Frontend": 42, "Backend": 58},  # Startup ecosystem
        "FI": {"Frontend": 40, "Backend": 60},  # Similar to Sweden
        "SE": {"Frontend": 40, "Backend": 60},  # Nordic leader
        "SI": {"Frontend": 40, "Backend": 60},  # Small mature market
    },
    2021: {
        "SK": {"Frontend": 38, "Backend": 62},  # Recovery year, similar pattern
        "CZ": {"Frontend": 38, "Backend": 62},  # React=Angular parity
        "PL": {"Frontend": 36, "Backend": 64},  # Recovery, backend focus
        "DE": {"Frontend": 42, "Backend": 58},  # Recovery, 96K positions
        "AT": {"Frontend": 40, "Backend": 60},  # Recovery
        "HU": {"Frontend": 36, "Backend": 64},  # Recovery
        "CH": {"Frontend": 42, "Backend": 58},  # Stable
        "LU": {"Frontend": 40, "Backend": 60},  # Stable
        "DK": {"Frontend": 42, "Backend": 58},  # Stable
        "NO": {"Frontend": 42, "Backend": 58},  # Recovery
        "IT": {"Frontend": 38, "Backend": 62},  # Recovery
        "HR": {"Frontend": 38, "Backend": 62},  # Recovery
        "PT": {"Frontend": 40, "Backend": 60},  # Recovery
        "ES": {"Frontend": 38, "Backend": 62},  # Recovery
        "IE": {"Frontend": 44, "Backend": 56},  # Brexit advantage
        "GB": {"Frontend": 44, "Backend": 56},  # Recovery boom
        "FR": {"Frontend": 38, "Backend": 62},  # Recovery
        "BE": {"Frontend": 40, "Backend": 60},  # Recovery
        "NL": {"Frontend": 44, "Backend": 56},  # Strong frontend
        "FI": {"Frontend": 40, "Backend": 60},  # Stable
        "SE": {"Frontend": 40, "Backend": 60},  # EXPLICIT: 1,915 FE / 2,888 BE
        "SI": {"Frontend": 40, "Backend": 60},  # Recovery
    },
    2022: {
        "SK": {"Frontend": 40, "Backend": 60},  # Record year, React growth
        "CZ": {"Frontend": 40, "Backend": 60},  # React overtakes Angular
        "PL": {"Frontend": 36, "Backend": 64},  # Peak year, 27.7% backend of total
        "DE": {"Frontend": 44, "Backend": 56},  # 120K positions, React growth
        "AT": {"Frontend": 40, "Backend": 60},  # Growth year
        "HU": {"Frontend": 38, "Backend": 62},  # Growing frontend
        "CH": {"Frontend": 44, "Backend": 56},  # Frontend growth
        "LU": {"Frontend": 42, "Backend": 58},  # Growth
        "DK": {"Frontend": 44, "Backend": 56},  # Frontend growth
        "NO": {"Frontend": 42, "Backend": 58},  # Growth
        "IT": {"Frontend": 40, "Backend": 60},  # Growth
        "HR": {"Frontend": 40, "Backend": 60},  # Strong growth +26%
        "PT": {"Frontend": 42, "Backend": 58},  # Salary boom +36.5%
        "ES": {"Frontend": 40, "Backend": 60},  # Growth
        "IE": {"Frontend": 44, "Backend": 56},  # Peak year
        "GB": {"Frontend": 44, "Backend": 56},  # Record 2M+ vacancies
        "FR": {"Frontend": 40, "Backend": 60},  # Growth
        "BE": {"Frontend": 42, "Backend": 58},  # Growth
        "NL": {"Frontend": 44, "Backend": 56},  # Record vacancies
        "FI": {"Frontend": 42, "Backend": 58},  # Frontend growth
        "SE": {"Frontend": 42, "Backend": 58},  # React 40-45%
        "SI": {"Frontend": 42, "Backend": 58},  # Talent shortage
    },
    2023: {
        "SK": {"Frontend": 40, "Backend": 60},  # Market cooling
        "CZ": {"Frontend": 42, "Backend": 58},  # Strong frontend growth
        "PL": {"Frontend": 38, "Backend": 62},  # Market correction
        "DE": {"Frontend": 44, "Backend": 56},  # Peak 149K positions
        "AT": {"Frontend": 42, "Backend": 58},  # Frontend growth
        "HU": {"Frontend": 38, "Backend": 62},  # Continued growth
        "CH": {"Frontend": 44, "Backend": 56},  # Stable
        "LU": {"Frontend": 42, "Backend": 58},  # Stable
        "DK": {"Frontend": 44, "Backend": 56},  # Mature market
        "NO": {"Frontend": 44, "Backend": 56},  # Balanced
        "IT": {"Frontend": 40, "Backend": 60},  # Angular still strong - Italy specific
        "HR": {"Frontend": 40, "Backend": 60},  # Slowest growth in 9 years
        "PT": {"Frontend": 42, "Backend": 58},  # Strong full-stack
        "ES": {"Frontend": 40, "Backend": 60},  # Stable
        "IE": {"Frontend": 44, "Backend": 56},  # Layoff impact
        "GB": {"Frontend": 44, "Backend": 56},  # Correction
        "FR": {"Frontend": 40, "Backend": 60},  # Angular still strong
        "BE": {"Frontend": 42, "Backend": 58},  # Stable
        "NL": {"Frontend": 44, "Backend": 56},  # Stable
        "FI": {"Frontend": 42, "Backend": 58},  # Stable
        "SE": {"Frontend": 42, "Backend": 58},  # React growing
        "SI": {"Frontend": 42, "Backend": 58},  # AI programme launch
    },
    2024: {
        "SK": {"Frontend": 40, "Backend": 60},  # Stable pattern
        "CZ": {"Frontend": 42, "Backend": 58},  # React 52% dominance
        "PL": {"Frontend": 38, "Backend": 62},  # Stabilization
        "DE": {"Frontend": 44, "Backend": 56},  # 137K+ positions
        "AT": {"Frontend": 42, "Backend": 58},  # Stable
        "HU": {"Frontend": 40, "Backend": 60},  # Balancing
        "CH": {"Frontend": 44, "Backend": 56},  # Premium market
        "LU": {"Frontend": 42, "Backend": 58},  # Finance tech hub
        "DK": {"Frontend": 44, "Backend": 56},  # Stable
        "NO": {"Frontend": 44, "Backend": 56},  # Azure dominant
        "IT": {"Frontend": 42, "Backend": 58},  # Modernizing
        "HR": {"Frontend": 42, "Backend": 58},  # TypeScript 68-73%
        "PT": {"Frontend": 42, "Backend": 58},  # .NET strong backend
        "ES": {"Frontend": 42, "Backend": 58},  # Frontend growing
        "IE": {"Frontend": 46, "Backend": 54},  # AI boom, frontend for ML interfaces
        "GB": {"Frontend": 44, "Backend": 56},  # Stable
        "FR": {"Frontend": 42, "Backend": 58},  # React growth
        "BE": {"Frontend": 42, "Backend": 58},  # Balanced
        "NL": {"Frontend": 44, "Backend": 56},  # React 39-40%
        "FI": {"Frontend": 44, "Backend": 56},  # React dominance
        "SE": {"Frontend": 44, "Backend": 56},  # React 58-65%
        "SI": {"Frontend": 44, "Backend": 56},  # React 35-42%
    },
    2025: {
        "SK": {"Frontend": 40, "Backend": 60},  # Calculated: ~906 FE / ~1352 BE jobs
        "CZ": {"Frontend": 42, "Backend": 58},  # Mature market
        "PL": {"Frontend": 38, "Backend": 62},  # Largest CEE market
        "DE": {"Frontend": 44, "Backend": 56},  # Strong React 50-60%, but Spring 28-33%
        "AT": {"Frontend": 42, "Backend": 58},  # Mature market
        "HU": {"Frontend": 40, "Backend": 60},  # Modernizing
        "CH": {"Frontend": 44, "Backend": 56},  # Balanced specialization
        "LU": {"Frontend": 42, "Backend": 58},  # Continued balance
        "DK": {"Frontend": 44, "Backend": 56},  # High specialization
        "NO": {"Frontend": 44, "Backend": 56},  # Stable
        "IT": {"Frontend": 42, "Backend": 58},  # Angular 35-40% unique to Italy
        "HR": {"Frontend": 42, "Backend": 58},  # React 35-40%
        "PT": {"Frontend": 42, "Backend": 58},  # React 38-45%, .NET 32-38%
        "ES": {"Frontend": 42, "Backend": 58},  # Modernizing market
        "IE": {"Frontend": 46, "Backend": 54},  # React 50-60% strong
        "GB": {"Frontend": 44, "Backend": 56},  # React 40-45%, Node 30-35%
        "FR": {"Frontend": 42, "Backend": 58},  # Balancing
        "BE": {"Frontend": 42, "Backend": 58},  # Mature market
        "NL": {"Frontend": 44, "Backend": 56},  # Node.js 40-42% backend
        "FI": {"Frontend": 44, "Backend": 56},  # Mature Nordic market
        "SE": {"Frontend": 44, "Backend": 56},  # React 60-65% dominance
        "SI": {"Frontend": 44, "Backend": 56},  # TypeScript 25-35%
    },
}

# Farby pre pie charty
COLORS = {
    "Frontend": QColor(33, 150, 243),   # Modra #2196F3
    "Backend": QColor(255, 152, 0),     # Oranzova #FF9800
}

CATEGORIES = ["Frontend", "Backend"]

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
    for cat in CATEGORIES:
        fields_def += f"&field={cat}:integer"

    uri = f"Polygon?crs={crs}&{fields_def}"
    new_layer = QgsVectorLayer(uri, f"FE_vs_BE_{year}", "memory")

    if not new_layer.isValid():
        print(f"  Nepodarilo sa vytvorit vrstvu pre {year}")
        return None

    dp = new_layer.dataProvider()
    year_data = FRONTEND_BACKEND_DATA[year]

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
                for cat in CATEGORIES:
                    attrs.append(country_data.get(cat, 0))
            else:
                # Nemame data - nulove hodnoty
                attrs = [iso_code, 0, 0]

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
    ds.categoryAttributes = CATEGORIES.copy()
    ds.categoryColors = [COLORS[cat] for cat in CATEGORIES]
    ds.categoryLabels = CATEGORIES.copy()

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
    print("Frontend vs Backend Pie Charts Generator")
    print("22 krajin - Modra (Frontend) vs Oranzova (Backend)")
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

    # Vytvor skupinu pre frontend vs backend vrstvy
    root = QgsProject.instance().layerTreeRoot()
    fe_be_group = root.insertGroup(0, "frontend_vs_backend")
    print("Vytvorena skupina: frontend_vs_backend")

    # Vytvor vrstvy pre kazdy rok
    for year in [2020, 2021, 2022, 2023, 2024, 2025]:
        layer = create_layer_for_year(year)
        if layer:
            setup_pie_chart(layer, year)
            # Pridaj vrstvu do projektu
            QgsProject.instance().addMapLayer(layer, False)
            # Pridaj do skupiny
            fe_be_group.addLayer(layer)
            print(f"Hotova vrstva: FE_vs_BE_{year}")
        print("-" * 40)

    print("=" * 60)
    print("HOTOVO!")
    print("")
    print("STRUKTURA:")
    print("  frontend_vs_backend/")
    print("     FE_vs_BE_2020")
    print("     FE_vs_BE_2021")
    print("     FE_vs_BE_2022")
    print("     FE_vs_BE_2023")
    print("     FE_vs_BE_2024")
    print("     FE_vs_BE_2025")
    print("")
    print("FARBY:")
    print("  Frontend: #2196F3 (Modra)")
    print("  Backend:  #FF9800 (Oranzova)")
    print("")
    print("22 krajin: SK, CZ, PL, DE, AT, HU, CH, LU, DK, NO,")
    print("           IT, HR, PT, ES, IE, GB, FR, BE, NL, FI, SE, SI")
    print("")
    print("DATA ZDROJE:")
    print("  - Svedsko 2021: Explicitne 1,915 FE / 2,888 BE pozicii (40:60)")
    print("  - Polsko 2022: Backend 27.7% vsetkych pozicii")
    print("  - Vypocitane z job counts pre frameworky v .md suboroch")
    print("")
    print("Prepinaj viditelnost vrstiev FE_vs_BE_2020 - FE_vs_BE_2025")
    print("=" * 60)

    iface.mapCanvas().refresh()


main()
