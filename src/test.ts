import {ScrapyPilot} from './ScrapyPilot'

async function runScrapyPilot() {
    try {
        const pilot = new ScrapyPilot();

        const instanceId = await pilot.startInstance('small', 0.05);
        console.log(`Instance started with ID: ${instanceId}`);

        const userPrompt = "Give me Djisktra's shortest path algorithm in Python. Include detailed comments. Download the file onto my local machine.";
        await pilot.run(userPrompt);
    } catch (error) {
        console.error('Error running ScrapyPilot:', error);
    }
}

runScrapyPilot();
