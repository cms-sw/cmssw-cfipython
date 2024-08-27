import FWCore.ParameterSet.Config as cms

def HLTMuonTrimuonL3Filter(**kwargs):
  mod = cms.EDFilter('HLTMuonTrimuonL3Filter',
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    FastAccept = cms.bool(False),
    MaxEta = cms.double(2.5),
    MinNhits = cms.int32(0),
    MaxDr = cms.double(2),
    MaxDz = cms.double(9999),
    ChargeOpt = cms.int32(0),
    MinPtTriplet = cms.double(0),
    MinPtMax = cms.double(3),
    MinPtMin = cms.double(3),
    MinInvMass = cms.double(2.8),
    MaxInvMass = cms.double(3.4),
    MinAcop = cms.double(-1),
    MaxAcop = cms.double(3.15),
    MinPtBalance = cms.double(-1),
    MaxPtBalance = cms.double(999999),
    NSigmaPt = cms.double(0),
    MaxDCAMuMu = cms.double(99999.9),
    MaxRapidityTriplet = cms.double(999999),
    InputLinks = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
