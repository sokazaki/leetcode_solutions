awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt # ERE(Extended Regular Expression)
grep '^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$' file.txt # BRE(Basic Regular Expression)
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt # ERE(Extended Regular Expression)
