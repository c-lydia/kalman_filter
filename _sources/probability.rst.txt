Probability
===========

.. attention::

    We won't be covering all probability theory. This section focuses on multiple random variables and stochastic processes.


Multiple Random Variables
-------------------------

CDF
^^^

If :math:`X` and :math:`Y` are random variables (RVs), their cumulative distribution functions (CDFs) are

.. math::

    F_X(x) = P\bigl(X \le x\bigr)

.. math::

    F_Y(y) = P\bigl(Y \le y\bigr)

The joint CDF is

.. math::

    F_{X,Y}(x, y) = P\bigl(X \le x,\; Y \le y\bigr)

Properties of the joint CDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

    0 \le F_{X,Y}(x,y) \le 1

.. math::

    \lim_{x\to -\infty} F_{X,Y}(x,y) = 0, \quad \lim_{y\to -\infty} F_{X,Y}(x,y)=0

.. math::

    \lim_{x,y\to\infty} F_{X,Y}(x,y) = 1

.. math::

    	ext{if } a\le b \text{ and } c\le d,\quad F_{X,Y}(a,c) \le F_{X,Y}(b,d)

.. math::

    P\bigl(a < X \le b,\; c < Y \le d\bigr) = F_{X,Y}(b,d) - F_{X,Y}(a,d) - F_{X,Y}(b,c) + F_{X,Y}(a,c)

Joint PDF
^^^^^^^^^

When :math:`X` and :math:`Y` are (jointly) continuous, the joint probability density function (PDF) is the mixed partial derivative of the joint CDF:

.. math::

    f_{X,Y}(x, y) = \frac{\partial^2}{\partial x\partial y} F_{X,Y}(x,y)

Equivalently,

.. math::

    F_{X,Y}(x,y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{X,Y}(u,v)\,dv\,du

Properties of the joint PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

    f_{X,Y}(x,y) \ge 0

.. math::

    \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx\,dy = 1

.. math::

    P\bigl(a < X \le b,\; c < Y \le d\bigr) = \int_a^b \int_c^d f_{X,Y}(x,y)\,dy\,dx

Marginal PDFs
^^^^^^^^^^^^^

.. math::

    f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy

.. math::

    f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx

For discrete random variables, replace PDFs with PMFs and integrals with sums.

