import FWCore.ParameterSet.Config as cms

def JetBxSelector(**kwargs):
  mod = cms.EDProducer('JetBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
