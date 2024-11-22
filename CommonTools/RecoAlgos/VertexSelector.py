import FWCore.ParameterSet.Config as cms

def VertexSelector(*args, **kwargs):
  mod = cms.EDFilter('VertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
