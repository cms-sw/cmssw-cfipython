import FWCore.ParameterSet.Config as cms

def InputAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('InputAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
