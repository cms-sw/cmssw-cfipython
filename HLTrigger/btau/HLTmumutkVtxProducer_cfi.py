import FWCore.ParameterSet.Config as cms

HLTmumutkVtxProducer = cms.EDProducer('HLTmumutkVtxProducer',
  MuCand = cms.InputTag('hltMuTracks'),
  TrackCand = cms.InputTag('hltMumukAllConeTracks'),
  PreviousCandTag = cms.InputTag('hltDisplacedmumuFilterDoubleMu4Jpsi'),
  SimpleMagneticField = cms.string(''),
  ThirdTrackMass = cms.double(0.493677),
  MaxEta = cms.double(2.5),
  MinPt = cms.double(3),
  MinInvMass = cms.double(0),
  MaxInvMass = cms.double(99999),
  MinD0Significance = cms.double(0),
  OverlapDR = cms.double(0.000144),
  BeamSpotTag = cms.InputTag('hltOfflineBeamSpot')
)
