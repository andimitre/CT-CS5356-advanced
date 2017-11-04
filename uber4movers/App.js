import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity
} from 'react-native';

export default class App extends Component<{}> {
  constructor() {
    super()
    this.state = {
      dummy: '(201) 445-3334',
      phoneNumber: ''
    }
    this.changeNumber = this.changeNumber.bind(this)
  }

  changeNumber(phoneNumber) {
    this.setState({phoneNumber})
  }

  render() {
    const { phoneNumber, dummy } = this.state
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}> Enter your phone number </Text>
        <TextInput style={styles.input} onChangeText={(value) => this.changeNumber({value})} placeholder={this.state.dummy} />
        <TouchableOpacity
            style={styles.submitButton} onPress={console.log(this.state.phoneNumber.value)}>
            <Text style={styles.submitButtonText}> Submit </Text>
         </TouchableOpacity>
         <TouchableOpacity
             style={styles.submitButton} onPress={console.log("mmm")}>
             <Text style={styles.submitButtonText}> Submit </Text>
          </TouchableOpacity>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
  input: {
    justifyContent: 'center',
    borderColor: 'black',
    color: 'black',
    textAlign: 'center',
  },
  submitButton: {
    backgroundColor: '#3498db',
    padding: 10,
    borderRadius: 10,
    margin: 15,
    height: 40
  },
});
