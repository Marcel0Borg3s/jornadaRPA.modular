$exclude = @("venv", "entradaDados_randomico.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "entradaDados_randomico.zip" -Force