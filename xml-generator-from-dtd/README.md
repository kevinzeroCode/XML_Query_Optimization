# XML generator from DTD + wikipedia parser
This project includes a DTD parser and an XML generator which can use the parsed DTD to generate valid XML templates. In addition said XML templates can be automatically filled with content from Wikipedia using the Wikipedia API.

## Required packages to use
 - `pip3`
 - `virtualenv` (can be installed through `pip3` or your default package manager)

## Setup
1. Set up virtual env `virtualenv -p python3 venv`
2. Activate virtual env `source venv/bin/activate`
3. Install the required packages `pip install -r requirements.txt`
4. Run the server `./run.sh`
5. Open your browser and go to http://127.0.0.1:5000/

## Examples
### Generate DTD and parse info from wikipedia
The DTD for wikipedia artciles is quite simple. For this example we'll use the following DTD:
```xml
<!ELEMENT article (text, text, title, text)>
<!ELEMENT text (#PCDATA)>
<!ELEMENT title (#PCDATA)>
```
1. Choose the file `data/sample-dtd/astronomicheski-obekt.dtd`
2. Enter wikipedia article title 'Астрономически обект'
3. Choose the option 'Вземи заглавията на секциите и текста'
4. Click the Generate button
The output should be:
```xml
<article>
	<text>
		Астрономически обект...
	</text>
	<text>
		Примери за астрономически...
	</text>
	<title>
		Галактики редактиране | редактиране на кода
	</title>
	<text>
		Вселената може да се...
	</text>
</article>
```
### Generate DTD only
Let's use a more complex DTD:
```xml
<!ELEMENT games (game)*>
<!ELEMENT game (home-team, ex-team, scores, yellows, reds)>
<!ELEMENT home-team (#PCDATA)>
<!ELEMENT ex-team (#PCDATA)>
<!ELEMENT scores (score)*>
<!ELEMENT yellows (player)*>
<!ELEMENT reds (player)*>
<!ELEMENT score (player)*>
<!ELEMENT player (#PCDATA)>
<!ATTLIST game score CDATA #REQUIRED>
<!ATTLIST score time CDATA #REQUIRED>
<!ATTLIST score type (field|penalty) #IMPLIED>
```

1. Choose the file `data/dtd/9elements_3attributes.dtd`
2. Leave the Wikipedia article field empty
3. Choose the option 'Не използвай Wikipedia'
4. Click the Generate button
The output should be:
```xml
<games>
	<game score="">
		<home-team />
		<ex-team />
		<scores>
			<score time="" type="">
				<player />
			</score>
		</scores>
		<yellows>
			<player />
		</yellows>
		<reds>
			<player />
		</reds>
	</game>
</games>
```
