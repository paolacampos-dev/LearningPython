# How to debug:

1. ```python
   import pdb; pdb.set_trace()
   ```
2. ```python
   breakpoint()
   ```

   - it can be modify its behaviour by modifying the enviroment variables

3. post mortem debugging will drop us automatically when an exception is hit:
   - in the terminal: python3 -m pdb <filename.py>
