# wiki to philosophy

[![tweet](twitter.png)](https://twitter.com/davelevitan/status/935619980594466816)

Also described [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy).

So. Here it is. In Python. With Beautiful soup. Obviously.

Also: I disproved the hypothesis: there are many loops (`/wiki/Accounting`), (`/wiki/Cardinal_direction`)

## Result

![dot](graph_dot.png)
![neato](graph_neato.png)

## Best of

### Unbalanced parentheses:

![parentheses](parentheses.png)

### Random links leading to pornographic images:

![pinterest](pinterest.png)

## Considerations

I took the [_Top-100 list_](https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#Top-100_list) and took all the articles that are not meta.

Those infoboxes, "this article needs work" boxes, images, table of contents (sometimes) are before the rest of the article in the html code. They all had to be sorted out.

Citations like [5] or [edit] links are also links. Don't want those.

I cannot categorically delete all parentheses from the code. It will damage links like `/wiki/set_(mathematics)`.

I decided to go past philosophy and see what is next. If I stop when reaching philosophy there are two big trees. The other one ends in knowledge. Going past philosophy finally merges those.

## Todo

Remove redundant code from 3 separate files.

Ignore external links.

## Acknowledgement

Thanks [@davelevitan](https://twitter.com/davelevitan) for bringing me this excelent challenge! It took about 2 hours.

## Sample output

### Simple (`wiki.py` with `debug = False`)

	-                              found: 18 steps
	Wiki                           found: 22 steps
	Facebook                       loop! (/wiki/Accounting)
	YouTube                        found: 10 steps
	404.php                        found: 20 steps
	United States                  found: 10 steps
	Google                         loop! (/wiki/Knowledge)
	Donald Trump                   found: 12 steps
	Wikipedia                      found: 22 steps
	Barack Obama                   found: 12 steps
	India                          loop! (/wiki/Cardinal_direction)
	World War II                   found: 9 steps
	Michael Jackson                found: 19 steps
	Malware                        found: 21 steps
	Sex                            loop! (/wiki/Knowledge)
	United Kingdom                 found: 9 steps
	Lady Gaga                      loop! (/wiki/Knowledge)
	Eminem                         found: 10 steps
	The Beatles                    found: 10 steps
	Adolf Hitler                   found: 10 steps
	Justin Bieber                  found: 11 steps
	World War I                    found: 9 steps
	The Big Bang Theory            loop! (/wiki/Knowledge)
	Steve Jobs                     found: 8 steps
	Canada                         loop! (/wiki/Knowledge)
	Game of Thrones                loop! (/wiki/Knowledge)
	How I Met Your Mother          loop! (/wiki/Knowledge)
	Academy Awards                 loop! (/wiki/Knowledge)
	Lil Wayne                      found: 17 steps
	Kim Kardashian                 found: 19 steps
	Australia                      loop! (/wiki/Knowledge)
	Cristiano Ronaldo              found: 11 steps
	XHamster                       loop! (/wiki/Knowledge)
	Miley Cyrus                    loop! (/wiki/Knowledge)
	Elizabeth II                   broken link! (https://en.wiktionary.org/wiki/Special:Search/potent)
	List of Presidents of the United States found: 11 steps
	Harry Potter                   found: 19 steps
	Rihanna                        broken link! (https://en.wiktionary.org/wiki/polynym)
	Japan                          found: 9 steps
	Selena Gomez                   loop! (/wiki/Knowledge)
	Glee (TV series)               found: 24 steps
	Germany                        found: 9 steps
	The Walking Dead (TV series)   loop! (/wiki/Knowledge)
	Abraham Lincoln                found: 12 steps
	Taylor Swift                   found: 16 steps
	Star Wars                      loop! (/wiki/Knowledge)
	Indigenous australian          found: 10 steps
	China                          found: 8 steps
	Lionel Messi                   found: 12 steps
	Breaking Bad                   loop! (/wiki/Knowledge)
	Johnny Depp                    found: 8 steps
	New York City                  loop! (/wiki/Knowledge)
	Tupac Shakur                   found: 15 steps
	Web scraping                   found: 20 steps
	France                         found: 8 steps
	Kanye West                     loop! (/wiki/Knowledge)
	Russia                         found: 16 steps
	Stephen Hawking                loop! (/wiki/Knowledge)
	Albert Einstein                loop! (/wiki/Knowledge)
	Earth                          loop! (/wiki/Knowledge)
	Angelina Jolie                 loop! (/wiki/Knowledge)
	Mark Zuckerberg                loop! (/wiki/Accounting)
	Internet Movie Database        found: 20 steps
	Leonardo DiCaprio              loop! (/wiki/Knowledge)
	Nicki Minaj                    found: 13 steps
	William Shakespeare            found: 12 steps
	Michael Jordan                 found: 11 steps
	Dwayne Johnson                 found: 14 steps
	Katy Perry                     found: 8 steps
	Illuminati                     found: 9 steps
	Doctor Who                     found: 13 steps
	Mila Kunis                     found: 9 steps
	Vietnam War                    loop! (/wiki/Knowledge)
	John F. Kennedy                found: 12 steps
	Adele                          loop! (/wiki/Knowledge)
	Sexual intercourse             loop! (/wiki/Knowledge)
	Human penis size               loop! (/wiki/Knowledge)
	One Direction                  found: 8 steps
	Favicon.ico                    found: 15 steps
	Global warming                 loop! (/wiki/Knowledge)
	London                         found: 15 steps
	John Cena                      loop! (/wiki/Knowledge)
	Muhammad Ali                   found: 15 steps
	List of The Big Bang Theory episodes loop! (/wiki/Knowledge)
	Vagina                         found: 17 steps
	Jay-Z                          found: 14 steps
	Bill Gates                     broken link! (https://en.wiktionary.org/wiki/Special:Search/potent)
	Arnold Schwarzenegger          found: 14 steps
	Will Smith                     found: 11 steps
	September 11 attacks           found: 10 steps
	Halloween                      loop! (/wiki/Halloween)
	Prince (musician)              loop! (/wiki/Knowledge)
	David Bowie                    found: 9 steps
	England                        found: 11 steps
	Singapore                      found: 14 steps
	Pornography                    loop! (/wiki/Knowledge)
	Israel                         loop! (/wiki/Knowledge)
	Bruce Lee                      found: 12 steps
	Java                           loop! (/wiki/Knowledge)
	Marilyn Monroe                 loop! (/wiki/Knowledge)
	Britney Spears                 found: 14 steps
	Grey's Anatomy                 loop! (/wiki/Management)
	Tom Cruise                     loop! (/wiki/Knowledge)
	Brazil                         loop! (/wiki/Knowledge)
	LeBron James                   found: 11 steps
	RMS Titanic                    loop! (/wiki/Knowledge)
	Amazon.com                     found: 15 steps
	Naruto                         found: 11 steps
	Masturbation                   loop! (/wiki/Knowledge)
	AMGTV                          found: 18 steps
	English language               found: 13 steps
	Lost (TV series)               loop! (/wiki/Knowledge)
	American Civil War             found: 11 steps
	Henry VIII of England          found: 11 steps
	Scarlett Johansson             found: 9 steps
