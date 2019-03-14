import FWCore.ParameterSet.Config as cms

globalTrackingRegion = cms.EDProducer('GlobalTrackingRegionEDProducer',
  RegionPSet = cms.PSet(
    precise = cms.bool(True),
    useMultipleScattering = cms.bool(False),
    originHalfLength = cms.double(21.2),
    originRadius = cms.double(0.2),
    originXPos = cms.double(0),
    originYPos = cms.double(0),
    originZPos = cms.double(0),
    ptMin = cms.double(0.9)
  )
)
