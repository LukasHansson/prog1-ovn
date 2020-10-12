print('Välj mellan:\n\tTar på mig kläder\n\tFörsover mig')
vakna = input('Vad gör du när du alarmet ringer? ')

if vakna == 'Försover mig':
  print('Otur')


elif vakna == 'Tar på mig kläder':
  print('Stiligt!')
  'Tar på mig kläder' == input('Vad gör du sen? ')
  'Vad gör du sen?'== input('Efter det då? ')
  print('Fräscht')
  frukost = input('Äter du frukost? ')
  if frukost =='Nej':
    print('Okej')
  elif frukost =='Ja':
    print('Vad äter du till frukost? ')
    'Vad äter du till frukost?' == input('')
    print('Låter gott!')