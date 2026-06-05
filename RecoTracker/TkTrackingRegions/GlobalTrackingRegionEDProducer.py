import FWCore.ParameterSet.Config as cms

def GlobalTrackingRegionEDProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
