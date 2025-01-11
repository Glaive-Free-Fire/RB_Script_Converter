def wrap_text_to_template(description, illustration, max_line_length=37):
    """
    Упаковывает текст описания в указанный шаблон.

    :param description: Описание (многострочная строка).
    :param illustration: Имя иллюстрации.
    :param max_line_length: Максимальная длина строки (включая пробелы).
    :return: Отформатированный текст в шаблоне.
    """
    def split_text_into_lines(text, line_length):
        words = text.split()
        lines, current_line = [], ""

        for word in words:
            if word == "(пробел)":
                # Добавляем текущую строку и начинаем новую строку
                if current_line:
                    lines.append(current_line.ljust(line_length))
                lines.append("")  # Пустая строка для разделения
                current_line = ""
            elif len(current_line) + len(word) + 1 > line_length:
                lines.append(current_line.ljust(line_length))
                current_line = word
            else:
                current_line += (" " if current_line else "") + word

        if current_line:
            lines.append(current_line.ljust(line_length))

        return lines

    # Удаляем переносы строк внутри параграфов
    description = description.replace("\n", " ").strip()

    # Разделяем описание на строки
    description_lines = split_text_into_lines(description, max_line_length)

    # Формируем шаблон
    template = "    {id} => [\n".format(id="ID_PLACEHOLDER")
    for line in description_lines:
        if line.strip() == "":
            template += f'    "",\n'
        else:
            template += f'    "{line}",\n'

    # Добавляем пустую строку и строку иллюстрации
    template += f'    "",\n'
    template += f'    "Иллюстрация:{illustration}",\n'
    template += "    ],"

    return template

# Пример использования
description_text = (
    """
    Древнее племя крылатых монстров, которых почитали как священных птиц. 
    Обладают наивысшим рангом в племени Гарпий, и в древности им поклонялись как Матери-Богине. Их популяция резко сократилась во время Великой Войны Святых и Демонов.
    В настоящее время лишь немногие знают, что в каждый исторический период существует лишь одно такое существо. Говорят, что за свою жизнь они откладывают в святилище священной птицы лишь одно яйцо, оставляя следующему поколению лишь одного потомка.
    (пробел)
    Хотя по своей натуре это существо миролюбиво, оно обладает гордостью и никогда не привязывается к тому, кого считает ниже себя.
    Однако говорят, что оно преданно служит тому, кого оно признало своим хозяином, позволяя ему взобраться на свою спину и парить в небесах на своих величественных крыльях.
    (пробел)
    В основном предпочитает мясо, однако похоже не нападает ни на людей, ни на других монстров. Из-за особенностей голосового аппарата не способно говорить на человеческом языке, однако обладает достаточно высоким уровнем интеллекта, и похоже понимает слова.
    Спокойный характер не позволяет ему причинять вред без причины, однако, если его спровоцировать, оно может напасть, поэтому соблюдайте осторожность.
    """
)
illustration_name = "UN_DO"

formatted_template = wrap_text_to_template(description_text, illustration_name)
print(formatted_template)
