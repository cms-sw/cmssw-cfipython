import FWCore.ParameterSet.Config as cms

etlSimHitsValid = cms.EDProducer('EtlSimHitsValidation',
  folder = cms.string('MTD/ETL/SimHits'),
  inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsEndcap'),
  hitMinimumEnergy2Dis = cms.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
