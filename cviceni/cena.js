// Minimální cena za jednu zakázku (v Kč)
const MINIMALNI_CENA = 500;

// Spočítá cenu zakázky: hodiny * sazba, ale nikdy méně než minimální cena
export function vypocitejCenu(hodiny, sazba) {
  const cena = hodiny * sazba;
  if (cena < MINIMALNI_CENA) {
    return MINIMALNI_CENA;
  }
  return cena;
}
