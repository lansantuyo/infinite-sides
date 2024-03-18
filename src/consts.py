from typing import List, TypedDict

DEFAULT_SYSTEM_MSG = """
You are playing as a historian tasked with combining elements from the Japanese Occupation in 
the Philippines to uncover deeper insights into this period. Use emojis to represent key figures, events, 
and concepts, and combine them to reveal new understandings or outcomes.

For example:
"🇯🇵 Japanese Expansionism" + "🌾 Rice & Food Shortages" could result in "📉 Economic Hardship"
or
"🏰 Manila Declared Open City" + "✈️ Japanese Air Raid" could result in "🔥 Manila in Flames"

Your task is to interpret combinations and provide results that reflect the historical interactions or consequences 
of these elements. The input format will be: "emoji Text + emoji Text", and your result should always be in the 
"emoji Text" format. Aim to use emojis that closely relate to the text for an immersive experience.

Here are some elements from the document to get you started:

- "👑 Manuel L. Quezon + 🛡️ National Defense Plan" = "🏰 Preparation for War"
- "💣 Pearl Harbor Bombing + 🌍 Philippines" = "🕰️ Start of Occupation"
- "👣 Bataan Death March + 🚶‍♂️ POWs" = "😢 Suffering and Hardship"
- "⚔️ Guerilla Warfare + 🌳 Philippine Jungles" = "🛡️ Resistance Efforts"
- "🇺🇸 Douglas MacArthur + 🗣️ 'I Shall Return'" = "🏖️ Leyte Landing"

Experiment with different combinations to explore the occupation's narrative. Your combinations and results will 
contribute to a deeper understanding of this historical period. Remember, the goal is to keep the emoji as closely 
related to the text as possible and maintain consistency throughout your responses.
"""


class ExampleEntry(TypedDict):
    from_str: str
    result_str: str


ExampleType = List[ExampleEntry]

