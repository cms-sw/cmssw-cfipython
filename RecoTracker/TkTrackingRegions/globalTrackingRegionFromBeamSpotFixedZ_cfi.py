import FWCore.ParameterSet.Config as cms

globalTrackingRegionFromBeamSpotFixedZ = cms.EDProducer('GlobalTrackingRegionFromBeamSpotEDProducer',
  RegionPSet = cms.PSet(
    precise = cms.bool(True),
    useMultipleScattering = cms.bool(False),
    nSigmaZ = cms.double(0),
    originHalfLength = cms.double(21.2),
    originRadius = cms.double(0.2),
    ptMin = cms.double(0.9),
    beamSpot = cms.InputTag('offlineBeamSpot')
  )
)
