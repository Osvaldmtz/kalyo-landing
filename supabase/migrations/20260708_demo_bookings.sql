-- demo_bookings table for kalyo.io/demo scheduling
CREATE TABLE IF NOT EXISTS public.demo_bookings (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  email text NOT NULL,
  whatsapp text NOT NULL,
  country text NOT NULL,
  interest text,
  scheduled_at timestamptz NOT NULL,
  meet_link text NOT NULL DEFAULT 'https://meet.google.com/pgd-dxmb-sfk',
  reminder_24h_sent boolean NOT NULL DEFAULT false,
  reminder_1h_sent boolean NOT NULL DEFAULT false,
  status text NOT NULL DEFAULT 'confirmed' CHECK (status IN ('pending', 'confirmed', 'cancelled')),
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS demo_bookings_scheduled_at_unique
  ON public.demo_bookings (scheduled_at)
  WHERE status IN ('pending', 'confirmed');

ALTER TABLE public.demo_bookings ENABLE ROW LEVEL SECURITY;
