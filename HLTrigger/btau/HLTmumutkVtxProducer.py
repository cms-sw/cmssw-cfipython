import FWCore.ParameterSet.Config as cms

def HLTmumutkVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTmumutkVtxProducer',
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
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
