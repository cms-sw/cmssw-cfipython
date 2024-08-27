import FWCore.ParameterSet.Config as cms

def TestSpecParAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestSpecParAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
