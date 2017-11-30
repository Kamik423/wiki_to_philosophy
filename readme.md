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

## Command line Options

	usage: wiki.py [-h] [-g] [-l] [-n] [-r ROOT] [-s] [-t] [-v]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -g, --graph           creates graphs
	  -l, --load            use graph.adjlist as source not web
	  -n, --no-nx           do not use networkx (disables -g -l -s)
	  -r ROOT, --root ROOT  search just specified page[s], separated by ","
	  -s, --save            saves adjacency list
	  -t, --time            displays the time per online step
	  -v, --verbose         print entire path

## Acknowledgement

Thanks [@davelevitan](https://twitter.com/davelevitan) for bringing me this excelent challenge! It took about 2 hours.

## Sample output

### Simple (`./wiki.py -gs`)


	-                                                 Hit loop after 23 steps 
	Wiki                                              Hit tree after 09 steps - 18 further steps to loop; 27 in total
	Facebook                                          Hit loop after 06 steps 
	YouTube                                           Hit tree after 10 steps - 05 further steps to loop; 15 in total
	404.php                                           Hit tree after 07 steps - 18 further steps to loop; 25 in total
	United States                                     Hit tree after 07 steps - 08 further steps to loop; 15 in total
	Google                                            Hit tree after 09 steps - 02 further steps to loop; 11 in total
	Donald Trump                                      Hit tree after 06 steps - 11 further steps to loop; 17 in total
	Wikipedia                                         Hit tree after 13 steps - 14 further steps to loop; 27 in total
	Barack Obama                                      Hit tree after 01 steps - 16 further steps to loop; 17 in total
	India                                             Hit loop after 05 steps 
	World War II                                      Hit tree after 03 steps - 11 further steps to loop; 14 in total
	Michael Jackson                                   Hit tree after 12 steps - 12 further steps to loop; 24 in total
	Malware                                           Hit tree after 05 steps - 21 further steps to loop; 26 in total
	Sex                                               Hit tree after 05 steps - 02 further steps to loop; 07 in total
	United Kingdom                                    Hit tree after 01 steps - 13 further steps to loop; 14 in total
	Lady Gaga                                         Hit tree after 09 steps - 03 further steps to loop; 12 in total
	Eminem                                            Hit tree after 08 steps - 07 further steps to loop; 15 in total
	The Beatles                                       Hit tree after 02 steps - 13 further steps to loop; 15 in total
	Adolf Hitler                                      Hit tree after 07 steps - 08 further steps to loop; 15 in total
	Justin Bieber                                     Hit tree after 01 steps - 15 further steps to loop; 16 in total
	World War I                                       Hit tree after 01 steps - 13 further steps to loop; 14 in total
	The Big Bang Theory                               Hit tree after 06 steps - 04 further steps to loop; 10 in total
	Steve Jobs                                        Hit tree after 02 steps - 11 further steps to loop; 13 in total
	Canada                                            Hit tree after 09 steps - 04 further steps to loop; 13 in total
	Game of Thrones                                   Hit tree after 02 steps - 08 further steps to loop; 10 in total
	How I Met Your Mother                             Hit tree after 01 steps - 09 further steps to loop; 10 in total
	Academy Awards                                    Hit tree after 06 steps - 05 further steps to loop; 11 in total
	Lil Wayne                                         Hit tree after 08 steps - 14 further steps to loop; 22 in total
	Kim Kardashian                                    Hit tree after 04 steps - 20 further steps to loop; 24 in total
	Australia                                         Hit tree after 03 steps - 10 further steps to loop; 13 in total
	Cristiano Ronaldo                                 Hit tree after 03 steps - 13 further steps to loop; 16 in total
	XHamster                                          Hit tree after 05 steps - 04 further steps to loop; 09 in total
	Miley Cyrus                                       Hit tree after 15 steps - 05 further steps to loop; 20 in total
	Elizabeth II                                      Hit tree after 07 steps - 11 further steps to loop; 18 in total
	List of Presidents of the United States           Hit tree after 00 steps - 16 further steps to loop; 16 in total
	Harry Potter                                      Hit tree after 06 steps - 18 further steps to loop; 24 in total
	Rihanna                                           Hit tree after 08 steps - 05 further steps to loop; 13 in total
	Japan                                             Hit tree after 01 steps - 13 further steps to loop; 14 in total
	Selena Gomez                                      Hit tree after 05 steps - 16 further steps to loop; 21 in total
	Glee (TV series)                                  Hit tree after 08 steps - 21 further steps to loop; 29 in total
	Germany                                           Hit tree after 01 steps - 13 further steps to loop; 14 in total
	The Walking Dead (TV series)                      Hit tree after 03 steps - 08 further steps to loop; 11 in total
	Abraham Lincoln                                   Hit tree after 01 steps - 16 further steps to loop; 17 in total
	Taylor Swift                                      Hit tree after 07 steps - 13 further steps to loop; 20 in total
	Star Wars                                         Hit tree after 02 steps - 08 further steps to loop; 10 in total
	Indigenous australian                             Hit tree after 03 steps - 12 further steps to loop; 15 in total
	China                                             Hit tree after 02 steps - 11 further steps to loop; 13 in total
	Lionel Messi                                      Hit tree after 11 steps - 06 further steps to loop; 17 in total
	Breaking Bad                                      Hit tree after 02 steps - 08 further steps to loop; 10 in total
	Johnny Depp                                       Hit tree after 03 steps - 10 further steps to loop; 13 in total
	New York City                                     Hit tree after 10 steps - 04 further steps to loop; 14 in total
	Tupac Shakur                                      Hit tree after 01 steps - 19 further steps to loop; 20 in total
	Web scraping                                      Hit tree after 02 steps - 23 further steps to loop; 25 in total
	France                                            Hit tree after 03 steps - 10 further steps to loop; 13 in total
	Kanye West                                        Hit tree after 07 steps - 03 further steps to loop; 10 in total
	Russia                                            Hit tree after 02 steps - 18 further steps to loop; 20 in total
	Stephen Hawking                                   Hit tree after 05 steps - 07 further steps to loop; 12 in total
	Albert Einstein                                   Hit tree after 02 steps - 05 further steps to loop; 07 in total
	Earth                                             Hit tree after 00 steps - 09 further steps to loop; 09 in total
	Angelina Jolie                                    Hit tree after 02 steps - 10 further steps to loop; 12 in total
	Mark Zuckerberg                                   Hit tree after 01 steps - 06 further steps to loop; 07 in total
	Internet Movie Database                           Hit tree after 05 steps - 20 further steps to loop; 25 in total
	Leonardo DiCaprio                                 Hit tree after 02 steps - 15 further steps to loop; 17 in total
	Nicki Minaj                                       Hit tree after 03 steps - 15 further steps to loop; 18 in total
	William Shakespeare                               Hit tree after 05 steps - 12 further steps to loop; 17 in total
	Michael Jordan                                    Hit tree after 02 steps - 14 further steps to loop; 16 in total
	Dwayne Johnson                                    Hit tree after 05 steps - 14 further steps to loop; 19 in total
	Katy Perry                                        Hit tree after 03 steps - 10 further steps to loop; 13 in total
	Illuminati                                        Hit tree after 06 steps - 08 further steps to loop; 14 in total
	Doctor Who                                        Hit tree after 06 steps - 12 further steps to loop; 18 in total
	Mila Kunis                                        Hit tree after 03 steps - 11 further steps to loop; 14 in total
	Vietnam War                                       Hit tree after 06 steps - 04 further steps to loop; 10 in total
	John F. Kennedy                                   Hit tree after 01 steps - 16 further steps to loop; 17 in total
	Adele                                             Hit tree after 04 steps - 09 further steps to loop; 13 in total
	Sexual intercourse                                Hit tree after 06 steps - 05 further steps to loop; 11 in total
	Human penis size                                  Hit tree after 03 steps - 06 further steps to loop; 09 in total
	One Direction                                     Hit tree after 03 steps - 10 further steps to loop; 13 in total
	Favicon.ico                                       Hit tree after 01 steps - 18 further steps to loop; 19 in total
	Global warming                                    Hit tree after 01 steps - 09 further steps to loop; 10 in total
	London                                            Hit tree after 01 steps - 18 further steps to loop; 19 in total
	John Cena                                         Hit tree after 08 steps - 07 further steps to loop; 15 in total
	Muhammad Ali                                      Hit tree after 04 steps - 16 further steps to loop; 20 in total
	List of The Big Bang Theory episodes              Hit tree after 01 steps - 10 further steps to loop; 11 in total
	Vagina                                            Hit tree after 03 steps - 18 further steps to loop; 21 in total
	Jay-Z                                             Hit tree after 05 steps - 14 further steps to loop; 19 in total
	Bill Gates                                        Hit tree after 04 steps - 16 further steps to loop; 20 in total
	Arnold Schwarzenegger                             Hit tree after 03 steps - 16 further steps to loop; 19 in total
	Will Smith                                        Hit tree after 06 steps - 10 further steps to loop; 16 in total
	September 11 attacks                              Hit tree after 03 steps - 12 further steps to loop; 15 in total
	Halloween                                         Hit loop after 02 steps 
	Prince (musician)                                 Hit tree after 07 steps - 03 further steps to loop; 10 in total
	David Bowie                                       Hit tree after 01 steps - 13 further steps to loop; 14 in total
	England                                           Hit tree after 02 steps - 14 further steps to loop; 16 in total
	Singapore                                         Hit tree after 04 steps - 15 further steps to loop; 19 in total
	Pornography                                       Hit tree after 00 steps - 08 further steps to loop; 08 in total
	Israel                                            Hit tree after 03 steps - 11 further steps to loop; 14 in total
	Bruce Lee                                         Hit tree after 05 steps - 12 further steps to loop; 17 in total
	Java                                              Hit tree after 02 steps - 11 further steps to loop; 13 in total
	Marilyn Monroe                                    Hit tree after 04 steps - 03 further steps to loop; 07 in total
	Britney Spears                                    Hit tree after 04 steps - 15 further steps to loop; 19 in total
	Grey's Anatomy                                    Hit loop after 09 steps 
	Tom Cruise                                        Hit tree after 01 steps - 11 further steps to loop; 12 in total
	Brazil                                            Hit tree after 02 steps - 11 further steps to loop; 13 in total
	LeBron James                                      Hit tree after 01 steps - 15 further steps to loop; 16 in total
	RMS Titanic                                       Hit tree after 08 steps - 05 further steps to loop; 13 in total
	Amazon.com                                        Hit tree after 02 steps - 18 further steps to loop; 20 in total
	Naruto                                            Hit tree after 03 steps - 13 further steps to loop; 16 in total
	Masturbation                                      Hit tree after 05 steps - 04 further steps to loop; 09 in total
	AMGTV                                             Hit tree after 04 steps - 18 further steps to loop; 22 in total
	English language                                  Hit tree after 05 steps - 13 further steps to loop; 18 in total
	Lost (TV series)                                  Hit tree after 02 steps - 08 further steps to loop; 10 in total
	American Civil War                                Hit tree after 01 steps - 15 further steps to loop; 16 in total
	Henry VIII of England                             Hit tree after 03 steps - 13 further steps to loop; 16 in total
	Scarlett Johansson                                Hit tree after 03 steps - 11 further steps to loop; 14 in total