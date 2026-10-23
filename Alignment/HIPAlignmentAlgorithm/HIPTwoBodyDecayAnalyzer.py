import FWCore.ParameterSet.Config as cms

def HIPTwoBodyDecayAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HIPTwoBodyDecayAnalyzer',
    alcarecotracks = cms.InputTag('ALCARECOTkAlZMuMu'),
    refit1tracks = cms.InputTag('FirstTrackRefitter'),
    refit2tracks = cms.InputTag('HitFilteredTracksTrackFitter'),
    finaltracks = cms.InputTag('FinalTrackRefitter'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
