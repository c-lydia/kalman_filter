Introduction
============

These notes focus on **Kalman filtering** and **optimal state estimation**, covering both the underlying theory and practical methods for estimating the state of dynamic systems from noisy measurements. Kalman filters are widely used in engineering, robotics, navigation, finance, and many other fields where systems change over time and measurements are uncertain.

Scope of These Notes
--------------------

The goal of this document is to provide a structured set of notes that:

- Explains the mathematics and intuition behind **state estimation**.
- Covers **linear system models**, Gaussian noise assumptions, and their role in deriving optimal estimates.
- Derives the **Kalman filter equations** from first principles.
- Explores **extensions and variations**, including the Extended Kalman Filter (EKF), Unscented Kalman Filter (UKF), and Kalman smoothing techniques.
- Provides examples and derivations to build intuition about uncertainty, prediction, and measurement updating.

These notes are intended for readers who already have a basic understanding of probability and random variables. As such, rather than starting from scalar random variables and elementary probability concepts, the discussion begins at **multiple random variables**. This approach is more relevant for practical systems, where different state components—such as position, velocity, or sensor biases—interact and must be estimated simultaneously.

Why Start at Multiple Random Variables
--------------------------------------

Real-world systems are rarely one-dimensional. A robot’s motion, an aircraft’s navigation, or a financial portfolio all involve **interdependent quantities** that cannot be treated independently. Modeling these requires **vector random variables**, which allow us to describe not only the expected value of each component but also the **covariance between components**, capturing how uncertainties are correlated.

By starting here, these notes focus on the mathematical tools and concepts that directly feed into **state-space modeling** and the **Kalman filter**, including:

- **Mean vectors** and **covariance matrices** to represent uncertainty in multiple dimensions.
- **Joint Gaussian distributions** and their properties, which are foundational for deriving Kalman updates.
- **Linear transformations** of random vectors, which appear in system dynamics and measurement models.
- **Conditional distributions**, which are central to updating state estimates when new measurements become available.

Structure and Approach
----------------------

The notes are organized to gradually build from these foundational concepts toward a full understanding of the Kalman filter:

1. **Multiple Random Variables** – vector notation, covariance, joint Gaussian distributions, and linear transformations.
2. **State-Space Models** – linear system representation, process and measurement models, and noise characterization.
3. **Kalman Filter** – derivation of prediction and update equations, intuition, and properties.
4. **Extensions** – nonlinear systems (EKF, UKF), smoothing, and other variations.
5. **Applications and Examples** – practical scenarios, implementation tips, and illustrative computations.

By framing the notes in this way, readers can focus on the **core ideas of state estimation** without being slowed by material they already know, while still maintaining a complete and coherent understanding of Kalman filtering.

Why These Notes Matter
----------------------

Kalman filtering is not just a theoretical exercise—it is a **powerful tool** for making sense of uncertain, dynamic systems. Understanding how to model uncertainty, combine predictions with measurements, and optimize estimates is a skill that applies across engineering, data science, and decision-making contexts. These notes are designed to provide both the **theoretical foundation** and **practical insight** to develop that skill.
