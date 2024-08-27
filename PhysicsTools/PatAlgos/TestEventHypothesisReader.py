import FWCore.ParameterSet.Config as cms

def TestEventHypothesisReader(**kwargs):
  mod = cms.EDAnalyzer('TestEventHypothesisReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
