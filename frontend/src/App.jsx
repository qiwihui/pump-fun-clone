import logo from "./logo.svg";
import "./App.css";
import Main from "./components/Main";
import { http, createConfig } from "wagmi";
import { sepolia } from "wagmi/chains";
import { WagmiProvider } from "wagmi";
import { ConnectKitProvider, getDefaultConfig } from "connectkit";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { injected } from "wagmi/connectors";

const projectId = "4265189f60ad0e1a606df6152e4e2ca0";

const config = createConfig(
  getDefaultConfig({
    // Your dApps chains
    chains: [sepolia],
    connectors: [injected()],
    transports: {
      // RPC URL for each chain
      [sepolia.id]: http("https://ethereum-sepolia-rpc.publicnode.com"),
    },
    // Required API Keys
    walletConnectProjectId: projectId,
    // Required App Info
    appName: "Token App Demo",
    // Optional App Info
    appDescription: "Token App Demo",
    appUrl: "https://family.co", // your app's url
    appIcon: "https://family.co/logo.png", // your app's icon, no bigger than 1024x1024px (max. 1MB)
  })
);

const queryClient = new QueryClient();

function App() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <ConnectKitProvider>
          <div className="App">
            <Main />
          </div>
        </ConnectKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  );
}

export default App;