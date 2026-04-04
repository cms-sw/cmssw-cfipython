import FWCore.ParameterSet.Config as cms

from .MuonTrackingRegionEDProducer import MuonTrackingRegionEDProducer

MuonTrackingRegionBuilderHLT = MuonTrackingRegionEDProducer(

  MeasurementTrackerName = ('hltESPMeasurementTracker'),
  beamSpot = ('hltOnlineBeamSpot'),
  input = ('hltL2Muons', 'UpdatedAtVtx'),
  vertexCollection = ('pixelVertices')
)
