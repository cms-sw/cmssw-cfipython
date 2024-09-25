import FWCore.ParameterSet.Config as cms

def HGCalLayerClusterHeterogeneousSoADumper(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalLayerClusterHeterogeneousSoADumper',
    src = cms.InputTag('hltHgcalSoALayerClustersProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
