import FWCore.ParameterSet.Config as cms

btlRecHits = cms.EDProducer('BtlRecHitsValidation',
  folder = cms.string('MTD/BTL/RecHits'),
  inputTag = cms.InputTag('mtdRecHits', 'FTLBarrel')
)
