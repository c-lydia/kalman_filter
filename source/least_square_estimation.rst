Least Square Estimation
=======================

Estimation of a constant
------------------------

Suppose :math:`x` is a constant but unknown n-element vector, and :math:`y` is a k-element noisy measurement vector

Assume that each element of the measurement vector :math:`y` is a linear combination of the elements of :math:`x` with the addition of some measurement noise

.. math::

    \begin{aligned}
    y_{1} &= H_{11}x_{1} + \cdots + H_{1n}x_{n} + v_{1} \\
    \vdots \\
    y_{k} &= H_{k1}x_{1} + \cdots + H_{kn}x_{n} + v_{k}
    \end{aligned}

This set of equations can be put into matrix form as 

.. math::

    y = Hx + v

Defined :math:`\epsilon_{k}` as the difference between the noisy measurements and the vector :math:`H\hat{x}` 

.. math:: 

    \epsilon_{y} = y - H\hat{x}

:math:`\epsilon_{y}` is called the measurement residual

The most probable value of the vector :math:`x` is the vector :math:`\hat{x}` that minimizes the sum of square between the observed values :math:`y` and the vector :math:`H\hat{x}`

We will be computing the :math:`\hat{x}` that minimizes the cost function 

The cost function :math:`J` is given as 

.. math:: 

    \begin{aligned}
    J &= \epsilon_{y1}^{2} + \cdots + \epsilon_{yk}^{2} \\
      &= \epsilon_{y}^{T}\epsilon_{y}
    \end{aligned}

Substitute :math:`\epsilon_{y}` into :math:`J`, we obtain 

.. math::

    \begin{aligned}
    J &= (y - H\hat{x})^{T}(y - H\hat{x}) \\
      &= y^{T}y - \hat{x}^{T}H^{T}y - y^{T}H\hat{x} + \hat{x}^{T}H^{T}\hat{x}
    \end{aligned}

Then 

.. math::

    \frac{\partial J}{\partial \hat{x}} = -y^{T}H - y^{T}H + 2\hat{x}^{T}H^{T}H 

Set 

.. math::

    \frac{\partial J}{\partial \hat{x}} = 0

We have 

.. math::

    -y^{T}H - y^{T}H + 2\hat{x}^{T}H^{T}H = 0

Solve for :math:`\hat{x}`, we obtain

.. math::

    \begin{aligned}
    H^{T}y &= H^{T}H\hat{x} \\
    \hat{x} &= \bigl(H^{T}H\bigr)^{-1}H^{T}y\\
            &= H^{L}y 
    \end{aligned}

where :math:`H_{L}` the left pseudo inverse of :math:`H`, exists if :math:`k \ge n` and :math:`H` is gull rank 

This means that the number of measurements :math:`k` is greater than the number of variables :math:`n` that we are trying to estimate, and the measurements are linearly independent

To prove that we found the minimum rather than some other type of stationary point, we need to prove that the second derivative of :math:`J` is positiive semidefinite

Example
^^^^^^^

We are trying to estimate the resistance :math:`x` of an unmarked resistor on the basis of :math:`k` noisy measurements from a multimeter

:math:`x` is a scalar, so :math:`k` noisy measurements are given as

.. math::

    \begin{aligned}
    y_{1} &= x + v_{1}\\
    \vdots \\
    y_{k} &= x + v_{k}
    \end{aligned}

It can be written in matrix form as 

.. math::

    \begin{bmatrix}
    y_{1} \\
    \vdots \\
    y_{k} 
    \end{bmatrix} =  \begin{bmatrix} 
                    1 \\ 
                    \vdots \\ 
                    1 
                    \end{bmatrix} x 
                    + 
                    \begin{bmatrix} 
                    v_1 \\ 
                    \vdots \\ 
                    v_k 
                    \end{bmatrix}

The optimal estimate of the resistance :math:`x` is given as

.. math::

    \begin{aligned}
    \hat{x} &= \bigl(H^{T}H\bigr)^{-1}H^{T}y \\
            &= \left(\begin{bmatrix}
                     1 & \cdots & 1 
                     \end{bmatrix}
                     \begin{bmatrix}
                     1 \\
                     \vdots \\
                     1 
                     \end{bmatrix}\right)^{-1} 
                     \begin{bmatrix}
                     1 & \cdots & 1
                     \end{bmatrix}
                     \begin{bmatrix}
                     y_{1} \\
                     \vdots \\
                     y_{k}
                     \end{bmatrix} \\
            &= \frac{1}{k}\bigl(y_{1} + \cdots + y_{k}\bigr)
    \end{aligned}

Weighted least squares estimation
---------------------------------

Suppose :math:`x` is aconstant but unknown n-element vector

And :math:`y` is a k-element noisy measurement vector

