# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kiertotie/blob/default/sbom.json) with SHA256 checksum ([227e2baa ...](https://git.sr.ht/~sthagen/kiertotie/blob/default/sbom.json.sha256 "sha256:227e2baab7ebdd9dc65db8211dfab16d50c178d57598371b75d4a6d4f84d021b")).
<!--[[[end]]] (checksum: acca2b0de9bf858ddbffbe19bb623cac)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                          | License     | Author            | Description (from packaging data)                                  |
|:-------------------------------------------|:-------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------|
| [Babel](https://babel.pocoo.org/)          | [2.11.0](https://pypi.org/project/Babel/2.11.0/) | BSD License | Armin Ronacher    | Internationalization utilities                                     |
| [PyYAML](https://pyyaml.org/)              | [6.0](https://pypi.org/project/PyYAML/6.0/)      | MIT License | Kirill Simonov    | YAML parser and emitter for Python                                 |
| [typer](https://github.com/tiangolo/typer) | [0.7.0](https://pypi.org/project/typer/0.7.0/)   | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 1f60d5b0becbcaf49e7e2550fc1dbe45)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                         | License     | Author         | Description (from packaging data)                 |
|:----------------------------------------------|:------------------------------------------------|:------------|:---------------|:--------------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/)  | BSD License | Armin Ronacher | Composable command line interface toolkit         |
| [pytz](http://pythonhosted.org/pytz)          | [2022.7](https://pypi.org/project/pytz/2022.7/) | MIT License | Stuart Bishop  | World timezone definitions, modern and historical |
<!--[[[end]]] (checksum: 2c34b77f1e6b53373df0b3208fb6d51b)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Babel==2.11.0
  - pytz [required: >=2015.7, installed: 2022.7]
PyYAML==6.0
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 4c0199d74efc4bd15de1857b44428067)-->
