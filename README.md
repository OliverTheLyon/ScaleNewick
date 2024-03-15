<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- ABOUT THE PROJECT -->
## About The Project

This is really a tool that I use frequently. As an evolutionary biologist and bioinforatician, I am working with phylogenetic tree reconstructions with various branch lengths.
Often they are in nucliotide substitutions, rate of neutral substituion, rate of codon substitution etc... 
Addtionally, when testing evolutionary models I want to see how tree depth impacts the results, scalling the tree quickly helps.

I made this repo, mostly so I can find the file quickly and easily, but so others don't have to take 15 min to wite it again.

Cheers!

OASL.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

1. Download ScaleNewick.py into your local directory
   ```sh
   git clone https://github.com/OliverTheLyon/ScaleNewick.git
   ```
2. Run Scale Newick
   ```sh
   python3 ScaleNewick.py InputTree.nwk ScaleFactor Outputfile.nwk
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

newick.nwk
  ```sh
  (A:0.1,B:0.2,(C:0.3,D:0.4):0.5);
  ```
Run Scale Newick
   ```sh
   python3 ScaleNewick.py newick.nwk 10 scalenewick.nwk
   ```

scalenewick.nwk
  ```sh
  (A:1.0,B:2.0,(C:3.0,D:4.0):5.0);
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
