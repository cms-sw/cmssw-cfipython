import FWCore.ParameterSet.Config as cms

from .GlobalTrackingRegionFromBeamSpotEDProducer import GlobalTrackingRegionFromBeamSpotEDProducer

globalTrackingRegionFromBeamSpot = GlobalTrackingRegionFromBeamSpotEDProducer(
  RegionPSet = dict(
    precise = True,
    useMultipleScattering = False,
    nSigmaZ = 4,
    originHalfLength = 0,
    originRadius = 0.2,
    ptMin = 0.9,
    beamSpot = ('offlineBeamSpot')
  )
)
