import React, {useCallback, useContext} from 'react';

import {Button, View, StyleSheet, Alert} from 'react-native';
import {AuthContext} from '../context';
import MQTT from 'sp-react-native-mqtt';
import WebView from 'react-native-webview';
import messaging from '@react-native-firebase/messaging';

const Streaming = () => {
  const {signOut} = useContext(AuthContext);

  MQTT.createClient({
    uri: 'mqtt://',
    clientId: 'ubuntu',
  })
    .then(function (client) {
      client.on('closed', function () {
        console.log('mqtt.event.closed');
      });

      client.on('error', function (msg) {
        console.log('mqtt.event.error', msg);
      });

      client.on('message', function (msg) {
        console.log('mqtt.event.message', msg);
        if (msg) {
          const hace = JSON.parse(msg.data);
          console.log(hace.success);
        }
      });

      client.on('connect', function () {
        console.log('connected');
        client.publish('common', 'common', 1, false);
      });

      client.connect();
    })
    .catch(function (err) {
      console.log(err);
    });

  const getFcmToken = useCallback(async () => {
    const fcmToken = await messaging().getToken();
    await Alert.alert(fcmToken);
    console.log(fcmToken);
  }, []);

  return (
    // <WebView
    //   source={{
    //     uri: 'http://',
    //   }}
    // />
    <Button title="get Token!!" onPress={getFcmToken} />
  );
};

export default Streaming;
