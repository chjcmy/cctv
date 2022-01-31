import React, {useEffect, useState} from 'react';

import {Button, Text, TextInput, View, StyleSheet} from 'react-native';
import Api from '../../../Api';

const Info = ({navigation}) => {
  const [person, setPerson] = useState({name: '', email: '', Ip: '', date: ''});

  useEffect(() => {
    const information = async () => {
      await Api.get('user/infoDetail');
    };
    information().then(result => console.log(result));
  }, []);

  return (
    <View>
      <Text style={styles.baseText}>naruto@Kakashi.Itachi</Text>
      <TextInput
        placeholder="ip"
        placeholderTextColor="#9a73ef"
        value="192.168.52.52"
      />
      <TextInput
        placeholder="이름"
        placeholderTextColor="#9a73ef"
        value="최성현"
      />
      <TextInput
        placeholder="만들어진 날짜"
        placeholderTextColor="#9a73ef"
        value="Fri May 28 2021 19:47:49"
      />
      <Button title="edit" onPress={() => navigation.navigate('Home')} />
    </View>
  );
};

const styles = StyleSheet.create({
  baseText: {
    fontFamily: 'Cochin',
  },
  titleText: {
    fontSize: 20,
    fontWeight: 'bold',
  },
});

export default Info;
