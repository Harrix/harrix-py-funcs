import re
import shutil
from pathlib import Path
from typing import Union


def clear_directory(path: Union[Path, str]) -> None:
    """This function clear directory with sub-directories.

    Args:
      path: Path of directory.

    Returns:
      None.

    Examples:
    ```py
    import harrixpylib as h

    h.clear_directory("C:/temp_dir")
    ```
    ```py
    from pathlib import Path
    import harrixpylib as h

    folder = Path(__file__).resolve().parent / "data"
    folder.mkdir(parents=True, exist_ok=True)
    Path(folder / "temp.txt").write_text("Hello, world!", encoding="utf8")
    ...
    h.clear_directory(folder)
    ```
    """
    path = Path(path)
    if path.is_dir():
        shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)


def open_file(filename: Union[Path, str]) -> str:
    """This function open file as UTF8 text file.

    Args:
      filename: Name of the file to open.

    Returns:
      Text file content. If the file could not be opened, an empty string is returned.

    Examples:
    ```py
    import harrixpylib as h

    s = h.open_file("file.txt")
    ```
    ```py
    import harrixpylib as h

    text = "Hello, world!"
    h.save_file(text, "file.txt")

    s = h.open_file("file.txt")
    print(s)
    ```
    """
    try:
        return Path(filename).read_text(encoding="utf8")
    except:
        return ""


def save_file(text: str, filename: Union[Path, str]) -> None:
    """This function save file as UTF8 text file.

    Args:
      text: Text for saving.
      filename: Name of the file to save.

    Returns:
      None.

    Examples:
    ```py
    import harrixpylib as h

    h.save_file("text", "file.txt")
    ```
    ```py
    import harrixpylib as h

    text = "Hello, world!"
    h.save_file(text, "file.txt")

    s = h.open_file("file.txt")
    print(s)
    ```
    """
    Path(filename).write_text(text, encoding="utf8")


def remove_yaml_from_markdown(markdown_text: str) -> str:
    """Function remove YAML from text of markdown file.

    Markdown before processing:
    ```md
    ---
    categories: [it, program]
    tags: [VSCode, FAQ]
    ---

    # Installing VSCode

    ```
    Markdown after processing:
    ```md
    # Installing VSCode
    ```

    Args:
      markdown_text: Text of markdown file.

    Returns:
      Text of markdown file without YAML.

    Example:
    ```py
    from pathlib import Path
    import harrixpylib as h

    md = Path("article.md").read_text(encoding="utf8")
    md_clean = h.remove_yaml_from_markdown(md)
    print(md_clean)
    ```
    """
    return re.sub(r"^---(.|\n)*?---\n", "", markdown_text.lstrip()).lstrip()
