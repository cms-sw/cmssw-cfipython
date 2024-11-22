import FWCore.ParameterSet.Config as cms

def TracksterToSimTracksterAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterToSimTracksterAssociatorProducer',
    tracksters = cms.InputTag('trackstersProducer'),
    simTracksters = cms.InputTag('simTrackstersProducer'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracksterMap = cms.InputTag('tracksterAssociatorProducer'),
    simTracksterMap = cms.InputTag('simTracksterAssociatorProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
