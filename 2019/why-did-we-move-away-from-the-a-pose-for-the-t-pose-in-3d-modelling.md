# Why did we move away from the A pose for the T pose in 3D modelling?

	author: Steve Theodore
	written: 2019-12-26
	views: 384
	upvotes: 4
	quora url: /Why-did-we-move-away-from-the-A-pose-for-the-T-pose-in-3D-modelling/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Generally, modelers prefer A-pose because it has less extreme deformations. However animators and riggers tend to prefer T-pose because the math is easier for many of the things you might want to do to a skeleton.

It’s really a false dilemma — a robust rig should be able to handle an arbitrary “zero” pose that is not actually at EulerAngles (0,0,0). The “zero” does not, in fact, have to be rigidly aligned with line of the clavicles. Unfortunately a lot of folks are so psychologically dependent on just typing zeros into the controls as a way of getting out of messy pose that they take the awkward T-Pose as a given, even though it makes life harder for modelers and tends to produce worse visuals.

It’s less of an issue in film and vfx production where there are often many different layers of artists between the animator and the modeller — muscle systems and custom skin deformers tend to render the A-pose vs T-Pose debate less contentious.

