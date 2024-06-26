
const circlesAppleStoreUrl = "https://apps.apple.com/us/app/futo-circles/id6451446720"
const circlesPlayStoreUrl = "https://play.google.com/store/apps/details?id=org.futo.circles&amp;pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1&amp;pli=1"
const circlesDefaultRedirectUrl = "https://circles.futo.org/#download"

// Redirect Circles app deep links if not installed
export function redirect(context) {
    let userAgent = context.request.headers.get("user-agent");

    if (userAgent.includes("iPhone") || userAgent.includes("iPad") || userAgent.includes("Mac OS")) {
        return Response.redirect(circlesAppleStoreUrl);
    }
    else if (userAgent.includes("Android")) {
        return Response.redirect(circlesPlayStoreUrl);
    }

    return Response.redirect(circlesDefaultRedirectUrl);
}
