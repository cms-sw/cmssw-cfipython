import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterHeterogeneousDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalLayerClusterHeterogeneousDumper',
    src = cms.InputTag('hltHgcalSoARecHitsLayerClustersProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
