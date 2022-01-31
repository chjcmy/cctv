import React from 'react';
import {createDrawerNavigator} from '@react-navigation/drawer';
import Info from '../../components/info/info';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Streaming from '../../components/barmenu/Streaming';
import loging from '../../components/barmenu/loging';

const HomeTab = () => {
  const Tab = createBottomTabNavigator();
  return (
    <Tab.Navigator>
      <Tab.Screen name="동영상" component={Streaming} />
      <Tab.Screen name="로그" component={loging} />
    </Tab.Navigator>
  );
};

const HomeScreen = () => {
  const Drawer = createDrawerNavigator();
  return (
    <Drawer.Navigator initialRouteName="Home">
      <Drawer.Screen name="Home" component={HomeTab} />
      <Drawer.Screen name="Info" component={Info} />
    </Drawer.Navigator>
  );
};

export default HomeScreen;
