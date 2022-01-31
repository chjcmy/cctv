import React, {useContext, useState} from 'react';

import {Button, TextInput, View} from 'react-native';
import auth from '@react-native-firebase/auth';

import {AuthContext} from '../context';
import AsyncStorage from '@react-native-async-storage/async-storage';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const {signIn} = useContext(AuthContext);

  const SignIn = () => {
    auth()
      .signInWithEmailAndPassword(email, password)
      .then(result => {
        AsyncStorage.setItem('@Email', result.user.email).then(() =>
          signIn(result.user.email),
        );
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <View>
      <TextInput
        placeholder="email"
        onChangeText={result => setEmail(result)}
      />
      <TextInput
        placeholder="password"
        onChangeText={result => setPassword(result)}
        secureTextEntry={true}
        placeholderTextColor="#9a73ef"
      />
      <Button title="Sign In" onPress={() => SignIn()} />
    </View>
  );
};

export default Login;
