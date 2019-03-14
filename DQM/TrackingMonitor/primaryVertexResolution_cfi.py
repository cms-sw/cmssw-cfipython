import FWCore.ParameterSet.Config as cms

primaryVertexResolution = cms.EDAnalyzer('PrimaryVertexResolution',
  vertexSrc = cms.untracked.InputTag('trackingDQMgoodOfflinePrimaryVertices'),
  beamspotSrc = cms.untracked.InputTag('offlineBeamSpot'),
  lumiScalersSrc = cms.untracked.InputTag('scalersRawToDigi'),
  rootFolder = cms.untracked.string('OfflinePV/Resolution'),
  transientTrackBuilder = cms.untracked.string('TransientTrackBuilder'),
  maxResol = cms.untracked.double(0.02),
  binsResol = cms.untracked.int32(100),
  maxPull = cms.untracked.double(5),
  binsPull = cms.untracked.int32(100),
  minNtracks = cms.untracked.double(-0.5),
  maxNtracks = cms.untracked.double(119.5),
  binsNtracks = cms.untracked.int32(60),
  minNvertices = cms.untracked.double(-0.5),
  maxNvertices = cms.untracked.double(199.5),
  binsNvertices = cms.untracked.int32(100),
  minPt = cms.untracked.double(1),
  maxPt = cms.untracked.double(1000),
  minLumi = cms.untracked.double(200),
  maxLumi = cms.untracked.double(20000)
)
