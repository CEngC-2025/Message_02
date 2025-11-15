import subprocess

zip_name = "protected.zip"
hash_name = "protected_hash.txt"

subprocess.run(["zip2john '" + zip_name + "' > '" + hash_name + "'"])

with open(hash_name, "r") as f:
    hash_contents = f.read()

hash_start = s.find("$pkzip2$")
hash_end = s.find("$pkzip2$", hash_start + 8)
hash_contents = hash_contents[hash_start : hash_end + 8]

# Step 2: Overwrite the file with the string
with open("myfile.txt", "w") as f:
    f.write(hash_contents)

subprocess.run(["hashcat -m 17200 -a 3" + hash_name + "-1 0123456789 ?1?1?1?1-?1?1-?1?1 --increment -w 3 -S --potfile-disable"])
