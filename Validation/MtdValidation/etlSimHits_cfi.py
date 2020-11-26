import FWCore.ParameterSet.Config as cms

etlSimHits = cms.EDProducer('EtlSimHitsValidation',
  folder = cms.string('MTD/ETL/SimHits'),
  inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsEndcap'),
  hitMinimumEnergy1Dis = cms.double(0.1),
  hitMinimumEnergy2Dis = cms.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
