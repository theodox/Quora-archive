# Computer Graphics: 

	author: Steve Theodore
	written: 2017-12-02
	views: 784
	upvotes: 3
	quora url: /Computer-Graphics-What-are-Gimbal-rotations-and-how-are-they-different-from-local-rotations/answer/Steve-Theodore
	author url: /profile/Steve-Theodore


Gimbal rotations derive their name from the old fashioned gimbal mouning, for example those used by gyroscopes.

![](https://qph.fs.quoracdn.net/main-qimg-213c26f724885bc9748dce8a6f775240)

It’s often convenient for artists to specify angular movement in terms of a series of rotations around the X, Y and Z axes; “45 degress in X”, “20 degrees in Y” and so on. We usually refer to this system as [Euler angles](https://en.wikipedia.org/wiki/Euler_angles).

Eulers make intuitive sense for a lot of users, and allows you to decouple different kinds of movements (pitch and yaw, for example, are easy to split out). But, those Euler rotations aren’t really independent of each other — if you rotate one of those axes 90 degrees, it becomes a different axis! So you can easily get surprising results. The worst is known as ‘gimbal lock’, which happens when the rotation of one axis so changes the meaning of the rotation of another that the rotation appears to be undone.



Nowadays many animation systems use a different mathematical approach, known as [quaternions](https://www.3dgep.com/understanding-quaternions/) to represent angles internally. Quaternions aren’t subject to gimbal lock, although the numbers involved are less intuitive to most people.

Eulers and quaternions can both be applied in any coordinate system — ‘local’ rotations just mean you’re rotating in the object’s own frame of reference rather than some other one. Gimbal lock and it’s related problems can happen in any space — they have to do with how the rotations are applied, not what the final result looks like.

