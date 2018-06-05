import FWCore.ParameterSet.Config as cms

HLTmumutktkFilter = cms.EDFilter('HLTmumutktkFilter',
  saveTags = cms.bool(True),
  MaxEta = cms.double(2.5),
  MinPt = cms.double(0),
  MaxNormalisedChi2 = cms.double(10),
  MinVtxProbability = cms.double(0),
  MinLxySignificance = cms.double(3),
  MinCosinePointingAngle = cms.double(0.9),
  MuonTag = cms.InputTag('hltL3MuonCandidates'),
  TrackTag = cms.InputTag('hltMumukAllConeTracks'),
  MuMuTkVertexTag = cms.InputTag('hltDisplacedmumuVtxProducerDoubleMu4Jpsi'),
  BeamSpotTag = cms.InputTag('hltOnineBeamSpot')
)
