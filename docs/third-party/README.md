# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/kiertotie/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([2780df90 ...](https://git.sr.ht/~sthagen/kiertotie/blob/default/etc/sbom/cdx.json.sha256 "sha256:2780df90058c96a018f76835fc64b23baf13d9ac234169d371b6c8e1aa5d2db1")).
<!--[[[end]]] (checksum: 48df3eea00a3bb07d20854030382f5c8)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                       | Version                                          | License     | Author            | Description (from packaging data)                                  |
|:-------------------------------------------|:-------------------------------------------------|:------------|:------------------|:-------------------------------------------------------------------|
| [Babel](https://babel.pocoo.org/)          | [2.14.0](https://pypi.org/project/Babel/2.14.0/) | BSD License | Armin Ronacher    | Internationalization utilities                                     |
| [PyYAML](https://pyyaml.org/)              | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)  | MIT License | Kirill Simonov    | YAML parser and emitter for Python                                 |
| [typer](https://github.com/tiangolo/typer) | [0.9.0](https://pypi.org/project/typer/0.9.0/)   | MIT License | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 46abda80381c986b2d4dfff79b2a8fec)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                      |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.5](https://pypi.org/project/click/8.1.5/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit              |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+ |
<!--[[[end]]] (checksum: cae3fba0485bf4de8a735f0ded0dcf53)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
Babel==2.14.0
PyYAML==6.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 669e9a9e8cba508e1836d9d043d7784f)-->
