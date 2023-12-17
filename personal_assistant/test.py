import dropbox

# Ваш токен доступу до Dropbox API
ACCESS_TOKEN = 'sl.Br0sOwOuzA2mWSTFkWT2B4VezL0eCMAskfqcgfcyDU_dUtW0_AupYSYgQnL0XcVagKXgT3KAMhF64isC6G44nasnm7yR2PD9HBVs9f4WT8UsUD67OeBHz-2dz5EdpfcoSeSzm0dA61S0'

# Створення об'єкту Dropbox
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Приклад виклику методу Dropbox API
account_info = dbx.users_get_current_account()

# Вивід інформації про аккаунт (якщо токен дійсний)
print(account_info)