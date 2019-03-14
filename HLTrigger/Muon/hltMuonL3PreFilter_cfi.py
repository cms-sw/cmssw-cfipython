import FWCore.ParameterSet.Config as cms

hltMuonL3PreFilter = cms.EDFilter('HLTMuonL3PreFilter',
  saveTags = cms.bool(True),
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
  CandTag = cms.InputTag('hltL3MuonCandidates'),
  PreviousCandTag = cms.InputTag(''),
  L1CandTag = cms.InputTag(''),
  inputMuonCollection = cms.InputTag(''),
  MinN = cms.int32(1),
  MaxEta = cms.double(2.5),
  MinNhits = cms.int32(0),
  MaxDr = cms.double(2),
  MinDr = cms.double(-1),
  MaxDz = cms.double(9999),
  MinDxySig = cms.double(-1),
  MinPt = cms.double(3),
  NSigmaPt = cms.double(0),
  MaxNormalizedChi2 = cms.double(9999),
  MaxDXYBeamSpot = cms.double(9999),
  MinDXYBeamSpot = cms.double(-1),
  MinNmuonHits = cms.int32(0),
  MaxPtDifference = cms.double(9999),
  MinTrackPt = cms.double(0),
  minMuonStations = cms.int32(-1),
  minTrkHits = cms.int32(-1),
  minMuonHits = cms.int32(-1),
  allowedTypeMask = cms.uint32(255),
  requiredTypeMask = cms.uint32(0),
  MaxNormalizedChi2_L3FromL1 = cms.double(9999),
  trkMuonId = cms.uint32(0),
  L1MatchingdR = cms.double(0.3),
  MatchToPreviousCand = cms.bool(True),
  InputLinks = cms.InputTag('')
)
