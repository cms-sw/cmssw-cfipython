import FWCore.ParameterSet.Config as cms

def MergedTrackstersProducer(**kwargs):
  mod = cms.EDProducer('MergedTrackstersProducer',
    egamma_tracksters = cms.InputTag('ticlTrackstersCLUE3DEM'),
    had_tracksters = cms.InputTag('ticlTrackstersCLUE3DHAD'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
