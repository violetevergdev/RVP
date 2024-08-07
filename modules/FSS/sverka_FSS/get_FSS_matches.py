import os
import pandas as pd


def get_FSS_matches(c, fss_db, vib_db, out_dir='OUT'):
    # Выполняем запрос
    query = c.execute(f'''select distinct *
from {fss_db} as f
join {vib_db} as v on
     f.СНИЛС == v.npers
group by f.СНИЛС''')

    # Получаем DataFrame
    results = pd.DataFrame(query, columns=[col[0] for col in c.description])

    # Устанавливаем выходной путь
    out = os.path.join(out_dir, 'Обработанный список ФСС.xlsx')

    # Записываем данные
    writer = pd.ExcelWriter(out)
    results.to_excel(writer, index=False)

    writer.close()