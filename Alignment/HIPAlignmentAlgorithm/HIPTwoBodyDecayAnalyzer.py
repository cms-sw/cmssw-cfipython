import FWCore.ParameterSet.Config as cms

def HIPTwoBodyDecayAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HIPTwoBodyDecayAnalyzer',
    alcarecotracks = cms.InputTag('ALCARECOTkAlZMuMu'),
    refit1tracks = cms.InputTag('FirstTrackRefitter'),
    refit2tracks = cms.InputTag('HitFilteredTracksTrackFitter'),
    finaltracks = cms.InputTag('FinalTrackRefitter'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
