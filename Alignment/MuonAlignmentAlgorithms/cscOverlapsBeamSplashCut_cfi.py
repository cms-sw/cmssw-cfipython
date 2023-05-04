import FWCore.ParameterSet.Config as cms

cscOverlapsBeamSplashCut = cms.EDFilter('CSCOverlapsBeamSplashCut',
  src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
  maxSegments = cms.int32(4),
  mightGet = cms.optional.untracked.vstring
)
