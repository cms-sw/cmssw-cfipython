import FWCore.ParameterSet.Config as cms

hltMuonTrackMassFilter = cms.EDFilter('HLTMuonTrackMassFilter',
  saveTags = cms.bool(True),
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
  CandTag = cms.InputTag('hltL3MuonCandidates'),
  TrackTag = cms.InputTag(''),
  PreviousCandTag = cms.InputTag(''),
  MinMasses = cms.vdouble(2.8),
  MaxMasses = cms.vdouble(3.4),
  checkCharge = cms.bool(True),
  MinTrackPt = cms.double(0),
  MinTrackP = cms.double(3),
  MaxTrackEta = cms.double(999),
  MaxTrackDxy = cms.double(999),
  MaxTrackDz = cms.double(999),
  MinTrackHits = cms.int32(5),
  MaxTrackNormChi2 = cms.double(10000000000),
  MaxDCAMuonTrack = cms.double(99999.9),
  CutCowboys = cms.bool(False)
)
