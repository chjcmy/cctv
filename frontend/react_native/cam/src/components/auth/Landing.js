import React from 'react';

import {Button, View} from 'react-native';

const Landing = ({navigation}) => {
  return (
    <View style={{flex: 1, justifyContent: 'center'}}>
      <Button title="Login" onPress={() => navigation.navigate('Login')} />
      <Button
        title="Register"
        onPress={() => navigation.navigate('Register')}
      />
    </View>
  );
};

export default Landing;
