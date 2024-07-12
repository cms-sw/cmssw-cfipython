import FWCore.ParameterSet.Config as cms

def MuTagJetBxSelector(**kwargs):
  mod = cms.EDProducer('MuTagJetBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
