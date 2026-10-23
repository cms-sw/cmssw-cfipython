import FWCore.ParameterSet.Config as cms

def HitResol(*args, **kwargs):
  mod = cms.EDAnalyzer('HitResol',
    lumiScalers = cms.InputTag('scalersRawToDigi'),
    combinatorialTracks = cms.InputTag('generalTracks'),
    trajectories = cms.InputTag('generalTracks'),
    CompressionSettings = cms.untracked.int32(-1),
    Layer = cms.int32(0),
    Debug = cms.bool(False),
    addLumi = cms.untracked.bool(False),
    cutOnTracks = cms.untracked.bool(False),
    trackMultiplicity = cms.untracked.uint32(100),
    MomentumCut = cms.untracked.double(3),
    UsePairsOnly = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
