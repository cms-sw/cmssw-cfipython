import FWCore.ParameterSet.Config as cms

def DDFilteredViewAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DDFilteredViewAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
