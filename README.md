<h1 align="center"> Python Value-Objects</h1>

<div align="center">

![](https://img.shields.io/badge/PRs-welcome-green.svg)
[![GitHub](https://img.shields.io/github/license/jparadadev/python-value-objects)](https://github.com/jparadadev/python-value-objects/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/pyvalueobjects)](https://pypi.org/project/pyvalueobjects/)
[![Downloads](https://pepy.tech/badge/pyvalueobjects)](https://pepy.tech/project/pyvalueobjects)
[![GA](https://github.com/jparadadev/python-value-objects/workflows/Tests/badge.svg)](https://github.com/jparadadev/python-value-objects/actions/workflows/test.yml)
 
</div>

![](https://raw.githubusercontent.com/jparadadev/python-value-objects/assets/assets/logo.png)

A collection of Value Objects to save time by generalizing types and format validations.

* [Value-objects](#value-objects)
  * [Numeric value-objects](#numeric-value-objects)
    * [Int](#int)
    * [Nullable Int](#nullable-int)
    * [Positive Int](#positive-int)
    * [Nullable Positive Int](#positive-int)
    * [Positive or zero Int](#positive-or-zero-int)
    * [Nullable Positive or zero Int](#nullable-positive-or-zero-int)
    * [Negative Int](#negative-int)
    * [Nullable Negative Int](#nullable-negative-int)
    * [Negative or zero Int](#negative-or-zero-int)
    * [Nullable Negative or zero Int](#nullable-negative-or-zero-int)
  * [String value-objects](#string-value-objects)
    * [String](#string)
    * [Nullable String](#nullable-string)
    * [Uuid4](#uuid4)
    * [Nullable Uuid4](#nullable-uuid4)
  * [Date value-objects](#date-value-objects)
    * [ISO Date](#iso-date)
  * [Data Structures value-objects](#data-structures-value-objects)
    * [ArrayList](#arraylist)
    * [NullableArrayList](#nullable-arraylist)
  * [Security value-objects](#security-value-objects)
    * [CVE](#cve)
    * [Nullable CVE](#nullable-cve)
    * [CPE](#cpe)
    * [Nullable CPE](#nullable-cpe)

# Value-objects

## Numeric value-objects

### Int

Integer numbers without a fractional component that don't support decimal points.

```python
from pyvalueobjects import Int

# Creation
my_integer = Int(9)

# Getting raw value
my_integer.value() # returns -> 9
```

### Nullable Int

Integer numbers and None.

```python
from pyvalueobjects import NullableInt

# Creation
my_integer = NullableInt(9)

# Creating from None
my_nullable_integer = NullableInt(None)

# Getting raw value
my_integer.value() # returns -> 9
my_nullable_integer.value() # returns -> None
```

### Positive Int

```python
from pyvalueobjects import PositiveInt

# Creation
my_integer = PositiveInt(9)

# Getting raw value
my_integer.value() # returns -> 9
```

### Nullable Positive Int

```python
from pyvalueobjects import NullablePositiveInt

# Creation
my_integer = NullablePositiveInt(9)

# Creating from None
my_nullable_integer = NullablePositiveInt(None)

# Getting raw value
my_integer.value() # returns -> 9
my_nullable_integer.value() # returns -> None
```

### Positive Or Zero Int

```python
from pyvalueobjects import PositiveOrZeroInt

# Creation
my_integer = PositiveOrZeroInt(9)

# Getting raw value
my_integer.value() # returns -> 9
```

### Nullable Positive Or Zero Int

```python
from pyvalueobjects import NullablePositiveOrZeroInt

# Creation
my_integer = NullablePositiveOrZeroInt(9)

# Creating from None
my_nullable_integer = NullablePositiveOrZeroInt(None)

# Getting raw value
my_integer.value() # returns -> 9
my_nullable_integer.value() # returns -> None
```

### Negative Int

```python
from pyvalueobjects import NegativeInt

# Creation
my_integer = NegativeInt(-9)

# Getting raw value
my_integer.value() # returns -> -9
```

### Nullable Negative Int

```python
from pyvalueobjects import NullableNegativeInt

# Creation
my_integer = NullableNegativeInt(-9)

# Creating from None
my_nullable_integer = NullableNegativeInt(None)

# Getting raw value
my_integer.value() # returns -> -9
my_nullable_integer.value() # returns -> None
```

### Negative Or Zero Int

```python
from pyvalueobjects import NegativeOrZeroInt

# Creation
my_integer = NegativeOrZeroInt(-9)

# Getting raw value
my_integer.value() # returns -> -9
```

### Nullable Negative Or Zero Int

```python
from pyvalueobjects import NullableNegativeOrZeroInt

# Creation
my_integer = NullableNegativeOrZeroInt(-9)

# Creating from None
my_nullable_integer = NullableNegativeOrZeroInt(None)

# Getting raw value
my_integer.value() # returns -> -9
my_nullable_integer.value() # returns -> None
```

## String value-objects

### String

```python
from pyvalueobjects import String

# Creation
my_str = String('potato')

# Getting raw value
my_str.value() # returns -> 'potato'
```

### Nullable String

```python
from pyvalueobjects import NullableString

# Creation
my_str = NullableString('potato')

# Getting raw value
my_str.value() # returns -> 'potato'

# Creation
my_nullable_str = NullableString(None)

# Getting raw value
my_nullable_str.value() # returns -> None
```

### Non Empty String

```python
from pyvalueobjects import NonEmptyString

# Creation
my_str = NonEmptyString('potato')

# Getting raw value
my_str.value() # returns -> 'potato'

# Creation
my_str2 = NonEmptyString('') # raises error
```

### Nullable non Empty String

```python
from pyvalueobjects import NullableNonEmptyString

# Creation
my_str = NullableNonEmptyString('potato')

# Getting raw value
my_str.value() # returns -> 'potato'

# Creation
my_str2 = NullableNonEmptyString(None)

# Getting raw value
my_str2.value() # returns -> None

# Creation
my_str3 = NullableNonEmptyString('') # raises error
```

### Uuid4

```python
from pyvalueobjects import Uuid4

# Creation
my_uuid4 = Uuid4('6c7add12-bf35-459e-a6c5-3178a2a33011')

# Getting raw value
my_uuid4.value()  # returns -> '6c7add12-bf35-459e-a6c5-3178a2a33011'
```

### Nullable Uuid4

```python
from pyvalueobjects import NullableUuid4

# Creation
my_uuid4 = NullableUuid4('6c7add12-bf35-459e-a6c5-3178a2a33011')
my_null_uuid4 = NullableUuid4(None)

# Getting raw value
my_uuid4.value()  # returns -> '6c7add12-bf35-459e-a6c5-3178a2a33011'
my_null_uuid4.value()  # returns -> 'None'
```

## Date value-objects

### ISO Date

```python
from pyvalueobjects import IsoDate

# Creation
my_date = IsoDate('2023-08-15T04:55:12.076Z')

# Getting raw value
my_date.value()  # returns -> '2023-08-15T04:55:12.076Z'
```

## Data structures value-objects

### ArrayList

```python
from pyvalueobjects import ArrayList
from pyvalueobjects import Int

# Creation
my_int_array = ArrayList(Int)([39])

# Getting raw value
my_int_array.value()  # returns -> [39]
```

### Nullable ArrayList

```python
from pyvalueobjects import ArrayList
from pyvalueobjects import Int

# Creation
my_int_array = ArrayList(Int)([39])
my_null_array = ArrayList(Int)(None)

# Getting raw value
my_int_array.value()  # returns -> [39]
my_null_array.value()  # returns -> None
```

## Security value-objects

### CVE

```python
from pyvalueobjects import Cve

# Creation
my_cve = Cve('CVE-2014-9418')

# Getting raw value
my_cve.value()  # returns -> 'CVE-2014-9418'
```

### Nullable CVE

```python
from pyvalueobjects import NullableCve

# Creation
my_cve = NullableCve('CVE-2014-9418')
my_null_cve = NullableCve(None)

# Getting raw value
my_cve.value()  # returns -> 'CVE-2014-9418'
my_null_cve.value()  # returns -> None
```

### CPE

```python
from pyvalueobjects import Cpe

# Creation
my_cpe = Cpe('cpe:/a:openjdk:openjdk:8u282')

# Getting raw value
my_cpe.value()  # returns -> 'cpe:/a:openjdk:openjdk:8u282'
```

### Nullable CPE

```python
from pyvalueobjects import NullableCpe

# Creation
my_cpe = NullableCpe('cpe:/a:openjdk:openjdk:8u282')
my_null_cpe = NullableCpe(None)

# Getting raw value
my_cpe.value()  # returns -> 'cpe:/a:openjdk:openjdk:8u282'
my_null_cpe.value()  # returns -> None
```