Assume that each element of :math:`y` is a linear combination of the elements of :math:`x` with the addition of some measurement noise

The variance of the measurement noise may be different of each element of :math:`k`

.. math::

    \begin{aligned}
    \begin{bmatrix}
    y_{1} \\
    \vdots \\
    y_{k}
    \end{bmatrix} &= \begin{bmatrix}
                     H_{11} & \cdots & H_{1n} \\
                     \vdots & \ddots & \vdots \\
                     H_{k1} & \cdots & H_{kn}
                     \end{bmatrix} 
                     \begin{bmatrix}
                     x_{1} \\
                     \vdots \\
                     x_{n} 
                     \end{bmatrix}
                     + 
                     \begin{bmatrix}
                     v_{1} \\
                     \vdots \\
                     v_{k}
                     \end{bmatrix} \\
    E\bigl(v_{i}^{2}\bigr) &= \sigma_{i}^{2}, i = 1, 2, \cdots, k
    \end{aligned}

Assume that the noise for each measurement is zero-mean and independent 

The measurement covariance matrix is

.. math::

    \begin{aligned}
    R &= E\bigl(vv^{T}\bigr)
      &= \begin{bmatrix}
         \sigma_{1}^{2} & \cdots & 0 \\
         \vdots & \ddots& \vdots \\
         0 & \cdots & \sigma_{k}^{2}
         \end{bmatrix}
    \end{aligned}

Minimize the cost function with respect to :math:`\hat{x}`

.. math::

    J = \frac{\epsilon_{y1}^{2}}{\sigma_{1}^{2}} + \cdots + \frac{\epsilon_{yk}^{2}}{\sigma_{k}^{2}}

If :math:`y_{1}` is a relatively noisy measurement, then we do not care much about minizing the difference between :math:`y_{1}` and the first element of :math:`H\hat{x}` because we do not have much confidence in :math:`y_{1}`

We will minimize the weighted sum of squares instead

The cost function can be written as

.. math::

    \begin{aligned}
    J &= \epsilon_{y}^{T}R^{-1}\epsilon_{y} \\
      &= (y - H\hat{x})^{T}R^{-1}(y - H\hat{x}) \\
      &= y^{T}R^{-1}y - \hat{x}^{T}H^{T}R^{-1}y - y^{T}R^{-1}H\hat{x} + \hat{x}^{T}H^{T}R^{-1}H\hat{x}
    \end{aligned}

Then 

.. math::

    \frac{\partial J}{\partial \hat{x}} = -y^{T}R^{-1}H + \hat{x}^{T}H^{T}R^{-1}H 

Set 

.. math::

     \frac{\partial J}{\partial \hat{x}} = 0

Compute :math:`\hat{x}`, we obtain 

.. math:: 

    \begin{aligned}
    0 &= -y^{T}R^{-1}H + \hat{x}^{T}H^{T}R^{-1}H \\
    H^{T}R^{-1}y &= H^{T}R^{-1}H\hat{x} \\
    \hat{x} &= \bigl(H^{T}R^{-1}H\bigr)^{-1}H^{T}R^{-1}y 
    \end{aligned}

.. important::

    This method requires that the measurement noise matrix :math:`R` be nonsingular, or each of the measurements :math:`y_{i}` must be correupted by at least some noise

Example
^^^^^^^

We are estimating the resistance :math:`x` ofan unmarked resistor on the basis of :math:`k` noisy measurements from a multimeter

:math:`x` is a scalar, so :math:`k` noisy measurements are given as

.. math::

    \begin{aligned}
    y_{i} &= x + v_{i} \\
    E\bigl(v_{i}^{2}\bigr) &= \sigma_{i}^{2}, i = 1, 2, \cdots, k 
    \end{aligned}

or in matrix form 

.. math::

    \begin{bmatrix} 
    y_{1} \\
    \vdots \\
    y_{k}
    \end{bmatrix} = \begin{bmatrix}
                    1 \\
                    \vdots \\
                    1 
                    \end{bmatrix} x
                    +
                    \begin{bmatrix}
                    v_{1} \\
                    \vdots \\
                    v_{k} 
                    \end{bmatrix}

The measurement noise covariance is given as 

.. math::

    R = diag\bigl(\sigma_{1}^{2}, \cdots, \sigma_{k}^{2}\bigr)

The optimal estimate of the resistance :math:`x` is givan as 