DEFAULT_BASE_URL = "http://localhost:11434/v1"
DEFAULT_EXAMPLES: ExampleType = [
    # Basic
    {"from_str": "🌍 Earth + 🌍 Earth", "result_str": "🏝️ Island"},
    {"from_str": "🌍 Earth + 💧 Water", "result_str": "🌱 Plant"},
    {"from_str": "🌍 Earth + 🌱 Plant", "result_str": "🌳 Tree"},
    {"from_str": "🌳 Tree + 🌳 Tree", "result_str": "🌳 Forest"},
    {"from_str": "🌳 Tree + 👤 Person", "result_str": "🌲 Wood"},
    {"from_str": "⬆️ North + ⬇️ South", "result_str": "🎯 Middle"},
    {"from_str": "⬅️ West + ➡️ East", "result_str": "🎯 Middle"},
    {"from_str": "🏛️ Institution + 👥 People", "result_str": "🏛️ Government"},
    {"from_str": "🕊️ Peacetime + 🏛️ Government", "result_str": "📜 Treaty"},

    {"from_str": "🔥 Fire + 🔫 Weapon", "result_str": "💣️ Bomb"},
    {"from_str": "🔥 Fire + 💣️ Bomb", "result_str": "💥 Explosion"},
    {"from_str": "💣️ Bomb + 💣️ Bomb", "result_str": "💥 Explosion"},

    {"from_str": "🌲 Wood + 💧 Water", "result_str": "🚤 Boat"},
    {"from_str": "🛶 Boat + 💨 Wind", "result_str": "🛩️ Airplane"},

    {"from_str": "👤 Person + 💴 Money", "result_str": "🧑‍💼 Merchant"},
    {"from_str": "👤 Person + 👤 Person", "result_str": "👥 People"},
    {"from_str": "👤 Person + 🇯🇵 Japan", "result_str": "👤 Japanese"},
    {"from_str": "👤 Person + 🇵🇭 Philippines", "result_str": "👤 Filipino"},
    {"from_str": "👤 Person + 🇺🇸 United States", "result_str": "👤 American"},
    {"from_str": "👤 Person + 🇨🇳 China", "result_str": "👤 Chinese"},

    {"from_str": "👤 Person + 🔫 Weapon", "result_str": "🪖 Soldier"},
    {"from_str": "🪖 Soldier + 🪖 Soldier", "result_str": "🪖 Troops"},
    {"from_str": "🪖 Troops + 🪖 Soldier", "result_str": "🎖️ General"},
    {"from_str": "👤 American + 🪖 Soldier", "result_str": "🪖 American Soldier"},
    {"from_str": "👤 Filipino + 🪖 Soldier", "result_str": "🪖 Filipino Soldier"},
    {"from_str": "👤 Japanese + 🪖 Soldier", "result_str": "🪖 Japanese Soldier"},
    {"from_str": "👤 Chinese + 🪖 Soldier", "result_str": "🪖 Chinese Soldier"},
    {"from_str": "🪖 American Soldier + 🪖 American Soldier", "result_str": "👥 American Troops"},
    {"from_str": "🪖 Filipino Soldier + 🪖 Filipino Soldier", "result_str": "👥 Filipino Troops"},
    {"from_str": "🪖 Japanese Soldier + 🪖 Japanese Soldier", "result_str": "👥 Japanese Troops"},
    {"from_str": "🪖 Chinese Soldier + 🪖 Chinese Soldier", "result_str": "👥 Chinese Troops"},
    {"from_str": "👥 Japanese Troops +🛶 Boat", "result_str": "🛶 Japanese Ship"},
    {"from_str": "👥 American Troops +🛶 Boat", "result_str": "🛶 American Ship"},
    {"from_str": "🛶 Japanese Ship +🛶 Japanese Ship", "result_str": "🛶 Japanese Navy"},
    {"from_str": "🛶 American Ship +🛶 American Ship", "result_str": "🛶 American Navy"},
    {"from_str": "🛶 Boat + 🪖 Soldier", "result_str": "⚓ Naval Power"},
    {"from_str": "🛶 Boat + 🪖 Troops", "result_str": "⚓ Naval Power"},
    {"from_str": "🛶 Boat + 🪖 General", "result_str": "⚓ Naval Power"},
    {"from_str": "🛩️ Airplane + 🪖 Soldier", "result_str": "✈️ Air Power"},
    {"from_str": "🛩️ Airplane + 🪖 Troops", "result_str": "✈️ Air Power"},
    {"from_str": "🛩️ Airplane + 🪖 General", "result_str": "✈️ Air Power"},
    {"from_str": "🌳 Forest + 🪖 Troops", "result_str": "🌳 Guerrilla Troops"},

    {"from_str": "🌱 Plant + 🏙️ Manila", "result_str": "🌿 Hemp"},
    {"from_str": "💴 Money + 🇯🇵 Japan", "result_str": " 💵 Mickey Mouse Money"},
    {"from_str": "🧑‍💼 Oda Kyosaburo + 🏙️ Manila", "result_str": "🏭 Ota Development Corporation"},
    {"from_str": "🏭 Factory + 🇯🇵 Oda Kyosaburo", "result_str": "🏭 Ota Development Corporation"},
    {"from_str": "🛡️ Defense + 🇵🇭 Philippines", "result_str": "📜 National Defense Plan"},
    {"from_str": "🏛️ Government + 🇵🇭 Philippines", "result_str": "📜 National Defense Plan"},
    {"from_str": "📃 Policy + 👨‍💼 Manuel L. Quezon", "result_str": "🛡️Civilian Emergency Administration"},
    {"from_str": "🌍 Earth + 🏛️ Institution", "result_str": "🏛️ League of Nations"},
    {"from_str": "👥 Japanese Troops +  🇯🇵 Japan",  "result_str": "🤝 Tripartite Pact"},
    {"from_str": "⚠️ War + 🇯🇵 Japan",  "result_str": "🤝 Tripartite Pact"},
    {"from_str": "👥 Filipino Troops + 🗻 Bataan", "result_str": "🌈 Rainbow Plan 5"},
    {"from_str": "⚠️ War + 🌈 Rainbow Plan 5", "result_str": "⚠️ War Plan Orange 3"},
    {"from_str": "🎖️ Douglas MacArthur" + "🌈 Rainbow Plan 5", "result_str": "⚠️ War Plan Orange 3"},
    {"from_str": "🇵🇭 Philippines + 📈 Business", "result_str": "🤪 Anti-Dummy Law"},
    {"from_str": "💴 Money + 📈 Business", "result_str": "🤪 Anti-Dummy Law"},
    {"from_str": "📃 Policy + 📈 Business", "result_str": "🤪 Anti-Dummy Law"},
    {"from_str": "🌾 Rice + 📈 Business", "result_str": "🍚 Bigasang Bayan"},
    {"from_str": "🌾 Rice + 💴 Money", "result_str": "🍚 Bigasang Bayan"},
    {"from_str": "🌾 Rice + 🧑‍💼 Merchant", "result_str": "🍚 Bigasang Bayan"},
    {"from_str": "🌾 Rice + 👤 Filipino", "result_str": "🍚 Bigasang Bayan"},
    {"from_str": "🇺🇸 America + 📜 Treaty", "result_str": "✍️ Hull Note"},
    {"from_str": "🇯🇵 Japan + 📜 Treaty", "result_str": "✍️ Hull Note"},
    {"from_str": "🌾 Rice + ⛩️ Japanese Occupation", "result_str": "🌾 Rice Crisis"},
    {"from_str": "🌾 Rice + 💴 Money", "result_str": "🌾 Rice Crisis"},



    # People
    {"from_str": "👤 Filipino + 🏛️ Government", "result_str": "👨‍💼 Manuel L. Quezon"},
    {"from_str": "👤 Filipino + 🇵🇭 Philippines", "result_str": "👨‍💼 Manuel L. Quezon"},
    {"from_str": "🧑‍💼 Merchant + 👤 Japanese", "result_str": "🧑‍💼 Oda Kyosaburo"},
    {"from_str": "🧑‍💼 Merchant + 🇯🇵 Japan", "result_str": "🧑‍💼 Oda Kyosaburo"},
    {"from_str": "🎖️ General + 👤 American", "result_str": "🎖️ Douglas MacArthur"},
    {"from_str": "🎖️ General + 🇯🇵 Japan", "result_str": "🎖️ Masaharu Homma"},
    {"from_str": "🎖️ General + 👤 Japanese", "result_str": "🎖️ Masaharu Homma"},

    # Places
    {"from_str": "🏝️ Island + 🇵🇭 Philippines", "result_str": "🏝️ Philippine Islands"},
    {"from_str": "🏝️ Philippine Islands + ⬆️ North", "result_str": "🏝️ Luzon"},
    {"from_str": "🏝️ Philippine Islands + 🎯 Middle", "result_str": "🏝️ Visayas"},
    {"from_str": "🏝️ Philippine Islands + ⬇️ South", "result_str": "🏝️ Mindanao"},
    {"from_str": "🏙️ City + 🏝️ Luzon", "result_str": "🏙️ Manila"},
    {"from_str": "🏙️ City + 🏝️ Mindanao", "result_str": "🏙️ Davao"},
    {"from_str": "🏝️ Island + 🏝️ Visayas", "result_str": "🏝️ Leyte"},
    {"from_str": "🇨🇳 China + 👥 Japanese Troops", "result_str": "🎌 Manchukuo"},
    {"from_str": "⬅️ West + 🏝️ Luzon", "result_str": "🗻 Bataan"},
    {"from_str": "🎯 Middle + 🏝️ Luzon", "result_str": "🌾 San Fernando"},
    {"from_str": "⬆️ North + 🌾 San Fernando", "result_str": "🌾 Tarlac"},
    {"from_str": "🌾 San Fernando + 👥 American Troops ", "result_str": "⛺️ Camp O’Donnell"},

    # Institutions
    {"from_str": "🏭 Factory + 🧑‍💼 Oda Kyosaburo", "result_str": "🏭 Ota Development Corporation"},

    # Events
    {"from_str": "🧑‍💼 Oda Kyosaburo + 🗻 Bataan", "result_str": "☠️ Bataan Death March"},
    {"from_str": "🪖 Masaharu Homma + 🗻 Bataan", "result_str": "☠️ Bataan Death March"},
    {"from_str": "🌴 Bataan + 🌴 San Fernando", "result_str": "☠️ Bataan Death March"},
    {"from_str": "🇺🇸 America + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
    {"from_str": "🇯🇵 Japan + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
    {"from_str": "👥 Japanese Troops + 👥 Chinese Troops", "result_str": "🪖 2nd Sino-Japanese War"},
    {"from_str": "🛶 Boat + 🏝️ Leyte", "result_str": "🏝️ Leyte Landing"},
    {"from_str": "⚓ Naval Power + 🏝️ Leyte", "result_str": "⚔️ Battle of Leyte Gulf"},

    # Narrative
    {"from_str": "🕊️ Peacetime + 👨‍💼 Manuel L. Quezon", "result_str": "🏛️ Start of the Commonwealth"},
    {"from_str": "🏛️ Government + 👨‍💼 Manuel L. Quezon", "result_str": "🏛️ Start of the Commonwealth"},
    {"from_str": "🏛️ Government + 📜 Treaty", "result_str": "🏛️ Start of the Commonwealth"},
    {"from_str": "🏛️ Government" + "📃 Policy", "result_str": "🏛️ Start of the Commonwealth"},
    {"from_str": "👤 Manuel Quezon + 🇺🇸 United States", "result_str": "🇵🇭 Start of the Commonwealth"},

    {"from_str": "🇺🇸 America + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
    {"from_str": "🇯🇵 Japan + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
    {"from_str": "✈️ Air Power + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},

    {"from_str": "🕊️ Peacetime + 💣 Pearl Harbor Bombing", "result_str": "⛩️ Japanese Occupation"},
    {"from_str": "🕊️ Peacetime + 👥 Japanese Troops", "result_str": "⛩️ Japanese Occupation"},
    {"from_str": "🕊️ Peacetime + 💣 Pearl Harbor Bombing", "result_str": "⛩️ Japanese Occupation"},
    {"from_str": "🇯🇵 Japan + 🇵🇭 Philippines", "result_str": "🇵🇭 Japanese Occupation"},

    {"from_str": "⛩️ Japanese Occupation +  🇵🇭 Philippines", "result_str": "🇵🇭 Philippine Resistance"},
    {"from_str": "⛩️ Japanese Occupation + 👤 Filipino", "result_str": "🇵🇭 Philippine Resistance"},
    {"from_str": "⛩️ Japanese Occupation + 👥 Filipino Troops", "result_str": "🇵🇭 Philippine Resistance"},

    {"from_str": "🇵🇭 Philippine Resistance + 💣 Bataan Death March", "result_str": "✊ Guerrilla Warfare"},
    {"from_str": "🌳 Guerrilla Troops + 👥 Japanese Troops", "result_str": "✊ Guerrilla Warfare"},

    {"from_str": "🛶 Boat + 🏝️ Leyte", "result_str": "🏝️ Leyte Gulf Landing"},

    {"from_str": "⚓ Naval Power + 🏝️ Leyte", "result_str": "⚔️ Battle of Leyte Gulf"},
    {"from_str": "⚠️ War + 🏝️ Leyte Gulf Landing", "result_str": "⚔️ Battle of Leyte Gulf"},
    {"from_str": "💥 Explosion + 🏝️ Leyte Gulf Landing", "result_str": "⚔️ Battle of Leyte Gulf"},
    {"from_str": "👥 Japanese Troops + 🏝️ Leyte Gulf Landing", "result_str": "⚔️ Battle of Leyte Gulf"},
    {"from_str": "👥 American Troops + 🏝️ Leyte Gulf Landing", "result_str": "⚔️ Battle of Leyte Gulf"},

    {"from_str": "🇺🇸 United States + 🏙️ Manila", "result_str": "🎉 Liberation of Manila"},
    {"from_str": "📃 Policy + 🏙️ Manila", "result_str": "🎉 Liberation of Manila"},
    {"from_str": "👥 American Troops + 🏙️ Manila", "result_str": "🎉 Liberation of Manila"},

    {"from_str": "🇵🇭 Philippines + 🕊️ Peacetime", "result_str": "🇵🇭 Proclamation of Philippine Liberation"},
    {"from_str": "🏛️ Start of the Commonwealth + 🏛️ Government", "result_str": "🇵🇭 Proclamation of Philippine Liberation"},


    # Others
    {"from_str": "🇵🇭 Philippines + 👨‍💼Manuel L. Quezon", "result_str": "🛡️Civilian Emergency Administration"},
    {"from_str": "🇺🇸 America + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
    {"from_str": "🇺🇸 America + 💥 Explosion", "result_str": "💣 Pearl Harbor Bombing"},
]

DEFAULT_CHIPS = [
    "🌍 Earth",
    "💨 Wind",
    "💧 Water",
    "🔥 Fire",
    "👤 Person",
    "🇯🇵 Japan",
    "🇵🇭 Philippines",
    "🇺🇸 America",
    "🇨🇳 China",
    "💴 Money",
    "🏙️ City",
    "🔫 Weapon",
    "🏛️ Institution",
    "🏝️ Island",
    "⬆️ North",
    "⬇️ South",
    "⬅️ West",
    "➡️ East",
    "📃 Policy",
    "🌾 Rice",
    "📈 Business",
    "⚠️ War",
    "🛡️ Defense",
    "🕊️ Peacetime",
]

MODELS = [
    "llama2",
    "mistral",
    "llava"
]

DEFAULT_MODEL = "llama2"
