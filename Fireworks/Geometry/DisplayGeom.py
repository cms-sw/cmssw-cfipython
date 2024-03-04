import FWCore.ParameterSet.Config as cms

def DisplayGeom(**kwargs):
  mod = cms.EDAnalyzer('DisplayGeom',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
