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
                lines.append("".ljust(line_length))  # Пустая строка для разделения
                current_line = ""
            elif len(current_line) + len(word) + 1 > line_length:
                lines.append(current_line.ljust(line_length))
                current_line = word
            else:
                current_line += (" " if current_line else "") + word

        if current_line:
            lines.append(current_line.ljust(line_length))

        return lines

    # Заменяем пустые строки между абзацами на "(пробел)"
    paragraphs = [p.strip() for p in description.split("\n") if p.strip()]
    marked_description = " (пробел) ".join(paragraphs)
    
    # Удаляем переносы строк внутри абзацев
    marked_description = marked_description.replace("\n", " ").strip()
    
    # Разделяем описание на строки
    description_lines = split_text_into_lines(marked_description, max_line_length)

    # Формируем шаблон
    template_lines = ["    ID_PLACEHOLDER => ["]
    for line in description_lines:
        if line.strip() == "":
            template_lines.append(f'    "",')
        else:
            template_lines.append(f'    "{line}",')

    # Добавляем пустую строку и строку иллюстрации
    template_lines.append(f'    "",')
    template_lines.append(f'    "Иллюстрация:{illustration}",')
    template_lines.append("    ],")

    return "\n".join(template_lines)

# Пример использования
description_text = (
    """
    Древнее племя птицеподобных йома, почитаемых как священные птицы. 
    Занимают высшее положение среди племени Гарпий, в древности им поклонялись как Матери Богине, но их численность резко сократилась во время Великой Войны Святых и Демонов. В настоящее время существует лишь одна особь в каждую эпоху, и лишь немногие знают об их существовании. За свою жизнь они откладывают в святилище священной птицы только одно яйцо, оставляя следующему поколению единственного потомка.
    
    Хотя по натуре миролюбивы, они горделивы и никогда не привязываются к тем, кого считают ниже себя. Однако проявляют преданность тому, кого признали своим хозяином, позволяя ему взобраться на спину и парить в небесах на своих величественных крыльях.
    
    Предпочитают мясную пищу, но не нападают ни на людей, ни на других монстров. Из-за особенностей голосового аппарата не могут говорить на человеческом языке, однако обладают достаточно высоким интеллектом и, похоже, понимают речь. Благодаря спокойному характеру не причиняют вред без причины, однако при провокации могут напасть, поэтому следует соблюдать осторожность.
    """
)
illustration_name = "UN_DO"

formatted_template = wrap_text_to_template(description_text, illustration_name)
print(formatted_template)
