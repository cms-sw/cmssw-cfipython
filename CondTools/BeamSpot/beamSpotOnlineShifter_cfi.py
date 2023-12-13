import FWCore.ParameterSet.Config as cms

beamSpotOnlineShifter = cms.EDAnalyzer('BeamSpotOnlineShifter',
  isHLT = cms.bool(True),
  useFullPixel = cms.bool(False),
  xShift = cms.double(0),
  yShift = cms.double(0),
  zShift = cms.double(0),
  IOVStartRun = cms.untracked.uint32(1),
  IOVStartLumi = cms.untracked.uint32(1),
  mightGet = cms.optional.untracked.vstring
)
