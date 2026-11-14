export default function middleware(request: Request) {
  const url = new URL(request.url);
  if (url.hostname === 'www.kalyo.io') {
    url.hostname = 'kalyo.io';
    return Response.redirect(url.toString(), 308);
  }
  // Pass through so Vercel continues to static files / vercel.json redirects.
  return new Response(null, {
    headers: { 'x-middleware-next': '1' },
  });
}
