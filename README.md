# site_generator

This Static Site Generator (SSG). project involves creating a software system that automates the conversion of raw content, like Markdown, into a structured and navigable HTML website. First, a parser translates text into an intermediate tree structure of nodes, which can then be converted into HTML strings. By utilizing a central HTML template, the system ensures that every generated page maintains a consistent layout and design, effectively separating the content from the presentation layer.

The engineering skills for this project center on data structure design and automated file processing. Key concepts include the implementation of recursive algorithms to traverse nested directory trees, which allows the system to mirror complex source hierarchies in the final output. Also, string manipulation for pattern matching, the application of Object-Oriented Programming to model document hierarchies, and unit testing to ensure the reliability of the transformation logic.

The logic behind a custom SSG is the foundation for widely used industry tools such as Hugo, Jekyll, and Eleventy. Beyond web development, programmatically walking a file system and transforming data from one format to another is important for building CI/CD pipelines, documentation generators, and data migration scripts. These techniques are useful for any backend or systems engineering task that requires processing large volumes of unstructured data into organized, usable assets.

