import FWCore.ParameterSet.Config as cms

def MatcherByPulls(**kwargs):
  mod = cms.EDProducer('MatcherByPulls',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
