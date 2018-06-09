
echo "stopping salusmind..."
sudo systemctl stop salusmind

echo "starting salusmind..."
sudo systemctl start salusmind
sudo systemctl enable salusmind

echo "restarting nginx..."
sudo systemctl restart nginx

echo "done!"
