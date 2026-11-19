"""
Script para converter os CSVs extraídos pelo DAX Studio (em data/extracted)
para o formato colunar Parquet (em data/parquet ou data/gold).

Pré-requisito: pyarrow instalado (uv add pyarrow ou pip install pyarrow)
"""

import sys
from pathlib import Path
import pandas as pd

# Pastas de entrada e saída
BASE_DIR = Path(__file__).resolve().parents[2] if "__file__" in locals() else Path.cwd()
EXTRACTED_DIR = BASE_DIR / "data" / "extracted"
PARQUET_DIR = BASE_DIR / "data" / "parquet"

PARQUET_DIR.mkdir(parents=True, exist_ok=True)


def converter_csv_para_parquet():
    csv_files = list(EXTRACTED_DIR.glob("*.csv"))
    if not csv_files:
        print(f"[!] Nenhum arquivo CSV encontrado em: {EXTRACTED_DIR}")
        return

    print(f"Iniciando conversão de {len(csv_files)} arquivos para Parquet...\n")

    for csv_file in csv_files:
        nome_tabela = csv_file.stem
        destino_parquet = PARQUET_DIR / f"{nome_tabela}.parquet"

        tamanho_original_mb = csv_file.stat().st_size / (1024 * 1024)
        print(f"[*] Processando: {csv_file.name} ({tamanho_original_mb:.2f} MB)...", end=" ", flush=True)

        try:
            # Lê com delimitador ';', separador decimal ',' e suporte a UTF-8/acentos
            df = pd.read_csv(
                csv_file,
                sep=";",
                decimal=",",
                encoding="utf-8-sig",
                low_memory=False,
            )

            # Salva em Parquet com compressão snappy (padrão)
            df.to_parquet(destino_parquet, index=False, engine="pyarrow")

            tamanho_parquet_mb = destino_parquet.stat().st_size / (1024 * 1024)
            reducao = ((tamanho_original_mb - tamanho_parquet_mb) / tamanho_original_mb) * 100 if tamanho_original_mb > 0 else 0
            print(f"[OK] -> {destino_parquet.name} ({tamanho_parquet_mb:.2f} MB | -{reducao:.1f}%)")

        except Exception as e:
            print(f"[ERRO] Falha ao converter: {e}")

    print(f"\nConversão finalizada com sucesso! Arquivos salvos em: {PARQUET_DIR}")


if __name__ == "__main__":
    converter_csv_para_parquet()
