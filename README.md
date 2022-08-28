
## Installation

```bash
git clone https://github.com/MasterChad/searchdb.git
```

## Utilisation

```bash
python main.py
```

Ou

```bash
python3 main.py
```

## Important !

Il se peut que vous recevez des retours comme : FINDSTR : la ligne X est trop longue ---  C'est tout simplement normal. Vous aurez tout les résultats dans le fichier indiqué !

 
## Très Important !

Changez le dossier de vos bases de données dans le script, remplacez " D:\db1\ " , et collez bien le *.* au dernier \ de votre dossier.

## Format parfait pour le os.system
```python
os.system("powershell.exe findstr /I "+chose+" D:\db1\*.* > "+result_str+".txt")
```

