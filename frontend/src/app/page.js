import Link from "next/link";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-100">
      <h1 className="text-4xl font-bold text-blue-600 mb-6">Finance Tracker</h1>

      <div className="space-x-4">
        <Link
  href="/register"
  className="px-4 py-2 bg-blue-600 text-white rounded-md"
>
  Register
</Link>

<Link
  href="/login"
  className="px-4 py-2 bg-gray-200 text-gray-800 rounded-md"
>
  Login
</Link>
      </div>
    </div>
  );
}
