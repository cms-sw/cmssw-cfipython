import FWCore.ParameterSet.Config as cms

def MuBxSelector(**kwargs):
  mod = cms.EDProducer('MuBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
