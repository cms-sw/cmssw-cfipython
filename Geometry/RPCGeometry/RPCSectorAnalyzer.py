import FWCore.ParameterSet.Config as cms

def RPCSectorAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCSectorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
