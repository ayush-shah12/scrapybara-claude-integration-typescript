import {ScrapyPilot} from './ScrapyPilot';

async function runScrapyPilot() {
    try {
        const pilot = new ScrapyPilot("scrapybara key", "anthropic key");

        const instanceId = await pilot.startInstance('small', 0.05);
        console.log(`Instance started with ID: ${instanceId}`);

        const userPrompt = "Do some very brief research on the impact of tarrifs.";
        await pilot.run(userPrompt);
    } catch (error) {
        console.error('Error running ScrapyPilot:', error);
    }
}

runScrapyPilot();
