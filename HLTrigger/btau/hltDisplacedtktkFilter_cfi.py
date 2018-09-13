import FWCore.ParameterSet.Config as cms

hltDisplacedtktkFilter = cms.EDFilter('HLTDisplacedtktkFilter',
  saveTags = cms.bool(False),
  FastAccept = cms.bool(False),
  MinLxySignificance = cms.double(0),
  MaxLxySignificance = cms.double(0),
  MaxNormalisedChi2 = cms.double(10),
  MinVtxProbability = cms.double(0),
  MinCosinePointingAngle = cms.double(-2),
  triggerTypeDaughters = cms.int32(0),
  DisplacedVertexTag = cms.InputTag('hltDisplacedtktkVtx'),
  BeamSpotTag = cms.InputTag('hltOnlineBeamSpot'),
  TrackTag = cms.InputTag('hltL3MuonCandidates')
)
