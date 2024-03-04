import FWCore.ParameterSet.Config as cms

def ValidateGeometry(**kwargs):
  mod = cms.EDAnalyzer('ValidateGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
