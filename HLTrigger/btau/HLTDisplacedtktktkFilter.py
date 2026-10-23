import FWCore.ParameterSet.Config as cms

def HLTDisplacedtktktkFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTDisplacedtktktkFilter',
    saveTags = cms.bool(True),
    FastAccept = cms.bool(False),
    MinLxySignificance = cms.double(0),
    MaxLxySignificance = cms.double(0),
    MaxNormalisedChi2 = cms.double(10),
    MinVtxProbability = cms.double(0),
    MinCosinePointingAngle = cms.double(-2),
    triggerTypeDaughters = cms.int32(0),
    DisplacedVertexTag = cms.InputTag('hltDisplacedtktktkVtx'),
    BeamSpotTag = cms.InputTag('hltOnlineBeamSpot'),
    TrackTag = cms.InputTag('hltL3MuonCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
