import FWCore.ParameterSet.Config as cms

def DQMSourcePi0(**kwargs):
  mod = cms.EDProducer('DQMSourcePi0',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
