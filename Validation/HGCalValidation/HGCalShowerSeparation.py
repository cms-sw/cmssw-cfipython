import FWCore.ParameterSet.Config as cms

def HGCalShowerSeparation(**kwargs):
  mod = cms.EDProducer('HGCalShowerSeparation',
    debug = cms.int32(1),
    filterOnEnergyAndCaloP = cms.bool(False),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
