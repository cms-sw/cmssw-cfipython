import FWCore.ParameterSet.Config as cms

def CSCOverlapsBeamSplashCut(*args, **kwargs):
  mod = cms.EDFilter('CSCOverlapsBeamSplashCut',
    src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
    maxSegments = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
