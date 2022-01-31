import React, {useContext, useEffect, useState} from 'react';

import {Alert, Button, Text, View} from 'react-native';

const loging = () => {
  // const {signOut} = useContext(AuthContext);

  // eslint-disable-next-line react-hooks/rules-of-hooks
  const [time, setTime] = useState(new Date());

  return (
    <View>
      <Text>log {time.valueOf() + 1}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 2}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 3}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 4}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 5}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 6}</Text>
      <Text>사람 확인</Text>
      <Text>log {time.valueOf() + 7}</Text>
      <Text>사람 확인</Text>
      <Text>log {time.valueOf() + 8}</Text>
      <Text>사람 확인</Text>
      <Text>log {time.valueOf() + 9}</Text>
      <Text>사람 확인</Text>
      <Text>log {time.valueOf() + 10}</Text>
      <Text>사람 확인</Text>
      <Text>log {time.valueOf() + 11}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 12}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 13}</Text>
      <Text>off</Text>
      <Text>log {time.valueOf() + 14}</Text>
    </View>
  );
};

export default loging;
