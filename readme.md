# wiki to philosophy

[![tweet](twitter.png)](https://twitter.com/davelevitan/status/935619980594466816)

Also described [here](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy).

So. Here it is. In Python. With Beautiful soup. Obviously.

Also: I disproved the hypothesis: there are many loops (`/wiki/Accounting`), (`/wiki/Cardinal_direction`)

## Result

![dot](graph/en/dot.png)
![neato](graph/en/neato.png)

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

I decided to go past philosophy and see what is next. First almost all articles ended in a loop between knwoledge and fact. However someone recently edited the fact article, now the loop is much bigger.

## Command line Options

	usage: wiki.py [-h] [-c COUNT] [-g] [-l] [-p | -i INTERNATIONAL] [-r ROOT]
	               [-s] [-t] [-v]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c COUNT, --count COUNT
	                        amount of random pages
	  -g, --graph           creates graphs
	  -l, --load            use graph.json as source not web
	  -p, --popular         search most popular pages
	  -i INTERNATIONAL, --international INTERNATIONAL
	                        search in different language [default=en]
	  -r ROOT, --root ROOT  search just specified page[s], separated by ","
	  -s, --save            saves graph to json, -ss saves at every step
	  -t, --time            displays the time per online step
	  -v, --verbose         print entire path

## Acknowledgement

Thanks [@davelevitan](https://twitter.com/davelevitan) for bringing me this excelent challenge! It took about 2 hours.

## Sample output

### `./wiki.py --verbose --time --count 5`

	searching 5 random pages:
	---------------
	graph:    False
	save:     False
	time:     True
	verbose:  True
	---------------
	[1/5] Mutation testing
	    execution                                                              /wiki/Execution_(computers)
	    computer                                                               /wiki/Computer_engineering
	    discipline                                                             /wiki/Discipline_(academia)
	    knowledge                                                              /wiki/Knowledge
	    facts                                                                  /wiki/Fact
	    evidence                                                               /wiki/Evidence
	    assertion                                                              /wiki/Logical_assertion
	    mathematical logic                                                     /wiki/Mathematical_logic
	    mathematics                                                            /wiki/Mathematics
	    space                                                                  /wiki/Space
	    objects                                                                /wiki/Physical_body
	    physics                                                                /wiki/Physics
	    natural science                                                        /wiki/Natural_science
	    science                                                                /wiki/Science
	    knowledge                                                              /wiki/Knowledge
	    Hit loop after 15 steps 0.6s/page
	[2/5] John Connor (Illinois politician)
	    Emily McAsey                                                           /wiki/Emily_McAsey
	    Democratic                                                             /wiki/Democratic_Party_(United_States)
	    two                                                                    /wiki/Two-party_system
	    major                                                                  /wiki/Major_party
	    political party                                                        /wiki/Political_party
	    elections                                                              /wiki/Election
	    group decision-making process                                          /wiki/Group_decision-making
	    individuals                                                            /wiki/Individuals
	    person                                                                 /wiki/Person
	    reason                                                                 /wiki/Reason
	    facts                                                                  /wiki/Fact
	    Hit tree after 11 steps 0.7s/page - 11 further steps to loop; 22 in total
	[3/5] Brenda Elliott
	    politician                                                             /wiki/Politician
	    party                                                                  /wiki/Political_party
	    Hit tree after 02 steps 0.3s/page - 17 further steps to loop; 19 in total
	[4/5] Gravitino
	    supergravity                                                           /wiki/Supergravity
	    theoretical physics                                                    /wiki/Theoretical_physics
	    physics                                                                /wiki/Physics
	    Hit tree after 03 steps 0.5s/page - 11 further steps to loop; 14 in total
	[5/5] Resident Evil: Caliban Cove
	    Resident Evil                                                          /wiki/Resident_Evil
	    Japan                                                                  /wiki/Japan
	    sovereign                                                              /wiki/Sovereign_state
	    international law                                                      /wiki/International_law
	    states                                                                 /wiki/State_(polity)
	    political entity                                                       /wiki/Polity
	    identity                                                               /wiki/Identity_(social_science)
	    psychology                                                             /wiki/Psychology
	    behavior                                                               /wiki/Behavior
	    actions                                                                /wiki/Action_(philosophy)
	    philosophy                                                             /wiki/Philosophy
	    study                                                                  /wiki/Education
	    learning                                                               /wiki/Learning
	    knowledge                                                              /wiki/Knowledge
	    Hit tree after 14 steps 0.9s/page - 11 further steps to loop; 25 in total
	    
### `./wiki.py --count 5`

	searching 5 random pages:
	---------------
	graph:    False
	save:     False
	time:     False
	verbose:  False
	---------------
	[1/5] Pathinaaru                                        Hit loop after 23 steps
	[2/5] Angolan                                           Hit tree after 12 steps - 11 further steps to loop; 23 in total
	[3/5] Delhi Public School Aligarh                       Hit dead end after 01 steps
	[4/5] Pakistan at the 2014 Asian Beach Games            Hit loop after 06 steps
	[5/5] Owen Summers                                      Hit tree after 11 steps - 11 further steps to loop; 22 in total