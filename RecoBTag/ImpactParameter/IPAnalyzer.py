import FWCore.ParameterSet.Config as cms

def IPAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('IPAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
