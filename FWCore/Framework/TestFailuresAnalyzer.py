import FWCore.ParameterSet.Config as cms

def TestFailuresAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestFailuresAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
