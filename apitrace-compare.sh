# $1 old trace
# $2 new trace
# $3 old frame
# $4 new frame

oldjson=$1_$3.json
newjson=$2_$4.json
echo $oldjson
echo $newjson

echo "replay old at frame "$3
apitrace replay -D $3 $1 > $oldjson 2> /dev/null

echo "replay new at frame "$4
apitrace replay -D $4 $2 > $newjson 2> /dev/null

apitrace diff-state $oldjson $newjson

rm $oldjson
rm $newjson
