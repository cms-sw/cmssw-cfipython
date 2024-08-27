import FWCore.ParameterSet.Config as cms

def PATPrimaryVertexCleaner(**kwargs):
  mod = cms.EDFilter('PATPrimaryVertexCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
