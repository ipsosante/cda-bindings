# CDA bindings

Python bindings for the [CDA R2](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=515) document format.

The bindings are generated using [tefra/xsdata](https://github.com/tefra/xsdata), based on the [ANS](https://esante.gouv.fr/) [variant of the CDA spec](https://github.com/ansforge/TestContenuCDA/tree/main/infrastructure/cda).

## Using the bindings

Add the following to your requirements.txt file :

```
git+https://github.com/ipsosante/cda-bindings.git
```

## Re-generating the bindings

Start by creating a Python virtualenv, and install the dependencies:


```
pip install .[cli]
```

Then you'll need to clone [https://github.com/ansforge/TestContenuCDA-3-0](https://github.com/ansforge/TestContenuCDA-3-0) somewhere.

```sh
git clone https://github.com/ansforge/TestContenuCDA-3-0.git
```

Come back to the `cda-bindings` directory, then run :

```sh
./regen.sh /path/to/ansforge/TestContenuCDA-3-0
```

This will regenerate the full bindings in `./cdabindings`.

## Validating the generated XML files with the XSD

```sh
git clone https://github.com/amouat/xsd-validator
cd xsd-validator
./xsdv.sh /path/to/ansforge/TestContenuCDA-3-0/infrastructure/cda/CDA_extended.xsd /path/to/generated/vsm_doc.xml
```

## Patches

### `patches/xsd/remove_cd_qualifier.patch`

Removes the `qualifier` property from de `CD` element (instead of declaring it with `maxOccurs="0"`). It is not supported by the spec :

> Les éléments de type "CV", "CE" ou "CD" doivent respecter les contraintes suivantes :
> [...]
> l'élément qualifier n'est pas utilisé car non supporté par la version ultérieure des types de données HL7 V3;

### `patches/xsd/remove_cd_qualifier.patch`

Make the `maxOccurs` property of the `translation` attributes of the `CE` element `unbounded` intead of `0`.

I've seen no reason if the spec to limit the usage of `translation` at the `CE` level. It also makes the generated `CV` class unusable because xsdata will generate a dataclass with a `translation` field with `init=False`.

### `patches/generated_code/cs_init.patch`

This is related to the patch `patches/xsd/remove_cd_qualifier.patch`. To make the generated `CS` class initializable, we need to manually declare its initializer to work around most of its field being re-declared with `init=False`.