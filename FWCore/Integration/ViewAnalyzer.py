import FWCore.ParameterSet.Config as cms

def ViewAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ViewAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
