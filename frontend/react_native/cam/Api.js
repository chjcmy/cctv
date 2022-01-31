import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {useState} from 'react';

export default axios.create({
  baseURL: 'http://10.0.2.2:8000/',
  // headers:
});
