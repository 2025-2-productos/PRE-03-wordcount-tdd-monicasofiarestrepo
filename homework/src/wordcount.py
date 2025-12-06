# Ejemplo para casos de uso
# python3 -m homework data/input data/output


import argparse
import os

from homework.src._internals.read_all_lines import read_all_lines


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def preprocess_lines(lines):
    return [line.strip().lower() for line in lines]


def split_into_words(lines):
    words = []
    for line in lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words


def count_words(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


def write_word_counts(output_folder, word_counts):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save the results using tsv format
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in word_counts.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)
