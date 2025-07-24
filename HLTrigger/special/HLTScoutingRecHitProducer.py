import FWCore.ParameterSet.Config as cms

def HLTScoutingRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTScoutingRecHitProducer',
    pfRecHitsECAL = cms.InputTag('hltParticleFlowRecHitECALUnseeded'),
    pfRecHitsECALCleaned = cms.InputTag('hltParticleFlowRecHitECALUnseeded', 'Cleaned'),
    pfRecHitsHBHE = cms.InputTag('hltParticleFlowRecHitHBHE'),
    minEnergyEB = cms.double(-1),
    minEnergyEE = cms.double(-1),
    minEnergyCleanedEB = cms.double(-1),
    minEnergyCleanedEE = cms.double(-1),
    minEnergyHBHE = cms.double(-1),
    mantissaPrecision = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
