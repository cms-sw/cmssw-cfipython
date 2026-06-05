import FWCore.ParameterSet.Config as cms

def PATSingleVertexSelector(*args, **kwargs):
  mod = cms.EDFilter('PATSingleVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
