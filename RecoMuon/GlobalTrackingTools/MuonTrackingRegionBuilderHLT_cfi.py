import FWCore.ParameterSet.Config as cms

from .MuonTrackingRegionEDProducer import MuonTrackingRegionEDProducer

MuonTrackingRegionBuilderHLT = MuonTrackingRegionEDProducer(
  EtaR_UpperLimit_Par1 = 0.25,
  DeltaR = 0.2,
  beamSpot = ('hltOnlineBeamSpot'),
  OnDemand = -1,
  vertexCollection = ('pixelVertices'),
  Rescale_phi = 3,
  Eta_fixed = False,
  Rescale_eta = 3,
  PhiR_UpperLimit_Par2 = 0.2,
  Eta_min = 0.05,
  Phi_fixed = False,
  Phi_min = 0.05,
  PhiR_UpperLimit_Par1 = 0.6,
  EtaR_UpperLimit_Par2 = 0.15,
  MeasurementTrackerName = ('hltESPMeasurementTracker'),
  UseVertex = False,
  Rescale_Dz = 3,
  Pt_fixed = False,
  Z_fixed = True,
  Pt_min = 1.5,
  DeltaZ = 15.9,
  DeltaEta = 0.2,
  DeltaPhi = 0.2,
  maxRegions = 1,
  precise = True,
  input = ('hltL2Muons', 'UpdatedAtVtx')
)
