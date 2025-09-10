import FWCore.ParameterSet.Config as cms

def MergedTrackstersProducer(*args, **kwargs):
  mod = cms.EDProducer('MergedTrackstersProducer',
    egamma_tracksters = cms.InputTag('ticlTrackstersCLUE3DEM'),
    had_tracksters = cms.InputTag('ticlTrackstersCLUE3DHAD'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
