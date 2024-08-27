import FWCore.ParameterSet.Config as cms

def HGCalLayerClustersFromSoAProducer(**kwargs):
  mod = cms.EDProducer('HGCalLayerClustersFromSoAProducer',
    src = cms.InputTag('hltHgcalSoALayerClustersProducer'),
    hgcalRecHitsLayerClustersSoA = cms.InputTag('hltHgcalSoARecHitsLayerClustersProducer'),
    hgcalRecHitsSoA = cms.InputTag('hltHgcalSoARecHitsProducer'),
    nHitsTime = cms.uint32(3),
    timeClname = cms.string('timeLayerCluster'),
    detector = cms.string('EE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
