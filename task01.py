from pathlib import Path
import shutil
import sys


def copy_and_sort_files(current_source: Path, dest_root: Path):
	try:
		for item in current_source.iterdir():
			if item.is_dir():
				copy_and_sort_files(item, dest_root)
				
			elif item.is_file():
				extension = item.suffix.lstrip(".").lower()
				if not extension:
					extension = "no_extension"
				target_directory = dest_root / extension
				try:
					target_directory.mkdir(parents=True, exist_ok=True)
					target_file_path = target_directory / item.name
					shutil.copy2(item, target_file_path)
					print(f"Скопійовано: '{item}' -> '{target_file_path}'")
				except Exception as e:
					print(f"Помилка при копіюванні файлу '{item}': {e}")

	except Exception as e:
		print(f"Помилка доступу до директорії '{current_source}': {e}")


def main():
	if len(sys.argv) < 3:
		print("Використання: python script.py [шлях_до_джерела] [шлях_до_призначення]")
		return

	source_path = Path(sys.argv[1])
	dest_path = Path(sys.argv[2])
	if not source_path.exists() or not source_path.is_dir():
		print(f"Помилка: Вихідна директорія '{source_path}' не існує або не є папкою")
		return

	print(f"Початок копіювання з '{source_path}' у '{dest_path}'...")
	copy_and_sort_files(source_path, dest_path)
	print("Процес успішно завершено!")


if __name__ == "__main__":
	main()