import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TelegrafConfigTest(unittest.TestCase):
    def test_mqtt_consumer_subscribes_only_to_eight_level_measurement_topics(self):
        config = (ROOT / "telegraf.conf").read_text(encoding="utf-8")

        topics_match = re.search(r'^\s*topics\s*=\s*\["([^"]+)"\]', config, re.MULTILINE)

        self.assertIsNotNone(topics_match)
        self.assertEqual(topics_match.group(1), "C-S/+/+/+/+/+/+/+")


if __name__ == "__main__":
    unittest.main()
