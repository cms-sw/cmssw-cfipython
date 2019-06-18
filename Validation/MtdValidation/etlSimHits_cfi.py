import FWCore.ParameterSet.Config as cms

etlSimHits = cms.EDProducer('EtlSimHitsValidation',
  folder = cms.string('MTD/ETL/SimHits'),
  inputTag = cms.InputTag('g4SimHits', 'FastTimerHitsEndcap'),
  hitMinimumEnergy = cms.double(0.1),
  mightGet = cms.optional.untracked.vstring
)
