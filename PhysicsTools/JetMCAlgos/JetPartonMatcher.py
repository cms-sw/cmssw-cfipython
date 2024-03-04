import FWCore.ParameterSet.Config as cms

def JetPartonMatcher(**kwargs):
  mod = cms.EDProducer('JetPartonMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
