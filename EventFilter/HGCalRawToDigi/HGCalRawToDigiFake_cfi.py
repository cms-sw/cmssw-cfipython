import FWCore.ParameterSet.Config as cms

HGCalRawToDigiFake = cms.EDProducer('HGCalRawToDigiFake',
  eeDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
  fhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEfront'),
  bhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEback')
)
