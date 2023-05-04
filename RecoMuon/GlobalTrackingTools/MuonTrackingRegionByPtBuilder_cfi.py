import FWCore.ParameterSet.Config as cms

MuonTrackingRegionByPtBuilder = cms.EDProducer('MuonTrackingRegionByPtEDProducer',
  DeltaR = cms.double(0.2),
  beamSpot = cms.InputTag(''),
  OnDemand = cms.int32(-1),
  vertexCollection = cms.InputTag(''),
  MeasurementTrackerName = cms.InputTag(''),
  UseVertex = cms.bool(False),
  Rescale_Dz = cms.double(3),
  Pt_fixed = cms.bool(False),
  Z_fixed = cms.bool(True),
  Pt_min = cms.double(1.5),
  DeltaZ = cms.double(15.9),
  ptRanges = cms.vdouble(
    0,
    1000000000
  ),
  deltaEtas = cms.vdouble(0.2),
  deltaPhis = cms.vdouble(0.15),
  maxRegions = cms.int32(1),
  precise = cms.bool(True),
  input = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
