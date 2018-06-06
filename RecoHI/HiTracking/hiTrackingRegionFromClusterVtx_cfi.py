import FWCore.ParameterSet.Config as cms

hiTrackingRegionFromClusterVtx = cms.EDProducer('HITrackingRegionForPrimaryVtxEDProducer',
  RegionPSet = cms.PSet(
    ptMin = cms.double(0.7),
    doVariablePtMin = cms.bool(True),
    originRadius = cms.double(0.2),
    nSigmaZ = cms.double(3),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    precise = cms.bool(True),
    useMultipleScattering = cms.bool(False),
    useFakeVertices = cms.bool(False),
    siPixelRecHits = cms.InputTag('siPixelRecHits'),
    directionXCoord = cms.double(1),
    directionYCoord = cms.double(1),
    directionZCoord = cms.double(0),
    useFoundVertices = cms.bool(True),
    VertexCollection = cms.InputTag('hiPixelClusterVertex'),
    useFixedError = cms.bool(True),
    fixedError = cms.double(3),
    sigmaZVertex = cms.double(3)
  )
)
