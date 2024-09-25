import FWCore.ParameterSet.Config as cms

def PrimaryVertexFilter(*args, **kwargs):
  mod = cms.EDFilter('PrimaryVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
