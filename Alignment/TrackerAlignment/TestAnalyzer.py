import FWCore.ParameterSet.Config as cms

def TestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
