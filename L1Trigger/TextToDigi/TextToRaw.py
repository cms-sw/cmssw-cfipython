import FWCore.ParameterSet.Config as cms

def TextToRaw(**kwargs):
  mod = cms.EDProducer('TextToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
