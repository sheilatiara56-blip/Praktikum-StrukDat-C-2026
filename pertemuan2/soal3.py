tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}

set3 = tim_frontend.symmetric_difference(tim_backend)
print(set3)

set3 = tim_frontend.difference(tim_backend)
print(set3)

semua_keahlian = tim_backend | tim_frontend
print(semua_keahlian)