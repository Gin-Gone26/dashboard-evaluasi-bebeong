QUESTION_GROUPS = {
    "PU": {
        "label": "Perceived Usefulness",
        "questions": {
            "PU1": "Website BEBEONG membantu saya memperoleh informasi atau layanan dengan lebih cepat.",
            "PU2": "Website BEBEONG mempermudah saya dalam mengakses layanan pemerintahan.",
            "PU3": "Website BEBEONG meningkatkan efektivitas saya dalam memperoleh informasi atau layanan.",
            "PU4": "Website BEBEONG membantu menghemat waktu dalam mengakses layanan pemerintahan.",
            "PU5": "Website BEBEONG memberikan manfaat dalam memenuhi kebutuhan layanan saya.",
            "PU6": "Website BEBEONG membantu saya memperoleh layanan secara lebih efisien dibandingkan cara konvensional.",
            "PU7": "Secara keseluruhan Website BEBEONG bermanfaat bagi saya.",
        },
    },
    "PEOU": {
        "label": "Perceived Ease of Use",
        "questions": {
            "PEOU1": "Website BEBEONG mudah dipelajari.",
            "PEOU2": "Menu dan fitur Website BEBEONG mudah dipahami.",
            "PEOU3": "Saya dapat menggunakan Website BEBEONG tanpa mengalami kesulitan berarti.",
            "PEOU4": "Tampilan Website BEBEONG mudah dipahami.",
            "PEOU5": "Interaksi dengan Website BEBEONG terasa mudah dilakukan.",
            "PEOU6": "Saya dapat dengan mudah menemukan layanan yang saya butuhkan pada Website BEBEONG.",
            "PEOU7": "Proses penggunaan Website BEBEONG mudah untuk diingat.",
        },
    },
    "BI": {
        "label": "Behavioral Intention",
        "questions": {
            "BI1": "Saya berminat menggunakan Website BEBEONG kembali di masa mendatang.",
            "BI2": "Saya akan menggunakan Website BEBEONG apabila membutuhkan layanan pemerintahan.",
            "BI3": "Saya bersedia merekomendasikan Website BEBEONG kepada orang lain.",
            "BI4": "Saya memiliki keinginan untuk terus menggunakan layanan yang tersedia pada Website BEBEONG.",
            "BI5": "Saya lebih memilih menggunakan Website BEBEONG dibandingkan proses pelayanan secara manual apabila tersedia.",
            "BI6": "Saya akan tetap menggunakan Website BEBEONG apabila terdapat pengembangan layanan di masa mendatang.",
        },
    },
}

QUESTION_COLUMNS = [
    question_code
    for group in QUESTION_GROUPS.values()
    for question_code in group["questions"].keys()
]

LIKERT_OPTIONS = {
    1: "1 - Sangat Tidak Setuju",
    2: "2 - Tidak Setuju",
    3: "3 - Netral",
    4: "4 - Setuju",
    5: "5 - Sangat Setuju",
}

EDUCATION_OPTIONS = ["SMA/SMK", "D3", "S1", "S2", "S3"]
