import FWCore.ParameterSet.Config as cms

def PATTracksToPackedCandidates(*args, **kwargs):
  mod = cms.EDProducer('PATTracksToPackedCandidates',
    srcTracks = cms.InputTag('hiConformalPixelTracks'),
    srcPrimaryVertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    srcOfflineBeamSpot = cms.InputTag('offlineBeamSpot'),
    dzSigCut = cms.double(10),
    dxySigCut = cms.double(25),
    dzSigHP = cms.double(7),
    dxySigHP = cms.double(20),
    ptMax = cms.double(1),
    ptMin = cms.double(0.3),
    resetHP = cms.bool(True),
    covarianceVersion = cms.int32(0),
    covarianceSchema = cms.int32(520),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
