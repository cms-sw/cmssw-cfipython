import FWCore.ParameterSet.Config as cms

def FastDMRChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('FastDMRChecker',
    minHitsPerModule = cms.int32(10),
    VertexCollection = cms.string('offlinePrimaryVertices'),
    VertexCut = cms.untracked.bool(False),
    trajectoryInput = cms.string('generalTracks'),
    Tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
