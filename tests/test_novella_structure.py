#!/usr/bin/env python3
import os
import unittest

class TestNovellaStructure(unittest.TestCase):
    def setUp(self):
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.chapters_dir = os.path.join(self.root, "chapters")
        self.expected_chapters = [
            "chapter_1_the_genesis_tick.md",
            "chapter_2_relativistic_slashing.md",
            "chapter_3_the_fork_of_ganymede.md",
            "chapter_4_zero_knowledge_horizon.md",
            "chapter_5_immutable_consensus.md"
        ]

    def test_chapter_existence(self):
        for ch in self.expected_chapters:
            p = os.path.join(self.chapters_dir, ch)
            self.assertTrue(os.path.exists(p), f"Chapter {ch} is missing!")

    def test_core_documentation(self):
        self.assertTrue(os.path.exists(os.path.join(self.root, "README.md")))
        self.assertTrue(os.path.exists(os.path.join(self.root, "WORLD_LORE.md")))
        self.assertTrue(os.path.exists(os.path.join(self.root, "CHARACTERS.md")))

    def test_total_word_count(self):
        total_words = 0
        for ch in self.expected_chapters:
            with open(os.path.join(self.chapters_dir, ch), "r", encoding="utf-8") as f:
                words = len(f.read().split())
                self.assertGreater(words, 300, f"Chapter {ch} too short ({words} words)")
                total_words += words
        print(f"\nVerified total novella word count: {total_words} words across 5 chapters.")
        self.assertGreater(total_words, 2000, "Novella total word count below threshold!")

if __name__ == "__main__":
    unittest.main()
