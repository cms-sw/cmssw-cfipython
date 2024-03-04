import FWCore.ParameterSet.Config as cms

def SCSimpleAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SCSimpleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
