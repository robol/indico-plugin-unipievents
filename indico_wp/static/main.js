const WPSYNC_CONFIG = {
    TEXT: 'Wordpress Sync',
    INPROGRESS_TEXT: 'Synchronization in progres...'
}

function getIndicoToolbar() {
    const marea = document.getElementById('event-management-header-right');
    if (marea) {
	const toolbar = marea.getElementsByClassName('toolbar')[0];
	return toolbar;
    }
}

function createWordpressButton() {
    let group = document.createElement('div');	
    group.className += 'group';
	
    let link = document.createElement('a');
    link.className += 'i-button icon-transmission';
    link.innerHTML = WPSYNC_CONFIG.TEXT;
    link.onclick = onWordpressSync;
    link.id = 'wp-sync-button'
	
    group.append(link);

    return group;
}

function injectWordpressSyncButton() {
    const toolbar = getIndicoToolbar();
    
    if (toolbar) {
	toolbar.prepend(createWordpressButton());
    }
}

function startWordpressSync() {
    let el = document.getElementById('wp-sync-button');
    el.innerHTML = WPSYNC_CONFIG.INPROGRESS_TEXT;
    el.onclick = undefined;
}

function endWordpressSync() {
    let el = document.getElementById('wp-sync-button');
    el.innerHTML = WPSYNC_CONFIG.TEXT;
    el.onclick = onWordpressSync;
}

async function onWordpressSync(event) {
    startWordpressSync();
    
    try {
	const response = await fetch('./wp/update');
	const data = await response.json();
    } catch (error) {
	console.error("Failed to request the update");
	return;
    }

    endWordpressSync();
}


window.addEventListener('DOMContentLoaded', injectWordpressSyncButton);

