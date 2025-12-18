import FWCore.ParameterSet.Config as cms

def HLTMuonL3SimplePreFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonL3SimplePreFilter',
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    MinN = cms.int32(1),
    MaxEta = cms.double(2.5),
    MinNhits = cms.int32(0),
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
    MatchToPreviousCand = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
