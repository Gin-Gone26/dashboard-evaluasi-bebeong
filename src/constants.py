QUESTION_GROUPS = {
    "PU": {
        "label": "Perceived Usefulness",
        "questions": {
            "PU1": "Aplikasi BEBEONG Banjar Super Apps membantu saya memperoleh informasi atau layanan dengan lebih cepat.",
            "PU2": "Aplikasi BEBEONG Banjar Super Apps mempermudah saya dalam mengakses layanan pemerintahan.",
            "PU3": "Aplikasi BEBEONG Banjar Super Apps meningkatkan efektivitas saya dalam memperoleh informasi atau layanan.",
            "PU4": "Aplikasi BEBEONG Banjar Super Apps membantu menghemat waktu dalam mengakses layanan pemerintahan.",
            "PU5": "Aplikasi BEBEONG Banjar Super Apps memberikan manfaat dalam memenuhi kebutuhan layanan saya.",
            "PU6": "Aplikasi BEBEONG Banjar Super Apps membantu saya memperoleh layanan secara lebih efisien dibandingkan cara konvensional.",
            "PU7": "Secara keseluruhan Aplikasi BEBEONG Banjar Super Apps bermanfaat bagi saya.",
        },
    },
    "PEOU": {
        "label": "Perceived Ease of Use",
        "questions": {
            "PEOU1": "Aplikasi BEBEONG Banjar Super Apps mudah dipelajari.",
            "PEOU2": "Menu dan fitur Aplikasi BEBEONG Banjar Super Apps mudah dipahami.",
            "PEOU3": "Saya dapat menggunakan Aplikasi BEBEONG Banjar Super Apps tanpa mengalami kesulitan berarti.",
            "PEOU4": "Tampilan Aplikasi BEBEONG Banjar Super Apps mudah dipahami.",
            "PEOU5": "Interaksi dengan Aplikasi BEBEONG Banjar Super Apps terasa mudah dilakukan.",
            "PEOU6": "Saya dapat dengan mudah menemukan layanan yang saya butuhkan pada Aplikasi BEBEONG Banjar Super Apps.",
            "PEOU7": "Proses penggunaan Aplikasi BEBEONG Banjar Super Apps mudah untuk diingat.",
        },
    },
    "BI": {
        "label": "Behavioral Intention",
        "questions": {
            "BI1": "Saya berminat menggunakan Aplikasi BEBEONG Banjar Super Apps kembali di masa mendatang.",
            "BI2": "Saya akan menggunakan Aplikasi BEBEONG Banjar Super Apps apabila membutuhkan layanan pemerintahan.",
            "BI3": "Saya bersedia merekomendasikan Aplikasi BEBEONG Banjar Super Apps kepada orang lain.",
            "BI4": "Saya memiliki keinginan untuk terus menggunakan layanan yang tersedia pada Aplikasi BEBEONG Banjar Super Apps.",
            "BI5": "Saya lebih memilih menggunakan Aplikasi BEBEONG Banjar Super Apps dibandingkan proses pelayanan secara manual apabila tersedia.",
            "BI6": "Saya akan tetap menggunakan Aplikasi BEBEONG Banjar Super Apps apabila terdapat pengembangan layanan di masa mendatang.",
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

