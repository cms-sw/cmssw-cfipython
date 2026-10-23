import FWCore.ParameterSet.Config as cms

def HGCalRawToDigiFake(*args, **kwargs):
  mod = cms.EDProducer('HGCalRawToDigiFake',
    eeDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    fhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEfront'),
    bhDigis = cms.InputTag('simHGCalUnsuppressedDigis', 'HEback'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
