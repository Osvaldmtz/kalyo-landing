export default function middleware(request: Request) {
  const url = new URL(request.url);
  if (url.hostname === 'www.kalyo.io') {
    url.hostname = 'kalyo.io';
    return Response.redirect(url, 308);
  }
}
