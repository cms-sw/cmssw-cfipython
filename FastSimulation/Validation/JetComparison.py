import FWCore.ParameterSet.Config as cms

def JetComparison(**kwargs):
  mod = cms.EDAnalyzer('JetComparison',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
