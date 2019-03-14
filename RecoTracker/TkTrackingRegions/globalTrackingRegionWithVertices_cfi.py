import FWCore.ParameterSet.Config as cms

globalTrackingRegionWithVertices = cms.EDProducer('GlobalTrackingRegionWithVerticesEDProducer',
  RegionPSet = cms.PSet(
    precise = cms.bool(True),
    useMultipleScattering = cms.bool(False),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    useFixedError = cms.bool(True),
    originRadius = cms.double(0.2),
    sigmaZVertex = cms.double(3),
    fixedError = cms.double(0.2),
    VertexCollection = cms.InputTag('firstStepPrimaryVertices'),
    ptMin = cms.double(0.9),
    useFoundVertices = cms.bool(True),
    useFakeVertices = cms.bool(False),
    maxNVertices = cms.int32(-1),
    nSigmaZ = cms.double(4)
  )
)
