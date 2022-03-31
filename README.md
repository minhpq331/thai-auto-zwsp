# Thai Auto Zero-width Space

Auto insert Zero-width space to Thai sentences based on PyICU package. This will help you display line-break correctly.

Credits to [pigeon-media/khmer-auto-zwsp](https://github.com/pigeon-media/khmer-auto-zwsp)

### Run as an API

```bash
docker-compose up -d
```

The server will be running on `http://localhost:5000`

#### Request

```json
{ "data": "แอปของคุณยังไม่ได้อัปเดต" }
```


#### Response

```json
{
  "data": "แอป<>ของ<>คุณ<>ยัง<>ไม่<>ได้<>อัปเดต"
}
```

> `<>` is used to indicate the ZWSP

### Run as CMD

```bash
docker build -t thai-auto-zwsp .

# Mount current directory with file1.txt, file2.txt to container and process it

docker run -it --rm \ 
  -u "$(id -u $USER):$(id -g $USER)" \
  -v "$PWD:/app/data" thai-auto-zwsp \
  python3 process.py file1.txt file2.txt
```

