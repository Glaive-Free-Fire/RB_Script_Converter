# RB_Script_AutoFormatter

## Overview
`RB_Script_AutoFormatter` is a Python script designed to automate the formatting of descriptive text into a predefined template. It processes multi-line descriptions, splits them into fixed-width lines, and incorporates specific rules like custom separators (`(пробел)`), while preserving proper alignment and structure.

This script is particularly useful for game developers working on RPG Maker projects, enabling consistent and efficient text formatting for in-game descriptions.

---

## Features
- **Automatic Line Wrapping**: Splits long descriptions into lines of a specified maximum length.
- **Custom Separators**: Recognizes `(пробел)` as a marker for forced line breaks, adding empty lines in the output.
- **Template Integration**: Formats the text into a predefined structure with placeholders for description and illustration data.
- **Preserves Alignment**: Ensures all lines are right-padded to maintain a consistent appearance.

---

## Prerequisites
- Python 3.6 or higher

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/RB_Script_AutoFormatter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RB_Script_AutoFormatter
   ```

---

## Usage

### Example Input
```python
# Example description text
description_text = (
    """
    Древнее племя крылатых монстров, которых почитали как священных птиц.
    Обладают наивысшим рангом в племени Гарпий, и в древности им поклонялись как Матери-Богине. Их популяция резко сократилась во время Великой Войны Святых и Демонов.
    (пробел)
    Хотя по своей натуре это существо миролюбиво, оно обладает гордостью и никогда не привязывается к тому, кого считает ниже себя.
    (пробел)
    В основном предпочитает мясо, однако похоже не нападает ни на людей, ни на других монстров.
    """
)
illustration_name = "UN_DO"

# Format the text into the template
formatted_template = wrap_text_to_template(description_text, illustration_name)
print(formatted_template)
```

### Example Output
```
    ID_PLACEHOLDER => [
    "Древнее племя крылатых монстров, ",
    "которых почитали как священных   ",
    "птиц. Обладают наивысшим рангом  ",
    "в племени Гарпий, и в древности  ",
    "им поклонялись как Матери-Богине.",
    "Их популяция резко сократилась   ",
    "во время Великой Войны Святых и  ",
    "Демонов.",
    "",  
    "Хотя по своей натуре это существо",
    "миролюбиво, оно обладает         ",
    "гордостью и никогда не           ",
    "привязывается к тому, кого       ",
    "считает ниже себя.",
    "",  
    "В основном предпочитает мясо,   ",
    "однако похоже не нападает ни на ",
    "людей, ни на других монстров.   ",
    "",  
    "Иллюстрация:UN_DO",
    ],
```

---

## Function Reference

### `wrap_text_to_template(description, illustration, max_line_length=37)`
Wraps and formats a description into the specified template.

#### Parameters:
- `description` (str): The text description to be formatted.
- `illustration` (str): The illustration name to include in the template.
- `max_line_length` (int, optional): Maximum character length per line (default is 37).

#### Returns:
- `str`: The formatted text in the specified template.

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

