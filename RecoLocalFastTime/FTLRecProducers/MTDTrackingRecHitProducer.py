import FWCore.ParameterSet.Config as cms

def MTDTrackingRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDTrackingRecHitProducer',
    barrelClusters = cms.InputTag('mtdClusters', 'FTLBarrel'),
    endcapClusters = cms.InputTag('mtdClusters', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
