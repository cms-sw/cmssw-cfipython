import FWCore.ParameterSet.Config as cms

hltDisplacedmumumuFilter = cms.EDFilter('HLTDisplacedmumumuFilter',
  saveTags = cms.bool(False),
  FastAccept = cms.bool(False),
  MinLxySignificance = cms.double(0),
  MaxLxySignificance = cms.double(0),
  MaxNormalisedChi2 = cms.double(10),
  MinVtxProbability = cms.double(0),
  MinCosinePointingAngle = cms.double(-2),
  DisplacedVertexTag = cms.InputTag('hltDisplacedmumumuVtx'),
  BeamSpotTag = cms.InputTag('hltOnlineBeamSpot'),
  MuonTag = cms.InputTag('hltL3MuonCandidates')
)
