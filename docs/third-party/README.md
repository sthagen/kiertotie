# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kiertotie/blob/default/sbom/cdx.json) with SHA256 checksum ([f4e2e628 ...](https://git.sr.ht/~sthagen/kiertotie/blob/default/sbom/cdx.json.sha256 "sha256:f4e2e628d1917251dfc87ea7c3101cafdb0804977694d1b01ebe402f97ea18a2")).
<!--[[[end]]] (checksum: 2bc9086529d19c3d537033907ea5cd1d)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                          | License     | Author            | Description (from packaging data)                                  |
|:-------------------------------------------|:-------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------|
| [Babel](https://babel.pocoo.org/)          | [2.12.1](https://pypi.org/project/Babel/2.12.1/) | BSD License | Armin Ronacher    | Internationalization utilities                                     |
| [PyYAML](https://pyyaml.org/)              | [6.0](https://pypi.org/project/PyYAML/6.0/)      | MIT License | Kirill Simonov    | YAML parser and emitter for Python                                 |
| [typer](https://github.com/tiangolo/typer) | [0.7.0](https://pypi.org/project/typer/0.7.0/)   | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 0e6ea983ea6fed49a5a31ced9c588297)-->

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
Babel==2.12.1
PyYAML==6.0
typer==0.7.0
└── click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 9c70555c6b4347f6e214a27a6961b068)-->
