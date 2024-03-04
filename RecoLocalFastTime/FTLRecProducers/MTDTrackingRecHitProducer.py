import FWCore.ParameterSet.Config as cms

def MTDTrackingRecHitProducer(**kwargs):
  mod = cms.EDProducer('MTDTrackingRecHitProducer',
    barrelClusters = cms.InputTag('mtdClusters', 'FTLBarrel'),
    endcapClusters = cms.InputTag('mtdClusters', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
