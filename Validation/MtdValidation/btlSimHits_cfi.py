import FWCore.ParameterSet.Config as cms

btlSimHits = cms.EDProducer('BtlSimHitsValidation',
  folder = cms.string('MTD/BTL/SimHits'),
  inputTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
  hitMinimumEnergy = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
