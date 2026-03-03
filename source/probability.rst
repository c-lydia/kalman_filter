Probability
===========

.. attention::

    This section does not cover all probability theory. It focuses on multiple random variables and stochastic processes.


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

Expected value
^^^^^^^^^^^^^^

The expected value of a function :math:`g(\cdot, \cdot)` of two RVs is

.. math::

    E\bigl[g(X, Y)\bigr] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y)\,f_{X,Y}(x, y)\,dx\,dy

Statistical independence
------------------------

Random variables :math:`X` and :math:`Y` are independent if

.. math::

    P\bigl(X \le x,\; Y \le y\bigr) = P\bigl(X \le x\bigr)\,P\bigl(Y \le y \bigr), \quad \text{for all } x,y

From the definition of joint distribution and PDF, this implies

.. math::

    F_{X,Y}(x, y) = F_X(x)\,F_Y(y)

.. math::

    f_{X,Y}(x, y) = f_X(x)\,f_Y(y)

.. important::

    The central limit theorem says that the sum of independent RVs tends toward a Gaussian RV, regardless of the PDF of the individual RVs that contribute to the sum.

Covariance and correlation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We define the covariance of two scalar RVs :math:`X` and :math:`Y` as

.. math::

    C_{XY} = E\bigl[(X - E[X])(Y - E[Y])\bigr] = E[XY] - E[X]E[Y]

We define the correlation coefficient of two scalar RVs :math:`X` and :math:`Y` as

.. math::

    \rho = \frac{C_{XY}}{\sigma_X\,\sigma_Y}

.. important::

    The correlation is a normalized measure of linear dependence between two RVs :math:`X` and :math:`Y`.

    - If :math:`X` and :math:`Y` are independent, then :math:`\rho = 0`.
    - If :math:`Y` is a linear function of :math:`X`, then :math:`\rho = \pm 1`.

We define the (unnormalized) cross-correlation of two scalar RVs :math:`X` and :math:`Y` as

.. math::

    R_{XY} = E[XY]

.. important::

    Two RVs are said to be uncorrelated if :math:`R_{XY} = E[X]E[Y]`.

    From the definition of independence, if two RVs are independent, then they are uncorrelated. Independence implies uncorrelatedness, but uncorrelatedness does not imply independence. In the special case in which two RVs are Gaussian and uncorrelated, they are also independent.

    Two RVs are orthogonal if :math:`R_{XY} = 0`.

    If two RVs are uncorrelated, then they are orthogonal only if at least one of them has zero mean. If two RVs are orthogonal, they may or may not be uncorrelated.

Examples
^^^^^^^^

Die rolls
~~~~~~~~~

Two rolls of a fair six-sided die are represented by the RVs :math:`X` and :math:`Y`.

The two RVs are independent because one roll does not affect the other. Each face has probability :math:`1/6`.

.. math::

    E[X] = E[Y] = \frac{1+2+3+4+5+6}{6} = 3.5

There are :math:`36` equally likely combinations of the two rolls. The (cross-)correlation is

.. math::

    R_{XY} = E[XY] = \frac{1}{36}\sum_{i=1}^{6}\sum_{j=1}^{6} ij = 12.25

.. math::

    E[X]E[Y] = 3.5 \cdot 3.5 = 12.25

Thus :math:`E[XY] = E[X]E[Y]`, so :math:`X` and :math:`Y` are uncorrelated.

Dependent opposite outcomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A rigged machine: on the first spin :math:`X` takes values :math:`1` or :math:`-1` with probability :math:`1/2` each, and the second spin :math:`Y` is always the opposite (so :math:`Y=-X`). The possible outcomes are :math:`(1,-1)` and :math:`(-1,1)`.

.. math::

    E[X] = 0, \quad E[Y] = 0

.. math::

    E[XY] = \frac{(1)(-1) + (-1)(1)}{2} = -1

Since :math:`E[XY] \neq E[X]E[Y]`, these variables are correlated; since :math:`E[XY] \neq 0` they are not orthogonal.

Dependent conditional outcomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the first spin :math:`X` takes values :math:`-1,0,1` equally likely. On the second spin define :math:`Y=1` if :math:`X=0`, otherwise :math:`Y=0`.

