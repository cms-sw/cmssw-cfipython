import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterDQM(*args, **kwargs):
  mod = cms.EDProducer('HGCalLayerClusterDQM',
    RecHits = cms.InputTag('hgcalRecHits'),
    layerClusters = cms.InputTag('hgcalSoALayerClusters'),
    MinimumEvents = cms.uint32(10000),
    PrescaleFactor = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
