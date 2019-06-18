import FWCore.ParameterSet.Config as cms

mtdTrackingRecHitProducer = cms.EDProducer('MTDTrackingRecHitProducer',
  barrelClusters = cms.InputTag('mtdClusters', 'FTLBarrel'),
  endcapClusters = cms.InputTag('mtdClusters', 'FTLEndcap'),
  mightGet = cms.optional.untracked.vstring
)
