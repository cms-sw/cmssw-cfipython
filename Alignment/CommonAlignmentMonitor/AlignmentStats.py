import FWCore.ParameterSet.Config as cms

def AlignmentStats(*args, **kwargs):
  mod = cms.EDAnalyzer('AlignmentStats',
    src = cms.InputTag('generalTracks'),
    OverlapAssoMap = cms.InputTag('OverlapAssoMap'),
    keepTrackStats = cms.bool(False),
    keepHitStats = cms.bool(False),
    TrkStatsFileName = cms.string('tracks_statistics.root'),
    HitStatsFileName = cms.string('HitMaps.root'),
    TrkStatsPrescale = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
