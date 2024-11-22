import FWCore.ParameterSet.Config as cms

def HIBestVertexSelection(*args, **kwargs):
  mod = cms.EDFilter('HIBestVertexSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
