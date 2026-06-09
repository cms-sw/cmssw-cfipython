import FWCore.ParameterSet.Config as cms

from .GlobalTrackingRegionFromBeamSpotEDProducer import GlobalTrackingRegionFromBeamSpotEDProducer

globalTrackingRegionFromBeamSpotFixedZ = GlobalTrackingRegionFromBeamSpotEDProducer(

  RegionPSet = dict(
    nSigmaZ = 0,
    originHalfLength = 21.2
  )
)
