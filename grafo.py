grafo = {
    "Lima": ["Callao", "Ica", "Junín", "Áncash"],
    "Callao": ["Lima"],

    "Ica": ["Lima", "Arequipa", "Ayacucho"],
    "Arequipa": ["Ica", "Cusco", "Moquegua"],
    "Moquegua": ["Arequipa", "Tacna", "Puno"],

    "Tacna": ["Moquegua", "Puno"],
    "Puno": ["Tacna", "Moquegua", "Cusco", "Madre de Dios"],

    "Cusco": ["Puno", "Apurímac", "Madre de Dios", "Arequipa"],
    "Apurímac": ["Cusco", "Ayacucho"],
    "Ayacucho": ["Apurímac", "Junín", "Ica", "Huancavelica"],

    "Junín": ["Lima", "Ayacucho", "Huancavelica", "Pasco"],
    "Huancavelica": ["Junín", "Ayacucho"],

    "Pasco": ["Junín", "Huánuco"],
    "Huánuco": ["Pasco", "Ucayali"],

    "Ucayali": ["Huánuco", "Loreto", "Madre de Dios"],
    "Madre de Dios": ["Ucayali", "Cusco"],

    "Loreto": ["Ucayali", "San Martín"],
    "San Martín": ["Loreto", "Amazonas"],
    "Amazonas": ["San Martín", "Cajamarca"],

    "Cajamarca": ["Amazonas", "Lambayeque", "Áncash"],
    "Lambayeque": ["Cajamarca", "Piura", "La Libertad"],
    "Piura": ["Lambayeque", "Tumbes"],
    "Tumbes": ["Piura"],

    "La Libertad": ["Lambayeque", "Áncash"],
    "Áncash": ["La Libertad", "Lima", "Cajamarca"]
}