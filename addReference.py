import os

cwd = os.path.basename(os.getcwd())    
vendorNameDatasetName = cwd.replace('Lean.DataSource.','')
reference=f'QuantConnect.DataSource.{vendorNameDatasetName}'
csproj = '../Lean/Algorithm.CSharp/QuantConnect.Algorithm.CSharp.csproj'

with open(csproj, mode='r') as fp:
    content = fp.read()
    if reference in content:
        exit(f"Lean\Algorithm.CSharp contains reference to {reference}")

content = content.replace('</Project>',
    f'''  <ItemGroup>
    <Reference Include="{reference}">
      <HintPath>..\..\{cwd}\\bin\Debug\\net6.0\{reference}.dll</HintPath>
    </Reference>
  </ItemGroup>
</Project>''')

with open(csproj, mode='w') as fp:
    fp.write(content)
    exit(f"Refernce to {reference} was added to Lean\Algorithm.CSharp")