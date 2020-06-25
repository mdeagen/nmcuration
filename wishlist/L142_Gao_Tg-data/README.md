## L142_Gao_2014

Probable curation error. Reported Tg/control Tg are far above expected range.

According to [this datasheet](https://espanol.kynar.com/export/sites/kynar-latam/.content/medias/downloads/literature/kynar-kynar-flex-pvdf-performance.pdf), expected Tg range for PVDF is -41 to -37 C, and the **melting temperature** is in the range 155 to 170 C.

Inspect the original source DOI to confirm that these values were curated properly.


### SPARQL query to find DOI

```
PREFIX nm: <http://nanomine.org/ns/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT * WHERE {
  ?doi sio:hasPart ?sample .
  ?sample a nm:PolymerNanocomposite .
  
  FILTER(REGEX(STR(?sample),"l142-s2-gao-2014"))
}
```

The paper's DOI is [10.1021/jp409474k](http://dx.doi.org/10.1021/jp409474k).

