param(
  [string]$Proyecto = (Get-Location).Path,
  [string]$Salida = (Join-Path (Get-Location).Path "documentacion.docx")
)

$repo = $PSScriptRoot
$env:PYTHONPATH = $repo
python -m app.main $Proyecto -o $Salida
