=====================
web.dispatch.resource
=====================

    © 2009-2016 Alice Bevan-McGregor and contributors.

..

    https://github.com/marrow/web.dispatch.resource

..

    |latestversion| |ghtag| |masterstatus| |mastercover| |masterreq| |ghwatch| |ghstar|



Introduction
============

Dispatch is the process of taking some starting point and a path, then resolving the object that path refers to. This
process is common to almost every web application framework (transforming URLs into controllers), RPC system, and even
filesystem shell. Other terms for this process include: "traversal", "routing", or "lookup".

Resource dispatch utilizes the HTTP verb (provided as the `HTTP_METHOD` WSGI environment variable) to determine which
method to call.

This package speaks a standardized `dispatch protocol <https://github.com/marrow/WebCore/wiki/Dispatch-Protocol>`__
and is not entirely intended for direct use by most developers. The target audience is instead the authors of
frameworks that may require such modular dispatch for use by their own users.


Installation
============

Installing ``web.dispatch.resource`` is easy, just execute the following in a terminal::

    pip install web.dispatch.resource

**Note:** We *strongly* recommend always using a container, virtualization, or sandboxing environment of some kind when
developing using Python; installing things system-wide is yucky (for a variety of reasons) nine times out of ten.  We
prefer light-weight `virtualenv <https://virtualenv.pypa.io/en/latest/virtualenv.html>`__, others prefer solutions as
robust as `Vagrant <http://www.vagrantup.com>`__.

If you add ``web.dispatch.resource`` to the ``install_requires`` argument of the call to ``setup()`` in your
application's ``setup.py`` file, this dispatcher will be automatically installed and made available when your own
application or library is installed.  We recommend using "less than" version numbers to ensure there are no
unintentional side-effects when updating.  Use ``web.dispatch.resource<2.1`` to get all bugfixes for the current release,
and ``web.dispatch.resource<3.0`` to get bugfixes and feature updates while ensuring that large breaking changes are not
installed.


Development Version
-------------------

    |developstatus| |developcover| |ghsince| |issuecount| |ghfork|

Development takes place on `GitHub <https://github.com/>`__ in the 
`web.dispatch.resource <https://github.com/marrow/web.dispatch.resource/>`__ project.  Issue tracking, documentation,
and downloads are provided there.

Installing the current development version requires `Git <http://git-scm.com/>`_, a distributed source code management
system.  If you have Git you can run the following to download and *link* the development version into your Python
runtime::

    git clone https://github.com/marrow/web.dispatch.resource.git
    (cd web.dispatch.resource; python setup.py develop)

You can then upgrade to the latest version at any time::

    (cd web.dispatch.resourec; git pull; python setup.py develop)

If you would like to make changes and contribute them back to the project, fork the GitHub project, make your changes,
and submit a pull request.  This process is beyond the scope of this documentation; for more information see
`GitHub's documentation <http://help.github.com/>`_.


Usage
=====

This section is split to cover framework authors who will need to integrate the overall protocol into their systems,
and the object interactions this form of dispatch provides for end users.



Version History
===============

Version 2.0
-----------

* Extract of the object dispatch mechanism from WebCore.

Version 1.x
-----------

* Process fully integrated in the WebCore web framework.


License
=======

web.dispatch.resource has been released under the MIT Open Source license.

The MIT License
---------------

Copyright © 2009-2016 Alice Bevan-McGregor and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


.. |ghwatch| image:: https://img.shields.io/github/watchers/marrow/web.dispatch.resource.svg?style=social&label=Watch
    :target: https://github.com/marrow/web.dispatch.resource/subscription
    :alt: Subscribe to project activity on Github.

.. |ghstar| image:: https://img.shields.io/github/stars/marrow/web.dispatch.resource.svg?style=social&label=Star
    :target: https://github.com/marrow/web.dispatch.obresourceject/subscription
    :alt: Star this project on Github.

.. |ghfork| image:: https://img.shields.io/github/forks/marrow/web.dispatch.resource.svg?style=social&label=Fork
    :target: https://github.com/marrow/web.dispatch.resource/fork
    :alt: Fork this project on Github.

.. |masterstatus| image:: http://img.shields.io/travis/marrow/web.dispatch.resource/master.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.resource/branches
    :alt: Release build status.

.. |mastercover| image:: http://img.shields.io/codecov/c/github/marrow/web.dispatch.resource/master.svg?style=flat
    :target: https://codecov.io/github/marrow/web.dispatch.resource?branch=master
    :alt: Release test coverage.

.. |masterreq| image:: https://img.shields.io/requires/github/marrow/web.dispatch.resource.svg
    :target: https://requires.io/github/marrow/web.dispatch.resource/requirements/?branch=master
    :alt: Status of release dependencies.

.. |developstatus| image:: http://img.shields.io/travis/marrow/web.dispatch.resource/develop.svg?style=flat
    :target: https://travis-ci.org/marrow/web.dispatch.resource/branches
    :alt: Development build status.

.. |developcover| image:: http://img.shields.io/codecov/c/github/marrow/web.dispatch.resource/develop.svg?style=flat
    :target: https://codecov.io/github/marrow/web.dispatch.resource?branch=develop
    :alt: Development test coverage.

.. |developreq| image:: https://img.shields.io/requires/github/marrow/web.dispatch.resource.svg
    :target: https://requires.io/github/marrow/web.dispatch.resource/requirements/?branch=develop
    :alt: Status of development dependencies.

.. |issuecount| image:: http://img.shields.io/github/issues-raw/marrow/web.dispatch.resource.svg?style=flat
    :target: https://github.com/marrow/web.dispatch.resource/issues
    :alt: Github Issues

.. |ghsince| image:: https://img.shields.io/github/commits-since/marrow/web.dispatch.resource/2.1.0.svg
    :target: https://github.com/marrow/web.dispatch.resource/commits/develop
    :alt: Changes since last release.

.. |ghtag| image:: https://img.shields.io/github/tag/marrow/web.dispatch.resource.svg
    :target: https://github.com/marrow/web.dispatch.resource/tree/2.1.0
    :alt: Latest Github tagged release.

.. |latestversion| image:: http://img.shields.io/pypi/v/web.dispatch.resource.svg?style=flat
    :target: https://pypi.python.org/pypi/web.dispatch.resource
    :alt: Latest released version.

.. |cake| image:: http://img.shields.io/badge/cake-lie-1b87fb.svg?style=flat
