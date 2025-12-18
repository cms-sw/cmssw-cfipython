import FWCore.ParameterSet.Config as cms

def HLTScoutingTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTScoutingTrackProducer',
    OtherTracks = cms.InputTag('hltPixelTracksL3MuonNoVtx'),
    vertexCollection = cms.InputTag('hltPixelVertices'),
    mantissaPrecision = cms.int32(10),
    vtxMinDist = cms.double(0.01),
    ptMin = cms.double(0.3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
