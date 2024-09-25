import FWCore.ParameterSet.Config as cms

def HFNoseRawToDigiFake(*args, **kwargs):
  mod = cms.EDProducer('HFNoseRawToDigiFake',
    hfnoseDigis = cms.InputTag('simHFNoseUnsuppressedDigis', 'HFNose'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
