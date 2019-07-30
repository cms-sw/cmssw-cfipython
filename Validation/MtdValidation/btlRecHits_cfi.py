import FWCore.ParameterSet.Config as cms

btlRecHits = cms.EDProducer('BtlRecHitsValidation',
  folder = cms.string('MTD/BTL/RecHits'),
  inputTag = cms.InputTag('mtdRecHits', 'FTLBarrel'),
  simHitsTag = cms.InputTag('mix', 'g4SimHitsFastTimerHitsBarrel'),
  hitMinimumEnergy = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)