.. math::

    \begin{aligned}
    \hat{x} &= \bigl(H^{T}R^{-1}H\bigr)^{-1}H^{T}R^{-1}y \\
            &= \left(
               \begin{bmatrix}
               1 & \cdots & 1
               \end{bmatrix}
               \begin{bmatrix}
               \sigma_{1}^{2} & \cdots & 0 \\
               \vdots & \ddots & \vdots \\
               0 & \cdots & \sigma_{k}^{2}
               \end{bmatrix}^{-1}
               \begin{bmatrix}
               1 \\
               \vdots \\
               1 
               \end{bmatrix}
               \right)^{-1}
               \times
               \begin{bmatrix}
               1 & \cdots & 1
               \end{bmatrix}
               \begin{bmatrix} 
               \sigma_{1}^{2} & \cdots & 0 \\
               \vdots & \ddots & \vdots \\
               0 & \cdots & \sigma_{k}^{2} 
               \end{bmatrix}^{-1} 
               \begin{bmatrix}
               y_{1} \\
               \vdots \\
               y_{k}
               \end{bmatrix} \\
            &= \left(\sum \frac{1}{\sigma_{i}^{2}}\right)^{-1} \left(\frac{y_{1}}{\sigma_{1}^{2}} + \cdots + \frac{y_{k}}{\sigma_{k}^{2}}\right)
    \end{aligned}

Recursive least squares estimation
----------------------------------

In weighted least squares estimation, we can compute :math:`\hat{x}` as

.. math::

    \hat{x} = \bigl(H^{T}R^{-1}H\bigr)^{-1}H^{T}R^{-1}y 

The :math:`H` matrix is a :math:`k\times n` matrix 

If we obtain measurements sequantially and want to update our estimate of :math:`x` with each new measurement, we need to augment :math:`H` matrix and completely recompute the estimate :math:`\hat{x}`

If the number of measurements become large, the computational effort could become prohittive

The computational effort of least squares estimation can rapidly outgrpw our resoucres

We will rework our leats squares estimation recursively

Suppose we have :math:`\hat{x}` after :math:`k - 1` measurements

We obtain new measurement :math:`y_{k}` 

A linear recursive estimator can be written in the form

.. math::

    \begin{aligned}
    y_{k} &= H_{k}x + v_{k} \\
    \hat{x}_{k} &= \hat{x}_{k - 1} + K_{k}(y_{k} - H_{k}\hat{x}_{k - 1}) 
    \end{aligned}

where :math:`K_{k}` is the estimator gain matrix and :math:`y_{k} - H_{k}\hat{x}_{k - 1}` is the correction term 

If the correction term is zero, or if the gain matrix is zero, the estimate does not change from time step :math:`k - 1` to :math:`k` 

The estimation error mean can be computed as 

.. math::

    \begin{aligned}
    E(\epsilon_{x, k}) &= E(x - \hat{x}) \\
                       &= E\bigl[x -\hat{x}_{k - 1} - K_{k}(y_{k} - H_{k}\hat{x}_{k - 1})\bigr] \\
                       &= E\bigl[\epsilon_{x, k - 1} - K_{k}\bigl(H_{k}x + v_{k} = H_{k}\hat{x}_{k - 1}\bigr)\bigr] \\
                       &= E\bigl[\epsilon_{x, k - 1} - K_{k}H_{k}(x_{k} - \hat{x}_{k - 1}) - K_{k}v_{k}\bigr] \\
                       &= \bigl(I - K_{k}H_{k}\bigr)E(\epsilon_{x, k - 1}) - K_{k}E(v_{k})
    \end{aligned}

If :math:`E(v_{k}) = 0` and :math:`E(\epsilon_{x, k - 1}) = 0`, then :math:`E(\epsilon_{x, k}) = 0` 

That is; if the measurement noise is zero-mean, and the initial estimate fo :math:`x` is set equal to the exprected value of :math:`x`, then the expected values of :math:`\hat{x}_{k}` will be equal to :math:`x_{K}`

Then, the estimator of :math:`x` is an unbiased estimator 

This property holds regardless of the value of the gain matrix 

.. important::

    On average, the estimate :math:`\hat{x}` will be equal to the true value :math:`x` 

We will be determining the optimal value of the gain matrix

Since the estimator is unbiased, we will minimize the sum of the variances of the estimation errors at time :math:`k` 

The cost function is given as 

.. math::

    \begin{aligned}
    J_{k} &= E\bigl[(x_{1} - \hat{x}_{1})^{2}\bigr] + \cdots + E\bigl[(x_{n} - \hat{x}_{n})^{2}\bigr] \\
          &= E\bigl(\epsilon_{x1, k}^{2} + \cdots + \epsilon_{xn, k}^{2}\bigr) \\
          &= E\bigl(\epsilon_{x, k}^{T}\epsilon_{x, k}\bigr) \\
          &= E\bigl[Tr\bigl(\epsilon_{x, k}\epsilon_{x, k}^{T}\bigr)\bigr] \\
          &= Tr\bigl(P_{k}\bigr)
    \end{aligned}

where :math:`P_{k}` is the estimation-error covariance

The recursive calculation of :math:`P_{k}` is given as

