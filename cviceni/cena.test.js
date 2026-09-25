import { test } from "node:test";
import assert from "node:assert";
import { vypocitejCenu } from "./cena.js";

test("normální výpočet: 5 hodin * 200 Kč = 1000 Kč", () => {
  assert.strictEqual(vypocitejCenu(5, 200), 1000);
});

test("výsledek pod 500 Kč se zvedne na 500 Kč", () => {
  // 2 * 100 = 200, to je méně než minimum
  assert.strictEqual(vypocitejCenu(2, 100), 500);
});

test("nulové hodiny vrátí minimální cenu 500 Kč", () => {
  assert.strictEqual(vypocitejCenu(0, 300), 500);
});
