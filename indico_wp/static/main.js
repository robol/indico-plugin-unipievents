const WPSYNC_TEXT = 'Wordpress Sync';
const WPSYNC_INPROGRESS = 'Synchronization in progres...';

window.addEventListener('DOMContentLoaded', (event) => {
    console.log("Adding the button for Wordpress Synchronization");
    const marea = document.getElementById('event-management-header-right')

    if (marea) {
	const toolbar = marea.getElementsByClassName('toolbar')[0];
	
	let group = document.createElement('div');	
	group.className += 'group';
	
	let link = document.createElement('a');
	link.className += 'i-button icon-transmission';
	link.innerHTML = WPSYNC_TEXT;
	link.onclick = onWordpressSync;
	link.id = 'wp-sync-button'
	
	group.append(link);
	toolbar.prepend(group);
    }
});

async function onWordpressSync(event) {
    console.log("Performing Wordpress synchronization");

    let el = document.getElementById('wp-sync-button');
    el.innerHTML = WPSYNC_INPROGRESS;
    el.onclick = undefined;

    try {
	const response = await fetch('./wp/update');
	const data = await response.json();
	console.log(data);
    } catch (error) {
	console.error("Failed to request the update");
	return;
    }

    await new Promise((res, rej) => setTimeout(res, 1000));

    el.innerHTML = WPSYNC_TEXT;
    el.onclick = onWordpressSync;
}
