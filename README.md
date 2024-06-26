# CDA bindings

Python bindings for the [CDA R2](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=515) document format.

The bindings are generated using [tefra/xsdata](https://github.com/tefra/xsdata), based on the [ANS](https://esante.gouv.fr/) [variant of the CDA spec](https://github.com/ansforge/TestContenuCDA/tree/main/infrastructure/cda).

## Using the bindings

Add the following to your requirements.txt file :

```
git+https://github.com/ipsosante/cda-bindings.git
```

And then

```
pip install -r requirements.txt
```

## Re-generating the bindings

Start by creating a Python virtualenv, and install the dependencies using the root `requirements.txt`.

Then you'll need to clone [https://github.com/ansforge/TestContenuCDA-3-0](https://github.com/ansforge/TestContenuCDA-3-0) somewhere.

```sh
git clone https://github.com/ansforge/TestContenuCDA-3-0.git
```

And patch it with all `.patch` files found at the top level of this repository :

```sh
cd /path/to/ansforge/TestContenuCDA
patch -p1 < /path/to/cda-bindings/remove_cd_qualifier.patch
patch -p1 < /path/to/cda-bindings/unbounded_ce_translation.patch
```

(See the "Patches" section for more info).

Come back to the `cda-bindings` directory, then run :

```sh
rm -rf ./cdabindings; xsdata generate --debug --config .xsdata.xml /path/to/ansforge/TestContenuCDA-3-0/infrastructure/cda/CDA_extended.xsd
```

## Validating the generated XML files with the XSD

```sh
git clone https://github.com/amouat/xsd-validator
cd xsd-validator
./xsdv.sh /path/to/ansforge/TestContenuCDA/infrastructure/cda/CDA_extended.xsd /path/to/generated/vsm_doc.xml
```

## Patches

### `remove_cd_qualifier.patch`

Removes the `qualifier` property from de `CD` element (instead of declaring it with `maxOccurs="0"`). It is not supported by the spec :

> Les éléments de type "CV", "CE" ou "CD" doivent respecter les contraintes suivantes :
> [...]
> l'élément qualifier n'est pas utilisé car non supporté par la version ultérieure des types de données HL7 V3;

### `unbounded_ce_translation.patch`

Make the `maxOccurs` property of the `translation` attributes of the `CE` element `unbounded` intead of `0`.

I've seen no reason if the spec to limit the usage of `translation` at the `CE` level. It also makes the generated `CE` class unusable because xsdata will generate a dataclass with a `translation` field with `init=False`. Because this field is also inherited, this makes the child class impossible to init.

Simple example to demonstrate the issue:

```py
from dataclasses import dataclass, field

@dataclass
class A:
    translation: str

@dataclass
class B(A):
    translation: str = field(init=False)

>>> A(translation="hello, world") # OK
>>> B()
AttributeError: 'B' object has no attribute 'translation'
```