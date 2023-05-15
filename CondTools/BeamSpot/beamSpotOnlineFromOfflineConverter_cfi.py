import FWCore.ParameterSet.Config as cms

beamSpotOnlineFromOfflineConverter = cms.EDAnalyzer('BeamSpotOnlineFromOfflineConverter',
  isHLT = cms.bool(True),
  IOVStartRun = cms.untracked.uint32(1),
  IOVStartLumi = cms.untracked.uint32(1),
  lastAnalyzedLumi = cms.double(1000),
  lastAnalyzedRun = cms.double(1),
  lastAnalyzedFill = cms.double(-999),
  numTracks = cms.int32(0),
  numPVs = cms.int32(0),
  numUsedEvents = cms.int32(0),
  numMaxPVs = cms.int32(0),
  meanPVs = cms.double(0),
  meanPVError = cms.double(0),
  rmsPVs = cms.double(0),
  rmsPVError = cms.double(0),
  startTime = cms.string(''),
  endTime = cms.string(''),
  lumiRange = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
