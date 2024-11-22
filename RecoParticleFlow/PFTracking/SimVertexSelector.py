import FWCore.ParameterSet.Config as cms

def SimVertexSelector(*args, **kwargs):
  mod = cms.EDFilter('SimVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
