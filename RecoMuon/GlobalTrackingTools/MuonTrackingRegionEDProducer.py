import FWCore.ParameterSet.Config as cms

def MuonTrackingRegionEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonTrackingRegionEDProducer',
    EtaR_UpperLimit_Par1 = cms.double(0.25),
    DeltaR = cms.double(0.2),
    OnDemand = cms.int32(-1),
    Rescale_phi = cms.double(3),
    Eta_fixed = cms.bool(False),
    Rescale_eta = cms.double(3),
    PhiR_UpperLimit_Par2 = cms.double(0.2),
    Eta_min = cms.double(0.05),
    Phi_fixed = cms.bool(False),
    Phi_min = cms.double(0.05),
    PhiR_UpperLimit_Par1 = cms.double(0.6),
    EtaR_UpperLimit_Par2 = cms.double(0.15),
    UseVertex = cms.bool(False),
    Rescale_Dz = cms.double(3),
    Pt_fixed = cms.bool(False),
    Z_fixed = cms.bool(True),
    Pt_min = cms.double(1.5),
    DeltaZ = cms.double(15.9),
    DeltaEta = cms.double(0.2),
    DeltaPhi = cms.double(0.2),
    maxRegions = cms.int32(1),
    precise = cms.bool(True),
    beamSpot = cms.InputTag(''),
    vertexCollection = cms.InputTag(''),
    MeasurementTrackerName = cms.InputTag(''),
    input = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
