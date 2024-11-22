import FWCore.ParameterSet.Config as cms

def PrimaryVertexObjectFilter(*args, **kwargs):
  mod = cms.EDFilter('PrimaryVertexObjectFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
