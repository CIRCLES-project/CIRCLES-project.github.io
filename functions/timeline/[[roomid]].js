import { redirect } from "../_middleware.js";

export function onRequest(context) {
    return redirect(context);
}
