import FWCore.ParameterSet.Config as cms

hgcalShowerSeparationDefault = cms.EDProducer('HGCalShowerSeparation',
  debug = cms.int32(1),
  filterOnEnergyAndCaloP = cms.bool(False),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  mightGet = cms.optional.untracked.vstring
)
