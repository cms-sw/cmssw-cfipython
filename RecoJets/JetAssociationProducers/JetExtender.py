import FWCore.ParameterSet.Config as cms

def JetExtender(**kwargs):
  mod = cms.EDProducer('JetExtender',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
