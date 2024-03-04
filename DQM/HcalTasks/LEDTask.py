import FWCore.ParameterSet.Config as cms

def LEDTask(**kwargs):
  mod = cms.EDProducer('LEDTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
