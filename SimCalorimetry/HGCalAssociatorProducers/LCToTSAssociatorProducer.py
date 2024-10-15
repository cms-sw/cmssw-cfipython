import FWCore.ParameterSet.Config as cms

def LCToTSAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('LCToTSAssociatorProducer',
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracksters = cms.InputTag('ticlTracksters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
