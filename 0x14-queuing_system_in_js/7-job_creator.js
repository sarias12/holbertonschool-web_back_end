import kue from 'kue';
const queue = kue.createQueue();
const jobs = [{
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
},
	      {
		  phoneNumber: '4153518781',
		  message: 'This is the code 4562 to verify your account'
	      },
	      {
		  phoneNumber: '4153518743',
		  message: 'This is the code 4321 to verify your account'
	      },
	      {
		  phoneNumber: '4153538781',
		  message: 'This is the code 4562 to verify your account'
	      },
	      {
		  phoneNumber: '4153118782',
		  message: 'This is the code 4321 to verify your account'
	      },
	      {
		  phoneNumber: '4153718781',
		  message: 'This is the code 4562 to verify your account'
	      },
	      {
		  phoneNumber: '4159518782',
		  message: 'This is the code 4321 to verify your account'
	      },
	      {
		  phoneNumber: '4158718781',
		  message: 'This is the code 4562 to verify your account'
	      },
	      {
		  phoneNumber: '4153818782',
		  message: 'This is the code 4321 to verify your account'
	      },
	      {
		  phoneNumber: '4154318781',
		  message: 'This is the code 4562 to verify your account'
	      },
	      {
		  phoneNumber: '4151218782',
		  message: 'This is the code 4321 to verify your account'
	      }
	     ];

function createJob (phoneNumber, message) {
    const jobData = {
	phoneNumber: phoneNumber,
	message: message
    }

    const job = queue.create('push_notification_code_2', jobData);

    job.save();

    job.on('enqueue', function(id, type){
	console.log(`Notification job created: ${job.id}`);
    }).on('complete', function(result){
	console.log(`Notification job #${job.id} completed`);
    }).on('failed', function(errorMessage){
	console.log(`Notification job #${job.id} failed: ${errorMessage}`);
    }).on('progress', function(progress, data){
	console.log(`Notification job #${job.id} ${progress}% complete`);
    });
}

jobs.forEach((element) => createJob(element.phoneNumber, element.message) )
