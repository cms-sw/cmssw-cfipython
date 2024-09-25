import FWCore.ParameterSet.Config as cms

def HLTmmkkFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTmmkkFilter',
    saveTags = cms.bool(True),
    MuCand = cms.InputTag('hltMuTracks'),
    TrackCand = cms.InputTag('hltMumukAllConeTracks'),
    ThirdTrackMass = cms.double(0.106),
    FourthTrackMass = cms.double(0.106),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(3),
    MinInvMass = cms.double(1.2),
    MaxInvMass = cms.double(2.2),
    MaxNormalisedChi2 = cms.double(10),
    MinLxySignificance = cms.double(3),
    MinCosinePointingAngle = cms.double(0.9),
    MinD0Significance = cms.double(0),
    FastAccept = cms.bool(False),
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
