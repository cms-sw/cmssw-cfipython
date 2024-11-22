import FWCore.ParameterSet.Config as cms

def VertexRefSelector(*args, **kwargs):
  mod = cms.EDFilter('VertexRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
