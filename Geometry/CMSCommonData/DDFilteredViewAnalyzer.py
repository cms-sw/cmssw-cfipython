import FWCore.ParameterSet.Config as cms

def DDFilteredViewAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DDFilteredViewAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