.. math::

    E[X] = \frac{-1 + 0 + 1}{3} = 0

.. math::

    E[Y] = \frac{0 + 1 + 0}{3} = \frac{1}{3}

.. math::

    E[XY] = \frac{0 + 0 + 0}{3} = 0

Here :math:`E[XY] = E[X]E[Y]`, so :math:`X` and :math:`Y` are uncorrelated; and :math:`E[XY]=0` so they are orthogonal.

Sum of independent RVs
~~~~~~~~~~~~~~~~~~~~~~

Suppose :math:`X` and :math:`Y` are independent RVs, and define :math:`Z = g(X) + h(Y)`. Then

.. math::

        \begin{aligned}
        E[Z] &= E[g(X)+h(Y)] \\
                 &= \iint (g(x)+h(y))\,f_{X,Y}(x,y)\,dx\,dy \\
                 &= \iint (g(x)+h(y))\,f_X(x)f_Y(y)\,dx\,dy \\
                 &= \int g(x)f_X(x)\,dx \int f_Y(y)\,dy \\
                 &\quad + \int h(y)f_Y(y)\,dy\int f_X(x)\,dx \\
                 &= E[g(X)] + E[h(Y)]
        \end{aligned}

Therefore the mean of the sum of two independent RVs equals the sum of their means:

.. math::

    E[X+Y] = E[X] + E[Y]

Expected value of the sum of outcomes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose we roll a die twice

We use :math:`X` and :math:`Y` to refer to the two rolls of the die

:math:`Z` represents the sum of the two outcomes

Then :math:`Z = X + Y`

Since :math:`X` and :math:`Y` are independent, we have

.. math:: 

    E\bigl(Z\bigr) = E\bigl(X\bigr) + E\big(Y\bigr) = 3.5 + 3.5 = 7

Multivariate statistics
-----------------------

Given an n-element RV :math:`X` and an m-element RV :math:`Y`

:math:`X` and :math:`Y` are comlumn vectors

Correlation
^^^^^^^^^^^

Their correlation is defined as 

