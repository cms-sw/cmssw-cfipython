import FWCore.ParameterSet.Config as cms

def BeamSpotProblemMonitor(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotProblemMonitor',
    monitorName = cms.untracked.string('BeamSpotProblemMonitor'),
    DCSStatus = cms.untracked.InputTag('scalersRawToDigi'),
    scalarBSCollection = cms.untracked.InputTag('scalersRawToDigi'),
    pixelTracks = cms.untracked.InputTag('pixelTracks'),
    nCosmicTrk = cms.untracked.int32(10),
    Debug = cms.untracked.bool(False),
    OnlineMode = cms.untracked.bool(True),
    doTest = cms.untracked.bool(False),
    AlarmONThreshold = cms.untracked.int32(10),
    AlarmOFFThreshold = cms.untracked.int32(40),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
