from food import (
    oat,
    protein_on,
    protein_powerbuff,
    nut,
    rice,
    vegetable,
    chicken,
    banana,
    beef_hm,
    sauce,
    tomato,
    oil,
    jisuan,
    egg,
)
from month import month
from meal import meal
from body import body
from eval import evaluator

morning = meal(oat(55), protein_powerbuff(40), nut(190))
former = meal(oat(35), beef_hm(200), tomato(250))
last = meal(banana(2), protein_powerbuff(35), jisuan(3), tomato(250))
june = month(morning, former, last)
june_body = body(24, 179, 90, (1, 1.2, 1.5), 500)

morning = meal(oat(55), protein_powerbuff(35), nut(175))
former = meal(oat(30), beef_hm(200), tomato(250))
last = meal(banana(2), protein_powerbuff(35), jisuan(3), tomato(250))
july = month(morning, former, last)
july_body = body(24, 179, 84.5, (1, 1.2, 1.5), 500)

morning = meal(oat(45), protein_powerbuff(35), nut(170))
former = meal(oat(30), beef_hm(170), tomato(250))
last = meal(banana(2), protein_powerbuff(35), jisuan(3), tomato(250))
aug = month(morning, former, last)
aug_body = body(24, 179, 79.5, (1, 1.2, 1.5), 500)

morning = meal(oat(150), protein_powerbuff(55), nut(40), oil())
former = meal(oat(80), tomato(250))
last = meal(rice(150), beef_hm(200), vegetable(200), jisuan(3))
sep = month(morning, former, last)
sep_body = body(24, 179, 75, (2.5, 1.2, 0.5), 300)

rest = meal(rice(100), protein_on(35), beef_hm(200), tomato(500), egg(10))

eval = evaluator(sep_body, sep)
eval._print()
# june._print()

# 88，105，130
