import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterHeterogeneousDumper(**kwargs):
  mod = cms.EDAnalyzer('HGCalLayerClusterHeterogeneousDumper',
    src = cms.InputTag('hltHgcalSoARecHitsLayerClustersProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
