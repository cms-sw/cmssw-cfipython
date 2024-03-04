import FWCore.ParameterSet.Config as cms

def CandOneToOneDeltaRMatcher(**kwargs):
  mod = cms.EDProducer('CandOneToOneDeltaRMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
