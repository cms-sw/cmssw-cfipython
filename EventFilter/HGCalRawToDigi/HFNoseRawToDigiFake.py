import FWCore.ParameterSet.Config as cms

def HFNoseRawToDigiFake(**kwargs):
  mod = cms.EDProducer('HFNoseRawToDigiFake',
    hfnoseDigis = cms.InputTag('simHFNoseUnsuppressedDigis', 'HFNose'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
