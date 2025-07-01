## Common commands to run this application
1. Install below required dependencies

| dependencies |
|----------|
| uvicorn   |
| fastapi   |

*Installation process*
```python
pip3 install uvicorn fastapi
```

2. Hit the below url to run this application
[Link text](https://localhost:8000/docs)

3. Endpoints exposed by application

```
/docs
/health
/notes
```

4. Example of hitting endpoints

```bash
curl -X GET http://localhost:8000/health

```bash
curl -X POST http://localhost:8000/notes -H "Content-Type: application/json" -d '{"content":"First note"}'
```
