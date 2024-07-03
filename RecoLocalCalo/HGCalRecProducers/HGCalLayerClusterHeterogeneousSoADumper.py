import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterHeterogeneousSoADumper(**kwargs):
  mod = cms.EDAnalyzer('HGCalLayerClusterHeterogeneousSoADumper',
    src = cms.InputTag('hltHgcalSoALayerClustersProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
