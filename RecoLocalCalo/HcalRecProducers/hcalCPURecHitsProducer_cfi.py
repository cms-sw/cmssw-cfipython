import FWCore.ParameterSet.Config as cms

hcalCPURecHitsProducer = cms.EDProducer('HcalCPURecHitsProducer',
  recHitsM0LabelIn = cms.InputTag('hbheRecHitProducerGPU', 'recHitsM0HBHE'),
  recHitsM0LabelOut = cms.string('recHitsM0HBHE'),
  recHitsLegacyLabelOut = cms.string('recHitsLegacyHBHE'),
  mightGet = cms.optional.untracked.vstring
)
