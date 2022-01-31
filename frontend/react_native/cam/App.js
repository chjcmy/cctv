/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {useEffect, useMemo, useState} from 'react';
import type {Node} from 'react';
import {Alert, StyleSheet, LogBox} from 'react-native';
import {GoogleSignin} from '@react-native-google-signin/google-signin';
import {createStackNavigator} from '@react-navigation/stack';
import {NavigationContainer} from '@react-navigation/native';
import messaging from '@react-native-firebase/messaging';

import LandingScreen from './src/components/auth/Landing';
import RegisterScreen from './src/components/auth/Register';
import LoginScreen from './src/components/auth/Login';
import notiScreen from './src/components/winning/winning';

import {AuthContext} from './src/components/context';
import {NotiContext} from './src/components/context';
import HomeScreen from './src/screens/HomeScreen';
import AsyncStorage from '@react-native-async-storage/async-storage';

GoogleSignin.configure({
  webClientId:
    '596926950146-p43o8fhgpqu7g3n78c871iq8kdvua417.apps.googleusercontent.com',
});

const App: () => Node = () => {
  const [userToken, setUserToken] = useState(false);
  const [notification, setNotification] = useState(true);
  LogBox.ignoreLogs(['Reanimated 2']);

  useEffect(() => {
    messaging().onMessage(async remoteMessage => {
      Alert.alert('A new FCM message arrived!', JSON.stringify(remoteMessage));
    });

    messaging().onNotificationOpenedApp(remoteMessage => {
      console.log('onNotificationOpenedApp: ', JSON.stringify(remoteMessage));
    });

    messaging()
      .getInitialNotification()
      .then(remoteMessage => {
        if (remoteMessage) {
          setNotification(false);
          console.log(JSON.stringify(remoteMessage.notification));
        }
      });
  }, []);
  const notiContext = useMemo(() => ({
    notioff: value => {
      setNotification(true);
    },
  }));
  const authContext = useMemo(() => ({
    signIn: value => {
      setUserToken(value);
    },
    signOut: value => {
      AsyncStorage.removeItem('@Email');
      setUserToken(null);
    },
    signUp: value => {
      setUserToken(value);
    },
  }));

  const Stack = createStackNavigator();

  return (
    <NotiContext.Provider value={notiContext}>
      <AuthContext.Provider value={authContext}>
        <NavigationContainer>
          {notification === false ? (
            <Stack.Navigator>
              <Stack.Screen
                name="noti"
                component={notiScreen}
                options={{headerShown: false}}
              />
            </Stack.Navigator>
          ) : userToken === null ? (
            <Stack.Navigator>
              <Stack.Screen
                name="Landing"
                component={LandingScreen}
                options={{headerShown: false}}
              />
              <Stack.Screen name="Register" component={RegisterScreen} />
              <Stack.Screen name="Login" component={LoginScreen} />
            </Stack.Navigator>
          ) : (
            <HomeScreen />
          )}
        </NavigationContainer>
      </AuthContext.Provider>
    </NotiContext.Provider>
  );
};

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});

export default App;
