import FWCore.ParameterSet.Config as cms

def HGCalRawToDigiFake(**kwargs):
  mod = cms.EDProducer('HGCalRawToDigiFake',
    eeDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    fhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEfront'),
    bhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEback'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
