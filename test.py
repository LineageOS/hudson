#!/usr/bin/env python3
import glob
import json
import unittest


class HudsonTestCase(unittest.TestCase):
    def test_build_targets(self):
        models_json = set()

        with open("updater/devices.json", "r") as f:
            for device in json.load(f):
                self.assertFalse(
                    device["model"] in models_json,
                    f"Duplicate model in devices.json: {device['model']}",
                )
                models_json.add(device["model"])

        models_hudson = set()

        with open("lineage-build-targets", "r") as f:
            for line in f.readlines():
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                model, _, _, _ = line.split()

                self.assertFalse(
                    model in models_hudson,
                    f"Duplicate model in lineage-build-targets: {model}",
                )
                models_hudson.add(model)

        models_missing = models_hudson - models_json

        if models_missing:
            self.fail(f"Missing models in devices.json: {', '.join(models_missing)}")

    def test_json(self):
        for file in glob.glob("updater/*.json"):
            with open(file, "r") as f:
                try:
                    json.load(f)
                except json.JSONDecodeError as e:
                    self.fail(f"Failed to load {file}")


if __name__ == "__main__":
    unittest.main()
