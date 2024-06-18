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
