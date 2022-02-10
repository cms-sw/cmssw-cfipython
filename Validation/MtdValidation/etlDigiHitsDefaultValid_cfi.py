import FWCore.ParameterSet.Config as cms

etlDigiHitsDefaultValid = cms.EDProducer('EtlDigiHitsValidation',
  folder = cms.string('MTD/ETL/DigiHits'),
  inputTag = cms.InputTag('mix', 'FTLEndcap'),
  LocalPositionDebug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
