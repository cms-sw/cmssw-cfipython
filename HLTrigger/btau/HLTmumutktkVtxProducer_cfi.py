import FWCore.ParameterSet.Config as cms

HLTmumutktkVtxProducer = cms.EDProducer('HLTmumutktkVtxProducer',
  MuCand = cms.InputTag('hltMuTracks'),
  TrackCand = cms.InputTag('hltMumukAllConeTracks'),
  PreviousCandTag = cms.InputTag('hltDisplacedmumuFilterDoubleMu4Jpsi'),
  SimpleMagneticField = cms.string(''),
  ThirdTrackMass = cms.double(0.493677),
  FourthTrackMass = cms.double(0.493677),
  MaxEta = cms.double(2.5),
  MinPt = cms.double(0),
  MinInvMass = cms.double(0),
  MaxInvMass = cms.double(99999),
  MinTrkTrkMass = cms.double(0),
  MaxTrkTrkMass = cms.double(99999),
  MinD0Significance = cms.double(0),
  OppositeSign = cms.bool(False),
  OverlapDR = cms.double(0.001),
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot')
)
