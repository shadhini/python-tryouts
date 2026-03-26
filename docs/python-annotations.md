---
icon: at
---

# Python Annotations

## Python Annotations

<table><thead><tr><th width="194.74609375" valign="top">Annotation</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>@staticmethod</code></td><td valign="top"><p>a utility function grouped with the class for organizational purposes</p><p>used when:</p><ul><li><p>the function is logically related to the class but doesn't need access to instance (<code>self</code>) or class (<code>cls</code>) data</p><ul><li>the method does not receive <code>self</code> (instance) or <code>cls</code> (class) as the first parameter</li><li>it cannot access or modify instance attributes or class attributes</li></ul></li><li>you want to namespace utility functions inside a class</li><li>the function could be standalone but grouping it with the class improves code organization</li></ul></td></tr><tr><td valign="top"><code>@lru_cache(maxsize=1)</code></td><td valign="top"><p><strong>LRU:</strong> "Least Recently Used"</p><p>a function caching mechanism from Python's <code>functools</code> module. </p><ul><li>caches the result of the function call</li><li><p><code>maxsize=1</code> means it will only store <strong>1 cached result</strong></p><ul><li>when function is called with the same arguments, it returns the cached results/instances instead of creating a new one - effectively making it a <strong>singleton</strong></li><li>ensures only one configuration instance exists for a given set of parameters</li><li>prevents redundant file reads and parsing</li><li>implements a singleton-like pattern without explicit singleton code</li></ul></li></ul></td></tr><tr><td valign="top"></td><td valign="top"></td></tr></tbody></table>

