import FWCore.ParameterSet.Config as cms

def MultiClustersFromTrackstersProducer(**kwargs):
  mod = cms.EDProducer('MultiClustersFromTrackstersProducer',
    Tracksters = cms.InputTag('Tracksters', 'TrackstersByCA'),
    LayerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    verbosity = cms.untracked.uint32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
