"""
Plant Disease Detection - Class Names, Label Parsing & Disease Info
"""

CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


def parse_label(label):
    """
    Parse a class label into plant name and disease name.
    E.g. 'Tomato___Early_blight' -> {'plant': 'Tomato', 'disease': 'Early Blight'}
    """
    parts = label.split("___")
    plant = parts[0].replace("_", " ")
    # Clean parenthetical info for display
    plant = plant.replace("  ", " ").strip()

    if len(parts) > 1:
        disease_raw = parts[1]
    else:
        disease_raw = "healthy"

    if disease_raw.lower() == "healthy":
        disease = "Healthy"
    else:
        disease = disease_raw.replace("_", " ").strip()
        # Title-case each word
        disease = " ".join(
            word.capitalize() if word[0].islower() else word for word in disease.split()
        )

    return {"plant": plant, "disease": disease}


DISEASE_INFO = {
    "Apple___Apple_scab": {
        "description": "Apple scab is caused by the fungus Venturia inaequalis. It leads to dark, olive-green to brown lesions on leaves and fruit.",
        "treatment": "Apply fungicides such as captan or myclobutanil during early spring. Remove fallen leaves and infected fruit to reduce overwintering spores. Plant resistant apple varieties.",
        "severity": "mild",
    },
    "Apple___Black_rot": {
        "description": "Black rot is caused by the fungus Botryosphaeria obtusa. It causes brown lesions on leaves, rotting fruit, and cankers on branches.",
        "treatment": "Prune out dead or infected branches. Remove mummified fruit. Apply fungicides during the growing season. Maintain good air circulation.",
        "severity": "severe",
    },
    "Apple___Cedar_apple_rust": {
        "description": "Cedar apple rust is caused by the fungus Gymnosporangium juniperi-virginianae. It causes bright orange-yellow spots on apple leaves and fruit.",
        "treatment": "Remove nearby cedar and juniper trees if possible. Apply fungicides like myclobutanil in spring. Plant resistant apple varieties.",
        "severity": "mild",
    },
    "Apple___healthy": {
        "description": "The apple plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: proper watering, balanced fertilization, and periodic pruning for good air circulation.",
        "severity": "healthy",
    },
    "Blueberry___healthy": {
        "description": "The blueberry plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: maintain acidic soil (pH 4.5-5.5), mulch with pine needles, and ensure proper irrigation.",
        "severity": "healthy",
    },
    "Cherry_(including_sour)___healthy": {
        "description": "The cherry plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: prune annually for shape and airflow, water deeply during dry spells, and apply balanced fertilizer in spring.",
        "severity": "healthy",
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "Powdery mildew is caused by the fungus Podosphaera clandestina. It creates a white powdery coating on cherry leaves, shoots, and fruit.",
        "treatment": "Apply sulfur-based or potassium bicarbonate fungicides. Prune to improve air circulation. Avoid overhead watering. Remove affected plant parts.",
        "severity": "mild",
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "description": "Gray leaf spot is caused by the fungus Cercospora zeae-maydis. It produces rectangular gray to tan lesions on corn leaves, reducing photosynthesis.",
        "treatment": "Rotate crops away from corn for 1-2 years. Use resistant hybrids. Apply foliar fungicides like strobilurin if disease pressure is high. Till crop residue after harvest.",
        "severity": "severe",
    },
    "Corn_(maize)___Common_rust_": {
        "description": "Common rust is caused by the fungus Puccinia sorghi. It produces small, round to elongated reddish-brown pustules on both leaf surfaces.",
        "treatment": "Plant resistant hybrids. Apply fungicides if infection is detected early and conditions favor spread. Usually does not require treatment in mature plants.",
        "severity": "mild",
    },
    "Corn_(maize)___healthy": {
        "description": "The corn plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: ensure adequate nitrogen fertilization, proper spacing, and consistent watering especially during tasseling.",
        "severity": "healthy",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "Northern leaf blight is caused by the fungus Exserohilum turcicum. It causes long, elliptical gray-green to tan lesions on corn leaves.",
        "treatment": "Use resistant hybrids. Rotate crops. Apply foliar fungicides if disease appears before tasseling. Manage crop residues through tillage.",
        "severity": "severe",
    },
    "Grape___Black_rot": {
        "description": "Black rot is caused by the fungus Guignardia bidwellii. It causes brown circular lesions on leaves and shriveled, black mummified berries.",
        "treatment": "Remove mummified berries and infected plant parts. Apply fungicides (myclobutanil, mancozeb) from bud break through fruit set. Improve air circulation through canopy management.",
        "severity": "severe",
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "Esca (Black Measles) is a complex fungal disease caused by multiple fungi including Phaeomoniella and Phaeoacremonium species. It causes interveinal striping on leaves and dark spotting on berries.",
        "treatment": "No fully effective cure exists. Prune out infected wood. Apply wound protectants after pruning. Remove severely affected vines. Some biocontrol agents show promise.",
        "severity": "severe",
    },
    "Grape___healthy": {
        "description": "The grape plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: proper trellising, balanced fertilization, regular pruning, and preventive fungicide sprays during wet seasons.",
        "severity": "healthy",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "Leaf blight (Isariopsis leaf spot) is caused by the fungus Pseudocercospora vitis. It produces dark brown spots with yellow halos on grape leaves.",
        "treatment": "Apply copper-based or mancozeb fungicides. Remove infected leaves. Improve air circulation by proper pruning. Avoid overhead irrigation.",
        "severity": "mild",
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "Huanglongbing (Citrus Greening) is caused by the bacterium Candidatus Liberibacter. It is spread by the Asian citrus psyllid and causes mottled yellowing of leaves, misshapen bitter fruit, and tree decline.",
        "treatment": "No cure exists. Control psyllid vectors with insecticides. Remove infected trees to prevent spread. Plant certified disease-free nursery stock. Apply nutritional sprays to manage symptoms.",
        "severity": "severe",
    },
    "Peach___Bacterial_spot": {
        "description": "Bacterial spot is caused by Xanthomonas arboricola pv. pruni. It causes small, dark, water-soaked lesions on leaves, fruit spotting, and twig cankers.",
        "treatment": "Apply copper-based bactericides in early spring. Plant resistant varieties. Avoid overhead irrigation. Remove severely infected branches.",
        "severity": "severe",
    },
    "Peach___healthy": {
        "description": "The peach plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: annual pruning for open center form, thinning fruit for size, and dormant fungicide sprays as prevention.",
        "severity": "healthy",
    },
    "Pepper,_bell___Bacterial_spot": {
        "description": "Bacterial spot is caused by Xanthomonas campestris pv. vesicatoria. It causes small, dark, water-soaked spots on pepper leaves and fruit, leading to defoliation and yield loss.",
        "treatment": "Use disease-free seed and transplants. Apply copper-based sprays. Rotate crops (2-3 year cycle). Avoid working with wet plants. Remove infected debris.",
        "severity": "severe",
    },
    "Pepper,_bell___healthy": {
        "description": "The bell pepper plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: consistent watering, balanced fertilization with calcium, and staking for support. Mulch to retain moisture.",
        "severity": "healthy",
    },
    "Potato___Early_blight": {
        "description": 'Early blight is caused by the fungus Alternaria solani. It produces dark brown to black concentric ring lesions ("target spots") on older leaves first.',
        "treatment": "Apply fungicides (chlorothalonil, mancozeb) preventively. Rotate crops. Remove infected plant debris. Ensure adequate nutrition and irrigation. Plant resistant varieties.",
        "severity": "mild",
    },
    "Potato___healthy": {
        "description": "The potato plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: hill soil around stems, maintain consistent moisture, and apply balanced fertilizer. Monitor for pests regularly.",
        "severity": "healthy",
    },
    "Potato___Late_blight": {
        "description": "Late blight is caused by the oomycete Phytophthora infestans. It causes water-soaked dark lesions on leaves and stems, white mold on undersides, and rapid plant death.",
        "treatment": "Apply fungicides (chlorothalonil, metalaxyl) preventively during cool, wet weather. Destroy infected plants immediately. Use certified disease-free seed potatoes. Avoid overhead irrigation.",
        "severity": "severe",
    },
    "Raspberry___healthy": {
        "description": "The raspberry plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: prune spent canes after fruiting, maintain trellis support, apply mulch, and ensure good air circulation.",
        "severity": "healthy",
    },
    "Soybean___healthy": {
        "description": "The soybean plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: ensure proper inoculation with rhizobium bacteria, maintain weed control, and scout regularly for pests.",
        "severity": "healthy",
    },
    "Squash___Powdery_mildew": {
        "description": "Powdery mildew on squash is caused by Podosphaera xanthii or Erysiphe cichoracearum. White powdery patches appear on leaf surfaces, reducing photosynthesis and yield.",
        "treatment": "Apply potassium bicarbonate, neem oil, or sulfur-based fungicides. Improve air circulation by proper spacing. Water at the base of plants. Remove severely infected leaves.",
        "severity": "mild",
    },
    "Strawberry___healthy": {
        "description": "The strawberry plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: mulch with straw, remove runners for larger fruit, ensure good drainage, and replace plants every 3-4 years.",
        "severity": "healthy",
    },
    "Strawberry___Leaf_scorch": {
        "description": 'Leaf scorch is caused by the fungus Diplocarpon earlianum. It produces irregular purple to dark red spots that merge to "scorch" the leaf margins.',
        "treatment": "Remove old infected leaves after harvest. Apply fungicides in spring. Ensure good air circulation and drainage. Plant resistant varieties. Renovate beds regularly.",
        "severity": "mild",
    },
    "Tomato___Bacterial_spot": {
        "description": "Bacterial spot is caused by Xanthomonas species. It creates small, dark, raised spots on leaves and fruit with yellow halos, leading to defoliation.",
        "treatment": "Use disease-free seed and transplants. Apply copper-based bactericides. Rotate crops. Avoid overhead watering. Remove and destroy infected plants.",
        "severity": "severe",
    },
    "Tomato___Early_blight": {
        "description": "Early blight is caused by Alternaria solani. It produces dark concentric ring lesions on older leaves first, progressing upward. Can cause significant defoliation.",
        "treatment": "Apply fungicides (chlorothalonil, mancozeb). Mulch around plant base. Stake plants for airflow. Remove lower affected leaves. Rotate crops annually.",
        "severity": "mild",
    },
    "Tomato___healthy": {
        "description": "The tomato plant appears healthy with no visible signs of disease.",
        "treatment": "Continue regular care: consistent deep watering, staking or caging, balanced fertilization with calcium, and regular pruning of suckers.",
        "severity": "healthy",
    },
    "Tomato___Late_blight": {
        "description": "Late blight is caused by Phytophthora infestans. It causes large, dark, water-soaked lesions on leaves, stems, and fruit, often with white fungal growth underneath.",
        "treatment": "Apply fungicides (chlorothalonil, copper) preventively in cool/wet conditions. Remove infected plants immediately. Ensure good air circulation. Use resistant varieties.",
        "severity": "severe",
    },
    "Tomato___Leaf_Mold": {
        "description": "Leaf mold is caused by the fungus Passalora fulva (Cladosporium fulvum). It produces pale green to yellow spots on upper leaf surfaces with olive-green to brown velvety mold underneath.",
        "treatment": "Improve ventilation in greenhouses. Reduce humidity below 85%. Apply fungicides if needed. Remove infected leaves. Use resistant varieties.",
        "severity": "mild",
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "Septoria leaf spot is caused by the fungus Septoria lycopersici. It produces many small, circular spots with dark borders and gray centers on lower leaves.",
        "treatment": "Remove infected lower leaves. Apply fungicides (chlorothalonil, copper). Mulch to prevent soil splash. Avoid overhead watering. Practice crop rotation.",
        "severity": "mild",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "description": "Two-spotted spider mites (Tetranychus urticae) cause stippling (tiny yellow dots) on leaves, fine webbing, and can cause leaf bronzing and drop under heavy infestation.",
        "treatment": "Spray plants with strong water jets to dislodge mites. Apply miticides or insecticidal soap. Introduce predatory mites (Phytoseiulus persimilis). Increase humidity around plants.",
        "severity": "mild",
    },
    "Tomato___Target_Spot": {
        "description": "Target spot is caused by the fungus Corynespora cassiicola. It produces concentric ring lesions (target-like) on leaves, stems, and fruit.",
        "treatment": "Apply fungicides (chlorothalonil, mancozeb). Improve air circulation. Remove infected plant debris. Practice crop rotation. Avoid excessive nitrogen fertilization.",
        "severity": "mild",
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "Tomato mosaic virus (ToMV) causes mottled light and dark green patterns on leaves, leaf curling, stunted growth, and reduced fruit quality.",
        "treatment": "No cure for viral infections. Remove and destroy infected plants. Disinfect tools with 10% bleach solution. Wash hands before handling plants. Plant resistant varieties. Control aphid vectors.",
        "severity": "severe",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is transmitted by whiteflies. It causes upward leaf curling, yellowing of leaf margins, stunted growth, and flower drop.",
        "treatment": "Control whitefly populations with insecticides or sticky traps. Remove infected plants. Use reflective mulches to repel whiteflies. Plant resistant varieties. Use insect-proof netting.",
        "severity": "severe",
    },
}
