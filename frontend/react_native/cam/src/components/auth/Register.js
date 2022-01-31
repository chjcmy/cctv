import React, {useContext, useState} from 'react';

import {View, TextInput, Button} from 'react-native';
import auth from '@react-native-firebase/auth';
import {AuthContext} from '../context';
import Api from '../../../Api';
import AsyncStorage from '@react-native-async-storage/async-storage';

const Register = props => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [ip, setIp] = useState('');
  const [password, setPassword] = useState('');

  const {signUp} = useContext(AuthContext);

  const SignUp = () => {
    auth()
      .createUserWithEmailAndPassword(email, password, name)
      .then(async result => {
        console.log(result);
        AsyncStorage.setItem('@Email', result.user.email).then(() => signUp());
      })
      .catch(error => {
        if (error.code === 'auth/email-already-in-use') {
          console.log('That email address is already in use!');
        }
        if (error.code === 'auth/invalid-email') {
          console.log('That email address is invalid!');
        }
        console.error(error);
      });
  };

  return (
    <View>
      <TextInput placeholder="name" onChangeText={result => setName(result)} />
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
      <TextInput placeholder="Ip" onChangeText={result => setIp(result)} />
      <Button
        title="SignUp"
        onPress={async () => {
          await Api.post('user/makeId', {Email: email, Ip: ip, name: name})
            .then(response => console.log(response))
            .catch(error => console.log(error));
          SignUp();
        }}
      />
    </View>
  );
};

export default Register;