.. math:: 

    R_{XY} &= E\bigl(XY^{T}\bigr) \\
           &= \begin{bmatrix}
              E\bigl(X_{1}Y_{1}\bigr) & \cdots & E\bigl(X_{1}Y_{m}\bigr) \\
              \vdots & \ddots & \vdots \\
              E\bigl(X_{n}Y_{1} & \cdots & E\bigl(X_{n}Y_{m}\bigr)
              \end{bmatrix}

Covariance
^^^^^^^^^^

Their covariance is defined as 

.. math:: 

    C_{XY} &= E\bigl[\bigl(X - \bar{X}\bigr)\bigl(Y - \bar{Y}\bigr)^{T}\bigr] \\
           &= E\bigl(XY^{T}\bigr) - \bar{X}\bar{Y}^{T}

Autocorrelation 
^^^^^^^^^^^^^^^

The autocorrelation of th n-element RV :math:`X` is defined as 

.. math::

    R_{X} &= E\bigl[XX^{T}\bigr] \\
          &= \begin{bmatrix}
             E\bigl[X_{1}^{2}\bigr] & \cdots & E\bigl[X_{1}X_{n}\bigr] \\
             \vdots & \ddots & \vdots \\
             E\bigl[X_{n}X_{1}\bigr] & \cdots & E\bigl[X_{n}^{2}\bigr]
             \end{bmatrix}

Since :math:`E\bigl(X_{i}X_{j}\bigr) = E\bigl(X_{j}X_{i}\bigr)`, then :math:`R_{X} = R_{X}^{T}`

.. important::

    An autocorrelation matrix is always symmetric.

For any n-element column vector :math:`z`, we have

.. math::

    z^{T}R_{X}z &= z^{T}E\bigl[XX^{T}\bigr]z \\
                &= E\bigl[z^{T}XX^{T}z\bigr] \\
                &= E\bigl[\bigl(z^{T}X\bigr)^{2}\bigr] \\
                &\ge 0

.. important::

    An autocorrelation matrix is always positive semidefinite.

Autocovariance
^^^^^^^^^^^^^^

The autocovariance of the n-element RV :math:`X` is defined as

.. math::

    C_{X} &= E\bigl[\bigl(X - \bar{X}\bigr)\bigl(X - \bar{X}\bigr)^{T}\bigr] \\
          &= \begin{bmatrix}
             E\bigl[\bigl(X_{1} - \bar{X_{1}}\bigr)^{2}\bigr] & \cdots & E\bigl[\bigl(X_{1} - \bar{X_{1}}\bigr)\bigl(X_{n} - \bar{X_{n}}\bigr)\bigr] \\
             \vdots & \ddots & \vdots \\
             E\bigl[\bigl(X_{n} - \bar{X_{n}}\bigr)\bigl(X_{1} - \bar{X_{1}}\bigr)\bigr] & \cdots & E\bigl[\bigl(X_{n} - \bar{X_{n}}\bigr)^{2}\bigr]
             \end{bmatrix} \\
          &= \begin{bmatrix}
             \sigma_{1}^{2} & \cdots & \sigma_{1n} \\
             \vdots & \ddots & \vdots \\
             \sigma_{n1} & \cdots & \sigma_{n}^{2}
             \end{bmatrix}

Since :math:`\sigma_{ij} = \sigma_{ji}`, then :math:`C_{X} = C_{X}^{T}`

.. important::

    An autocovariance matrix is always symmetric

For any n-element column vector :math:`z`, we have

.. math::

    z^{T}C_{X}z &= z^{T}E\bigl[\bigl(X - \bar{X}\bigr)\bigl(X - \bar{X}\bigr)^{T}\bigr]z \\
                &= E\bigl[z^{T}\bigl(X - \bar{X}\bigr)\bigl(X - \bar{X}\bigr)^{T}z\bigr] \\
                &= E\bigl[\bigl(z^{T}\bigl(X - \bar{X}\bigr)\bigr)^{2}\bigr] \\
                &\ge 0

.. important::

    An autocovariance matrix is always positive semidefinite.

Gaussian RV
^^^^^^^^^^^

An n-element RV :math:`X` is multivariate Gaussian with mean :math:`\bar{X}` and covariance :math:`C_X` if its PDF is

.. math::

    f_X(x) = \frac{1}{(2\pi)^{\frac{n}{2}}\,|C_X|^{\frac{1}{2}}}\;e^{-\tfrac{1}{2}(X - \bar{X})^{T}C_X^{-1}(X - \bar{X})}

Linear transformation
~~~~~~~~~~~~~~~~~~~~~

Consider a Gaussian RV :math:`X` undergoes a linear transformation

.. math::

    Y = g\bigl(X\bigr) = AX + b 

Where :math:`A` is a constant :math:`n x n` matrix, and :math:`b` is a constant :math:`n`-element vector

If :math:`A` is invertible, then 

.. math:: 

    X = h\bigl(Y\bigr) = A^{-1}Y - A^{-1}b 

Normality
~~~~~~~~~

We have 

.. math:: 

    f_{Y}(y) &= |h'(y)|f_{X}\bigl[h(y)\bigr] \\
             &= |A^{-1}|\frac{1}{(2\pi)^{\frac{n}{2}}\,|C_X|^{\frac{1}{2}}}\;e^{-\tfrac{1}{2}(A^{-1}y - A^{-1}b - \bar{x})^{T}C_X^{-1}(A^{-1}y - A^{-1}b - \bar{x})} \\
             &= |A^{-1}|\frac{1}{(2\pi)^{\frac{n}{2}}\,|C_X|^{\frac{1}{2}}}\;e^{-\tfrac{1}{2}(A^{-1}y - A^{-1}b - A^{-1}A\bar{x})^{T}C_X^{-1}(A^{-1}y - A^{-1}b - A^{-1}A\bar{x})} \\
             &= \frac{1}{(2\pi)^{\frac{n}{2}}\,|A||C_X|^{\frac{1}{2}}}\;e^{-\tfrac{1}{2}\bigl[A^{-1}y - A^{-1}\bigl(b - A\bar{x}\bigr)\bigr]^{T}C_X^{-1}\bigl[A^{-1}y - A^{-1}\bigl(b - A\bar{x}\bigr)\bigr]} \\
             &= \frac{1}{(2\pi)^{\frac{n}{2}}\,{A}^{\frac{1}{2}}|C_X|^{\frac{1}{2}}}|A^{T}|^{\frac{1}{2}}\;e^{-\tfrac{1}{2}(A^{-1}y - A^{-1}\bar{y})^{T}C_X^{-1}(A^{-1}y - A^{-1}\bar{y})} \\
             &= \frac{1}{(2\pi)^{\frac{n}{2}}\,|AC_XA^{T}|^{\frac{1}{2}}}\;e^{-\tfrac{1}{2}(y - \bar{y})^{T}\bigl(AC_X^{-1}A^{T}\bigr)(y - \bar{y})}

.. math:: 

    y \sim N\bigl(A\bar{x} + b, AC_{X}A^{T}\bigr)

.. important:: 

    Normality is preserved in linear transformation of random vectors.

Stochatsic processes
--------------------

A stochastic process :math:`X(t)` is an RV :math:`X` that changes with time.

Types of stochastic processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Continuous random process:** is a random process that the RV at each time is continuous and time is continuous
- **Discrete random process:** is a random process that the RV at each time is discrete and time is continuous 
- **Continuous random sequence:** is a random process that the RV at each time is continuous and time is discrete 
- **Discrete random sequence:** is a random process that the RV at each time is discrete and time is discrete

PDF
^^^

The PDF of :math:`X` is 

.. math::

    F_{X}(x, t) = P\bigl[X(t) \le x\bigr]

.. important::

    If :math:`X(t)` is a random vector, then the inequality above is an element-by element inequality

CDF
^^^

The CDF of :math:`X` is 

.. math::

    f_{X}(x, t) = \frac{dF_{X}(x, t)}{dx}

.. important::

    If :math:`X(t)` is a random vector, then the derivative above is taken once with respect to each element of :math:`x`

Mean
^^^^

The mean of :math:`X` is 

.. math::

    \bar{x}(t) = \int_{-\infty}^{\infty}xf(x, t)dx 

Covariance
^^^^^^^^^^

The covariance of :math:`X` is

.. math::

    \begin{aligned}
    C_X(t) &= E\bigl[(X(t)-\bar{x}(t))(X(t)-\bar{x}(t))^{T}\bigr] \\
           &= \int_{\mathbb{R}^n} \bigl[x-\bar{x}(t)\bigr]\bigl[x-\bar{x}(t)\bigr]^{T}\,f_X(x,t)\,dx
    \end{aligned}

Joint distribution
^^^^^^^^^^^^^^^^^^

Second-order PDF
~~~~~~~~~~~~~~~~

The second-order PDF of :math:`X` is defined as 

.. math::

    F(x_{1}, x_{2}, t_{1}, t_{2}) = P\bigl(X(t_{1}) \le x_{1}, X(t_{2}) \le x_{2}\bigr)

.. important::

    If :math:`X(t)` is a random vector, then the inequality above consists of :math:`2n` inequalities

Second-order CDF
~~~~~~~~~~~~~~~~

The second-oder CDF of :math:`X` is

.. math::

    f(x_{1}, x_{2}, t_{1}, t_{2}) = \frac{\partial^{2}F(x_{1}, x_{2}, t_{1}, t_{2})}{\partial x_{1} \partial x_{2}}

.. important::  

    If :math:`X(t)` is a random vector, the derivative above consists of :math:`2n` derivatives

Autocorrelation
~~~~~~~~~~~~~~~

The correlation between two RVs :math:`X(t_{1})` and :math:`X(t_{2})` is called the autocorrelation of the stochastic process :math:`X(t)`  

.. math::

    R_{X}(t_{1}, t_{2}) = E\bigl[X(t_{1})X^{T}(t_{2})\bigr]

Autocovariance
~~~~~~~~~~~~~~

The autocovariance of a stochastic process is defined as 

.. math::

    C_{X}(t_{1}, t_{2}) = E\bigl[\bigl(X(t_{1}) - \bar{X}(t_{1})\bigr)\bigl(X(t_{2}) - \bar{X}(t_{2})\bigr)^{T}\bigr]

Strict-sense stationary process: SSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Strict-sense stationary (SSS) stochastic process is a stochastic process for which the PDF does not change with time. 

.. important::

    The mean of the stationary stochastic process is constant with respect to time, and the autocorrelation is a function of the time difference :math:`t_{2} - t_{1}` 

.. math::

    \begin{aligned}
    \bar{x} &= E\bigl[X(t)\bigr] \\
    R_X(t_{2} - t_{1}) &= E\bigl[X(t_{1})X^{T}(t_{2})\bigr] 
    \end{aligned}

Wide-sense stationary process: WSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wide-sense stationary (WSS) stachastic process is a stochastic process for which the PDF changes with time, but the mean is constant with resepct to time and the autocorrelation is a function of the time difference.

From the definition of autocorrelation, it can be shown taht for WSS process the following propeties hold

.. math::

    \begin{aligned}
    R_{X}(0) &= E\bigl[X(t)X^{T}(t)\bigr] \\
    R_{X}(-\tau) &= R_{X}(\tau)
    \end{aligned}

.. important::

    A stationary process is wide-sense srarionary, but a wide-sense stationary process may or may not be stationary

For scalar stichastic processes, it can be shown that 

.. math::

    |R_{X}(\tau)| \le R_{X}(0)

Ergodic process
^^^^^^^^^^^^^^^

Suppose we have a stochastic process :math:`X(t)`

Suppose that the process has a realization :math:`x(t)` 

The time average of :math:`X(t)` is defined, in continuous-time random processes, as

.. math::

    A\bigl[X(t)\bigr] = \lim_{T \to \infty} \frac{1}{2T}\int_{-T}^{T}x(t)dt

The time autocorrelation of :math:`X(t)` is defined, in continuouse-time random processes, as

.. math::

    R\bigl[X(t), \tau\bigr] = A\bigl[X(t)X^{T}(t + \tau)\bigr]

.. important:: 

    Discrete-time random processes are straightforward extensions of the continuous-timer random processes

An ergodic process is a stationary random process for which

.. math::

    \begin{aligned}
    E\bigl(X\bigr) &= A\bigl[X(t)\bigr] \\
    R_{X}(\tau) &= R\bigl[X(t), \tau\bigr]
    \end{aligned}

.. important::

    If the random process is ergodic, then we can use those time averages to estimate the statistics of the stochastic process

Cross correlation and cross covariance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cross correlation of :math:`X(t)` and :math:`Y(t)` is defined as 

.. math::

    R_{XY}(t_{1}, t_{2}) = E\bigl[X(t_{1})Y^{T}(t_{2})\bigr]

Two random processes :math:`X(t)` and :math:`Y(t)` are said to be uncorrelated if :math:`R_{XY}(t_{1}, t_{2}) = E\bigl[X(t_{1})\bigr]E\bigl[Y^{T}(t_{2})\bigr]` for all :math:`t_{1}` and :math:`t_{2}`

The cross covariance of :math:`X(t)` and :math:`Y(t)` is defined as 

.. math::

    C_{XY}(t_{1}, t_{2}) = E\bigl[\bigl(X(t_{1}) - \bar{X}(t_{1})\bigr)\bigl(Y(t_{2}) - \bar{Y}(t_{2})\bigr)^{T}\bigr]

White noise and colored noise
-----------------------------

If the RV :math:`X(t_{1})` is independent from the RV :math:`X(t_{2})` for all :math:`t_{1} \neq t_{2}`, then :math:`X(t)` is called white noise; otherwise, :math:`X(t)` is called colored noise

The power spectrum :math:`S_{X}(\omega)` of a wide-sense stationaru stochastic process :math:`X(t)` is defined as the Fourier trnasform os the autocorrelation.

.. math::

    \begin{aligned}
    S_{X}(\omega) &= \int_{-\infty}^{\infty}R_{X}(\tau)e^{-j\omega\tau}d\tau \\
    R_{X}(\tau) &= \frac{1}{2\pi}\int_{-\infty}^{\infty}S_{X}(\omega)e^{j\omega\tau}d\omega
    \end{aligned}

These equations are called the Wiener-Khintchine relations after Norbert Wiener anf Aleksandr Khinchin.

The power of a wide-sense stationaru stochastic process is defined as 

.. math::

    P_{X} = \frac{1}{2\pi}\int_{-\infty}^{\infty}S_{X}(\omega)d\omega

The cross correlation of a wide-sense stationary stochastic process is the inverse Fourier transform of the cross power spectrum of two wide-sense stationary stochastic processes :math:`X(t)` and :math:`Y(t)` 

.. math::

    \begin{aligned}
    S_{XY}(\omega) &= \int_{-\infty}^{\infty}R_{XY}(\tau)e^{-j\omega\tau}d\tau \\
    R_{XY}(\tau) &= \frac{1}{2\pi}\int_{-\infty}^{\infty}S_{XY}(\omega)d^{j\omega\tau}d\omega
    \end{aligned}

The power spectrum of a discrete-time random process is defined as 

.. math::

    \begin{aligned}
    S_{X}(\omega) &= \sum_{k = -\infty}^{\infty}R_{X}(k)e^{-j\omega k}, \omega \in [-\pi, \pi] \\
    R_{X}(k) &= \frac{1}{2\pi}\int_{-\infty}^{\infty}S_{X}(\omega)e^{j\omega k}d\omega 
    \end{aligned}

A discrete-time stochastic process :math:`X(t)` is called wite noise if 

.. math:: 

    R_{X}(k) = \begin{cases}
               \sigma^2, k=0 \\
               0, k\neq 0
               \end{cases}

where :math:`\delta_{k}` is the kronecker delta function, defined as 

.. math::

    \delta_{k} = \begin{cases}
                 1, k = 0 \\
                 0, k \neq 0
                 \end{cases}

If :math:`X(t)` is a dicrete-time white noise process, then the RV :math:`X(n)` is uncorrelated with :math:`X(m)` unless :math:`m = n` 

The power of a discrete-time white noise process is equal at all frequencies

.. math::

    S_{X}(\omega) = R_{X}(0), \omega \in [-\pi, \pi]

For a continuous-time random process, white noise has equal power at all frequencies

.. math:: 

    S_{X}(\omega) = R_{X}(0)

Substitute this expression for :math:`S_{X}(\omega)` into :math:`R_{X}(\tau)`, then for continuous-time white noise

.. math::

    R_{X}(\tau) = R_{X}(0)\delta(\tau)

where :math:`\delta(\tau)` is the continuous-time impulse function 

Example
^^^^^^^

Suppose that a zero-mean stationary stochsatic process has the autocoreelation function 

.. math::

    R_{X}(\tau) = \sigma^{2}e^{-\beta|\tau|}

where :math:`\beta` is a positive real number 


The power spectrum is computed as 

.. math:: 

    \begin{aligned}
    S_{X}(\omega) &= \int_{-\infty}^{\infty}\sigma^{2}e^{-\beta|\tau|}e^{-j\omega\tau}d\tau \\
                  &= \int_{-\infty}^{0}\sigma^{2}e^{(\beta - j\omega)\tau}d\tau + \int_{0}^{\infty}\sigma^{2}e^{-(\beta + j\omega)\tau}d\tau \\
                  &= \frac{\sigma^{2}}{\beta - j\omega} + \frac{\sigma^{2}}{\beta + j\omega} \\
                  &= \frac{2\sigma^{2}\beta}{\omega^{2} + \beta^{2}}
    \end{aligned}

The variance of stochastic process is computed as

.. math::

    \begin{aligned}
    E\bigl[X^{2}(t)\bigr] &= \frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{2\sigma^{2}\beta}{\omega^{2} + \beta^{2}}\,d\omega \\
                          &= \frac{\sigma^{2}\beta}{\pi}\left[\frac{1}{\beta}\arctan\left(\frac{\omega}{\beta}\right)\right]_{-\infty}^{\infty} \\
                          &= \sigma^{2} \\
                          &= R_{X}(0)
    \end{aligned}
