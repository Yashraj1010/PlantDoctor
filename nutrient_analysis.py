def analyze_nutrients(n, p, k, plant):
    if plant == "potato":
        if n > p and n > k:
            return "Excess nitrogen can harm potato crops: lowers yield, boosts disease risk, reduces starch, causes hollow heart & cracks."
        elif p > n and p > k:
            return "Excess phosphorus hinders potato growth due to short growth period & shallow roots. While vital for cell division & flowering, too much impedes nutrient absorption (e.g., zinc, iron). High levels cause soluble salt buildup, stunting growth."
        elif k > n and k > p:
            return "Potassium boosts early leaf expansion, delays shedding, and boosts yield of small potato tubers. It influences tuber features like size, shape, and color, while aiding nitrogen uptake and protein synthesis."
        elif n < p and n < k:
            return "Nitrogen deficiency in soil can cause reduced growth, pale leaves, and a smaller number of tubers."
        elif p < n and p < k:
            return "potato tubers can have smaller sizes, reduced yield, and slower growth. Phosphorus deficiency can also cause necrotic spots on the tubers, and decrease starch production"
        elif k < n and k < p:
            return "Potassium deficiency can cause plants to wilt on dry days, have short internodes, and small leaf blades. Potassium-deficient crops also grow slowly, have poorly developed root systems, and are prone to drought, pests, diseases, and nematodes."
    elif plant == "tomato":
        if n > p and n > k:
            return "High levels of nitrogen can help in tomato yield. Nitrogen can increase root biomass, plant height, root length, and root diameter."
        elif p > n and p > k:
            return "Phosphorus helps plants develop roots, which improves water use and nutrient uptake. However, too much phosphorus can prevent plants from absorbing nitrogen, which can limit the growth of the stem and foliage. It can also cause plants to grow poorly and even die."
        elif k > n and k > p:
            return "Excess soil potassium hampers tomato plant nutrition, hindering absorption of vital nutrients (magnesium, calcium, iron, zinc). This can trigger nitrogen and calcium deficiency, showing as yellowing between leaf veins and brown spots. Potassium surplus also disrupts micronutrient uptake (manganese, zinc, iron, magnesium)."
        elif n < p and n < k:
            return "the leaves may turn pale green or yellow, and the plant may appear thin and upright.  old leaves may turn brown or completely yellow before falling off. Other symptoms include stunted growth, reduced branching, and leaf surface area."
        elif p < n and p < k:
            return "Stunted growth Small, rigid leaves, Dark green leaves, Purple coloring, Reduced fruiting, Slow maturity, Reduced root development"
        elif k < n and k < p:
            return "Tomato plants may exhibit symptoms like yellow leaf margins, leathery tissue between veins, yellowing shoulders on fruit, and uneven ripening."
    elif plant == "corn":
        if n > p and n > k:
            return "Excess nitrogen prompts lush corn growth, inviting pests, diseases, and weak stems prone to lodging during flowering and grain filling. Additionally, it can harm the environment and reduce farm profits."
        elif p > n and p > k:
            return "High phosphorus (P) levels in soil are essential for high corn yields. Phosphorus is the second most demanded nutrient by corn plants and directly affects crop development and yield. It stimulates root and shoot growth and promotes vigorous seedling growth."
        elif k > n and k > p:
            return "Adequate potassium aids corn growth, enhancing disease resistance, water stress tolerance, and stalk strength. It promotes: strong cell walls for disease resistance and sturdy stalks; efficient photosynthesis for better crop yield; improved water relations; activation of enzymes; enhanced nutrient absorption; increased drought resistance and protein content; cellulose formation; and reduced lodging."
        elif n < p and n < k:
            return ", it can result in stunted growth, reduced yield, and yellowing of leaves due to insufficient chlorophyll production."
        elif p < n and p < k:
            return "Phosphorus deficiency in corn, displaying a purple or reddish color on the lower leaves and stem. Older leaves are affected before younger leaves. This condition is associated with an accumulation of sugars in P-deficient plants, especially during times of low temperature."
        elif k < n and k < p:
            return "Potassium deficiency in corn manifests as: yellowing or necrosis of leaf margins starting from tip to base, brown scorching, leaf tip curling, chlorosis between veins, purple spots on leaf undersides, reduced grain weight, incomplete grain filling, and premature black layer formation in seeds."
    else:
        return "Invalid values entered"
