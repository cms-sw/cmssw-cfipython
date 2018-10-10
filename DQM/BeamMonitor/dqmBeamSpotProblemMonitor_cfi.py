import FWCore.ParameterSet.Config as cms

dqmBeamSpotProblemMonitor = cms.EDProducer('BeamSpotProblemMonitor',
  monitorName = cms.untracked.string('BeamSpotProblemMonitor'),
  DCSStatus = cms.untracked.InputTag('scalersRawToDigi'),
  scalarBSCollection = cms.untracked.InputTag('scalersRawToDigi'),
  pixelTracks = cms.untracked.InputTag('pixelTracks'),
  nCosmicTrk = cms.untracked.int32(10),
  Debug = cms.untracked.bool(False),
  OnlineMode = cms.untracked.bool(True),
  doTest = cms.untracked.bool(False),
  AlarmONThreshold = cms.untracked.int32(10),
  AlarmOFFThreshold = cms.untracked.int32(40)
)