.. math::

    \begin{aligned}
    P_{k} &= E\bigl(\epsilon_{x, k}\epsilon_{x, k}^{T}\bigr) \\
          &= E\bigl[\bigl(\bigl(I - K_{k}H_{k}\bigr)\epsilon_{x, k - 1} - K_{k}v_{k}\bigr)\bigl(\bigl(I - K_{k}H_{k}\bigr)\epsilon_{x, k - 1} - K_{k}v_{k}\bigr)^{T}\bigr] \\
          &= \bigl(I - K_{k}H_{k}\bigr)E\bigl(\epsilon_{x, k - 1}\epsilon_{x, k - 1}^{T}\bigr)\bigl(I - K_{k}H_{k}\bigr)^{T} - K_{k}E\bigl(v_{k}\epsilon_{x, k - 1}^{T}\bigr)\bigl(I - K_{k}H_{k}\bigr)^{T} \\
          &- \bigl(I - K_{k}H_{k}\bigr)E\bigl(\epsilon_{x, k - 1}v_{k}^{T}\bigr)K_{k}^{T} + K_{k}E\bigl(v_{k}v_{k}^{T}\bigr)K_{k}^{T} 
    \end{aligned}

:math:`\epsilon_{x, k - 1}` is dependent of :math:`v_{k}` 

Then 

.. math:: 

    E\bigl(v_{k}\epsilon_{x, k - 1}^{T}\bigr) = E(v_{k})E(\epsilon_{x, k - 1}) = 0

Since both expected values are zero, then 

.. math::

    P_{k} = \bigl(I - K_{k}H_{k}\bigr)P_{k - 1}\bigl(I - K_{k}H_{k}\bigr)^{T} + K_{k}R_{k}K_{k}^{T}

where :math:`R_{k}` is the covariance of :math:`v_{k}`

Assume that :math:`P_{k - 1}` and :math:`R_{k}` are positive definited, then :math:`P_{k}` is positive definited

We will compute the value of :math:`K_{k}` 

The mean of the estimation error is zero, then the estimation error will be zero-mean and consistently zero 

From the cost function, using the property fo partial deriavtive of trace of matrix and chain rule, we obtain 

.. math:: 

    \frac{\partial J_{k}}{\partial K_{k}} = 2\bigl(I - K_{k}H_{k}\bigr)P_{k - 1}\bigl(-H_{k}^{T}\bigr) + 2K_{k}R_{k}

Set this derivative to zero, solve for :math:`K_{k}`, we obtain

.. math::

    \begin{aligned}
    K_{k}R_{k} &= \bigl(I - K_{k}H_{k}\bigr)P_{k - 1}H_{k}^{T} \\
    K_{k}\bigl(R_{k} + H_{k}P_{k - 1}H_{k}^{T} &= P_{k - 1}H_{k}^{T} \\
    K_{k} &= P_{k - 1}H_{k}^{T}\bigl(H_{k}P_{k - 1}H_{k}^{T} + R_{k}\bigr)^{-1}
    \end{aligned}

.. tip::

    **Recursive leat squares estimation**

    Initialize the estimator as follows

        .. math::

            \begin{aligned}
            \hat{x}_{0} &= E(x) \\
            P_{0} &= E\bigl[(x- \hat{x}_{0})(x - \hat{x}_{0})^{T}\bigr]
            \end{aligned}

    - If no knowledge about :math:`x` is available =, then :math:`P_{0} = \infty I`
    - If perfect knowledge about :math:`x` is available, then :math:`P_{0} = 0`

    For :math:`k = 1, 2, \cdots`, perform 

    - Obtain the measurement :math:`y_{k}`, assuming that :math:`y_{k}` is give by 

        .. math::

            y_{k} = H_{k}x + v_{k}
    
      where :math:`v_{k}` is a zero-mean random vector with covariance :math:`R_{k}` 

      Assume that the measurement noise at each time step :math:`k` is independent, that is, :math:`E(v_{i}v_{k}) = R_{k}\delta_{k - 1}` 

      This implies that the measurement noise is white 

    - Update the estimate of :math:`x` and the estimation-error covariance :math:`P` as following

        .. math::

            \begin{aligned}
            K_{k} &= P_{k - 1}H_{k}^{T}\bigl(H_{k}P_{k - 1}H_{k}^{T} + R_{k}\bigr)^{1} \\
            \hat{x}_{k} &= \hat{x}_{k - 1} + K_{k}\bigl(y_{k} - H_{k}\hat{x}_{k - 1}\bigr) \\
            P_{k} &= \bigl(I - K_{k}H_{k}\bigr)P_{k - 1}\bigl(I - K_{k}H_{k}\bigr)^{T} + K_{k}R_{k}K_{k}^{T}
            \end{aligned}
