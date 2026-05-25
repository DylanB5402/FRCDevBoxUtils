import 'dotenv/config';


import { Daytona, DaytonaConfig } from '@daytona/sdk'

const config: DaytonaConfig = {
  apiKey: process.env.DAYTONA_API_KEY,
  target: 'us',
}


async function main() {
  
    const daytona = new Daytona(config);
    const sandbox = await daytona.create({
        snapshot: "frc-devbox-large",
    });
    console.log(`Sandbox created with ID: ${sandbox.id}`);
    await sandbox.git.clone(
        "https://github.com/DylanB5402/FRCDevBoxUtils.git",
        "workspace/FRCDevBoxUtils"
    )
    const sshAccess = await sandbox.createSshAccess(240)
    console.log(`ssh in with ssh -A ${sshAccess.token}@ssh.app.daytona.io`)

    const signedUrl = await sandbox.getSignedPreviewUrl(5810, 3600);

    console.log("NT4:")
    console.log(`URL: ${signedUrl.url}`);  // Token is embedded in the URL
    console.log(`Token: ${signedUrl.token}`);  // Can be used to revoke access

    const signedUrl2 = await sandbox.getSignedPreviewUrl(5808, 3600);

    console.log("AdvantageScope:")
    console.log(`URL: ${signedUrl2.url}`);  // Token is embedded in the URL
    console.log(`Token: ${signedUrl2.token}`);  // Can be used to revoke access

}
main()