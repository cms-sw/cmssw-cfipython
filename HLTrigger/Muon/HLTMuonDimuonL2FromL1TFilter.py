import FWCore.ParameterSet.Config as cms

def HLTMuonDimuonL2FromL1TFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonDimuonL2FromL1TFilter',
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    CandTag = cms.InputTag('hltL2MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    SeedMapTag = cms.InputTag('hltL2Muons'),
    FastAccept = cms.bool(False),
    MaxEta = cms.double(2.5),
    MinNhits = cms.int32(0),
    MinNstations = cms.int32(0),
    MinNchambers = cms.int32(2),
    MaxDr = cms.double(100),
    MaxDz = cms.double(9999),
    ChargeOpt = cms.int32(0),
    MinPtPair = cms.double(0),
    MinPtMax = cms.double(3),
    MinPtMin = cms.double(3),
    MinInvMass = cms.double(1.6),
    MaxInvMass = cms.double(5.6),
    MinAcop = cms.double(-1),
    MaxAcop = cms.double(3.15),
    MinAngle = cms.double(-999),
    MaxAngle = cms.double(2.5),
    MinPtBalance = cms.double(-1),
    MaxPtBalance = cms.double(999999),
    NSigmaPt = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
