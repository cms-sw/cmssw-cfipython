import FWCore.ParameterSet.Config as cms

def PFDisplacedVertexSelector(*args, **kwargs):
  mod = cms.EDFilter('PFDisplacedVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
