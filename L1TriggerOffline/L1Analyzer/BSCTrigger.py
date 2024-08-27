import FWCore.ParameterSet.Config as cms

def BSCTrigger(**kwargs):
  mod = cms.EDProducer('BSCTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
