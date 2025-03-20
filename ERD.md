# Entity Relationship Diagram

## Entities

1. **App**
2. **Keylogger**
3. **CameraCapture**
4. **KeyloggerCameraApp**
5. **SecureKeylogger**
6. **SecureCameraCapture**
7. **SecureKeyloggerCameraApp**
8. **Index** (HTML template)

## Relationships

1. **App** is the main application that uses `Keylogger`, `CameraCapture`, and `KeyloggerCameraApp`.
2. **SecureKeylogger**, **SecureCameraCapture**, and **SecureKeyloggerCameraApp** are secure versions of their respective entities.
3. **Index** is an HTML template used by the `App`.

## ERD

```plaintext
+---------------------+
|       App           |
+---------------------+
| - keylogger         |
| - cameraCapture     |
| - keyloggerCameraApp|
+---------------------+
          |
          | uses
          v
+---------------------+       +---------------------+
|     Keylogger       |<----->|  KeyloggerCameraApp |
+---------------------+       +---------------------+
          |
          | uses
          v
+---------------------+
|  CameraCapture      |
+---------------------+

+---------------------+       +---------------------+
|  SecureKeylogger    |<----->|SecureKeyloggerCameraApp|
+---------------------+       +---------------------+
          |
          | uses
          v
+---------------------+
|SecureCameraCapture  |
+---------------------+

+---------------------+
|       Index         |
+---------------------+
          |
          | used by
          v
+---------------------+
|       App           |
+---------------------+

this is the basic er diagram
