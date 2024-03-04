import FWCore.ParameterSet.Config as cms

def MCMatcher(**kwargs):
  mod = cms.EDProducer('MCMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
