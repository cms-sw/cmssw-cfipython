import FWCore.ParameterSet.Config as cms

from .GlobalTrackingRegionFromBeamSpotEDProducer import GlobalTrackingRegionFromBeamSpotEDProducer

globalTrackingRegionFromBeamSpotFixedZ = GlobalTrackingRegionFromBeamSpotEDProducer(
  RegionPSet = dict(
    precise = True,
    useMultipleScattering = False,
    nSigmaZ = 0,
    originHalfLength = 21.2,
    originRadius = 0.2,
    ptMin = 0.9,
    beamSpot = ('offlineBeamSpot')
  )
)
