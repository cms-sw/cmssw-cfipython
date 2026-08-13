import FWCore.ParameterSet.Config as cms

def ScoutingTrackNtuplizer(*args, **kwargs):
  mod = cms.EDAnalyzer('ScoutingTrackNtuplizer',
    tracks = cms.InputTag('hltScoutingTrackPacker'),
    vertices = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    beamSpotLabel = cms.InputTag('hltOnlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
