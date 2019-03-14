import FWCore.ParameterSet.Config as cms

globalTrackingRegionFromBeamSpot = cms.EDProducer('GlobalTrackingRegionFromBeamSpotEDProducer',
  RegionPSet = cms.PSet(
    precise = cms.bool(True),
    useMultipleScattering = cms.bool(False),
    nSigmaZ = cms.double(4),
    originHalfLength = cms.double(0),
    originRadius = cms.double(0.2),
    ptMin = cms.double(0.9),
    beamSpot = cms.InputTag('offlineBeamSpot')
  )
)
