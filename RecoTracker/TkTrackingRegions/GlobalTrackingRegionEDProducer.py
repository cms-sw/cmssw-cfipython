import FWCore.ParameterSet.Config as cms

def GlobalTrackingRegionEDProducer(**kwargs):
  mod = cms.EDProducer('GlobalTrackingRegionEDProducer',
    RegionPSet = cms.PSet(
      precise = cms.bool(True),
      useMultipleScattering = cms.bool(False),
      originHalfLength = cms.double(21.2),
      originRadius = cms.double(0.2),
      originXPos = cms.double(0),
      originYPos = cms.double(0),
      originZPos = cms.double(0),
      ptMin = cms.double(0.9)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
