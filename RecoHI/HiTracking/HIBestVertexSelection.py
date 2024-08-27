import FWCore.ParameterSet.Config as cms

def HIBestVertexSelection(**kwargs):
  mod = cms.EDFilter('HIBestVertexSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
