import FWCore.ParameterSet.Config as cms

def HLTMuonL3andL2PreFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonL3andL2PreFilter',
    saveTags = cms.bool(True),
    L3CandTag = cms.InputTag('hltL3MuonCandidates'),
    L2CandTag = cms.InputTag('hltL2MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    BeamSpotTag = cms.InputTag('hltOnlineBeamSpot'),
    MatchToPreviousCand = cms.bool(True),
    MaxDeltaRL2L3 = cms.double(0.05),
    L2CandSelection = cms.PSet(
      MinN = cms.int32(1),
      MaxDXYBeamSpot = cms.double(9999),
      MinDXYBeamSpot = cms.double(-1),
      MaxDz = cms.double(9999),
      MinDxySig = cms.double(-1),
      NSigmaPt = cms.double(0),
      MaxPtDifference = cms.double(9999),
      MinTrackPt = cms.double(0),
      MaxNormalizedChi2 = cms.double(9999),
      MinPt = cms.double(23),
      MaxEta = cms.double(2.5),
      MinNmuonHits = cms.int32(0),
      MinNhits = cms.vint32(
        1,
        0
      ),
      AbsEtaBins = cms.vdouble(
        1,
        9999
      ),
      MinNstations = cms.vint32(
        1,
        1
      ),
      MinNchambers = cms.vint32(
        1,
        0
      )
    ),
    L3CandSelection = cms.PSet(
      MinN = cms.int32(1),
      MaxDXYBeamSpot = cms.double(9999),
      MinDXYBeamSpot = cms.double(-1),
      MaxDz = cms.double(9999),
      MinDxySig = cms.double(-1),
      NSigmaPt = cms.double(0),
      MaxPtDifference = cms.double(9999),
      MinTrackPt = cms.double(0),
      MaxNormalizedChi2 = cms.double(9999),
      MinPt = cms.double(23),
      MaxEta = cms.double(2.5),
      MinNmuonHits = cms.int32(0),
      MinNhits = cms.vint32(
        1,
        0
      ),
      AbsEtaBins = cms.vdouble(
        1,
        9999
      ),
      MinNstations = cms.vint32(
        1,
        1
      ),
      MinNchambers = cms.vint32(
        1,
        0
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
