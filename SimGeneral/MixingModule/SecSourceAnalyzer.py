import FWCore.ParameterSet.Config as cms

def SecSourceAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SecSourceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
