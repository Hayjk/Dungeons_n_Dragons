from model import bones, bones_ability, ability_manna
from view import message
from view import text
class Entity:
    def __init__(self, name: str, experience: int, manna: int, ability: str):
        self.name = name
        self.experience = experience
        self.manna = manna
        self.ability = ability

    def specifications(self) -> str:
        return f'существо: {self.name} | опыт: {self.experience} | ' \
               f'манна: {self.manna} | способность: {self.ability}'

    def count_experience(self) -> int:
        self.experience = self.experience + (bones() // 2)
        return self.experience

    def count_ability(self) -> int:
        self.experience = self.experience + bones_ability()
        return self.experience


    def subtraction_experience_1(self) -> int:
        if self.experience > 0:
            self.experience = self.experience - 1
            return self.experience
        return message(text.error_experience)

    def subtraction_experience_2(self) -> int:
        if self.experience > 0:
            self.experience = self.experience - 2
            return self.experience
        return message(text.error_experience)

    def subtraction_experience_3(self) -> int:
        if self.experience > 0:
            self.experience = self.experience - 3
            return self.experience
        return message(text.error_experience)

    def subtraction_experience_5(self) -> int:
        if self.experience > 0:
            self.experience = self.experience - 5
            return self.experience
        return message(text.error_experience)

    def enchanter_ability(self):
        self.manna = self.manna + ability_manna()
        return self.manna

    def subtraction_manna_2(self) -> int:
        if self.manna > 0:
            self.manna = self.manna - 2
            return self.manna
        return message(text.error_manna)

    def subtraction_manna_3(self) -> int:
        if self.manna > 0:
            self.manna = self.manna - 3
            return self.manna
        return message(text.error_manna)

    def subtraction_manna_4(self) -> int:
        if self.manna > 0:
            self.manna = self.manna - 4
            return self.manna
        return message(text.error_manna)

    def count_manna_experience(self) -> int:
        if self.manna > 0 and self.experience > 0:
            self.experience = self.experience + self.manna
            return self.experience
        return self.experience

    def count_end(self) -> str:
        if self.experience >= 10:
            return message(text.end_history_win)
        return message(text.end_history_lose)

    def count_end_fury(self) -> str:
        if self.experience >= 13:
            return message(text.end_history_win)
        return message(text.end_history_lose)


human = Entity('Человек', 0, None, '---')
enchanter = Entity('Чародей', 0, 0, '---')
fury = Entity('Фурия', 0, None, '+++')