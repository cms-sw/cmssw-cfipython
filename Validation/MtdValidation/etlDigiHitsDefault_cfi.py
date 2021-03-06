import FWCore.ParameterSet.Config as cms

etlDigiHitsDefault = cms.EDProducer('EtlDigiHitsValidation',
  folder = cms.string('MTD/ETL/DigiHits'),
  inputTag = cms.InputTag('mix', 'FTLEndcap'),
  mightGet = cms.optional.untracked.vstring
)
