@echo off
title Multi-CMD Launcher

:: Start the server in a new command prompt window
start "Server" cmd /k python src/server.py

:: Add a small delay to allow the server to initialize (optional)
timeout /t 2 >nul

:: Start the first client in a new command prompt window
start "Client 1" cmd /k python src/client.py

:: Start the second client in a new command prompt window
start "Client 2" cmd /k python src/client.py