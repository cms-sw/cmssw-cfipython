import FWCore.ParameterSet.Config as cms

def CSCOverlapsBeamSplashCut(**kwargs):
  mod = cms.EDFilter('CSCOverlapsBeamSplashCut',
    src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
    maxSegments = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
