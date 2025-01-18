from pathlib import Path
from tempfile import TemporaryDirectory

import harrix_pylib as h


def test_add_author_book():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/add_author_book__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/add_author_book__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.add_author_book(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")
        md_after = md_after.replace("Name Surname", Path(temp_folder).name)

    assert md_after == md_applied


def test_add_image_captions():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/add_image_captions__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/add_image_captions__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.add_image_captions(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")

    assert md_after == md_applied


def test_get_yaml_from_markdown():
    md = Path(h.dev.get_project_root() / "tests/data/get_yaml.md").read_text(encoding="utf8")
    md_clean = h.md.get_yaml(md)
    assert len(md_clean.splitlines()) == 4


def test_remove_yaml_from_markdown():
    md = Path(h.dev.get_project_root() / "tests/data/get_yaml.md").read_text(encoding="utf8")
    md_clean = h.md.remove_yaml(md)
    assert len(md_clean.splitlines()) == 1


def test_sort_sections():
    current_folder = h.dev.get_project_root()
    md = Path(current_folder / "tests/data/sort_sections__before.md").read_text(encoding="utf8")
    md_after = Path(current_folder / "tests/data/sort_sections__after.md").read_text(encoding="utf8")

    with TemporaryDirectory() as temp_folder:
        temp_filename = Path(temp_folder) / "temp.md"
        temp_filename.write_text(md, encoding="utf-8")
        h.md.sort_sections(temp_filename)
        md_applied = temp_filename.read_text(encoding="utf8")

    assert md_after == md_applied


def test_split_yaml_content():
    md = Path(h.dev.get_project_root() / "tests/data/get_yaml.md").read_text(encoding="utf8")
    yaml, content = h.md.split_yaml_content(md)
    assert len(yaml.splitlines()) + len(content.splitlines()) == 5


def test_identify_code_blocks():
    md = Path(h.dev.get_project_root() / "tests/data/add_image_captions__before.md").read_text(encoding="utf8")
    _, content = h.md.split_yaml_content(md)
    count_lines_content = 0
    count_lines_code = 0
    for _, state in h.md.identify_code_blocks(content.splitlines()):
        print(_)
        if state:
            count_lines_code+= 1
        else:
            count_lines_content+= 1
    assert count_lines_code == 9
    assert count_lines_content == 22


def test_add_note():
    with TemporaryDirectory() as temp_dir:
        base_path = Path(temp_dir)
        # Test with images
        name = "test_note"
        text = "# Test Note\nThis is a test note with images."
        is_with_images = True

        result_msg, result_path = h.md.add_note(base_path, name, text, is_with_images)

        # Check if the message indicates file creation
        assert "File" in result_msg

        # Check if the note file exists
        note_file = base_path / f"{name}/{name}.md"
        assert note_file.is_file()

        # Check if the image folder was created
        img_folder = base_path / f"{name}/img"
        assert img_folder.is_dir()

        # Verify content of the note file
        with note_file.open('r', encoding='utf-8') as file:
            assert file.read().strip() == text

        # Test without images
        name = "test_note_no_images"
        text = "# Simple Note\nThis note has no images."
        is_with_images = False

        result_msg, result_path = h.md.add_note(base_path, name, text, is_with_images)

        # Check if the message indicates file creation
        assert "File" in result_msg

        # Check if the note file exists at the base path
        note_file_no_images = base_path / f"{name}.md"
        assert note_file_no_images.is_file()

        # Verify content of the note file
        with note_file_no_images.open('r', encoding='utf-8') as file:
            assert file.read().strip() == text

        # Check that there's no image folder created
        assert not (base_path / f"{name}/img").exists()
