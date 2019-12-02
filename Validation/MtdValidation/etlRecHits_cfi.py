import FWCore.ParameterSet.Config as cms

etlRecHits = cms.EDProducer('EtlRecHitsValidation',
  folder = cms.string('MTD/ETL/RecHits'),
  inputTag = cms.InputTag('mtdRecHits', 'FTLEndcap'),
  mightGet = cms.optional.untracked.vstring
)
