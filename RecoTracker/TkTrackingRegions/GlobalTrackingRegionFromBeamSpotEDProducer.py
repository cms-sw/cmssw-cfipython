import FWCore.ParameterSet.Config as cms

def GlobalTrackingRegionFromBeamSpotEDProducer(*args, **kwargs):
  mod = cms.EDProducer('GlobalTrackingRegionFromBeamSpotEDProducer',
    RegionPSet = cms.PSet(
      precise = cms.bool(True),
      useMultipleScattering = cms.bool(False),
      nSigmaZ = cms.double(4),
      originHalfLength = cms.double(0),
      originRadius = cms.double(0.2),
      ptMin = cms.double(0.9),
      beamSpot = cms.InputTag('offlineBeamSpot')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
