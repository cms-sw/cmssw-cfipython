import FWCore.ParameterSet.Config as cms

def TrivialDeltaRViewMatcher(**kwargs):
  mod = cms.EDProducer('TrivialDeltaRViewMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
