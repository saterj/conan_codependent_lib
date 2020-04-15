# use this as a profile

Create this as `ECU_sdk/2.7.2.220@SDKS/test` with `conan create . SDKs/test`


then update a profile with this stuff:

```
[settings]
os=Linux
os_target=Linux
os_build=Linux
arch=x86
arch_target=armv7
arch_build=armv7

[options]
[build_requires]
*: ecu_sdk/2.7.2.220@SDKS/test
[env]
```
