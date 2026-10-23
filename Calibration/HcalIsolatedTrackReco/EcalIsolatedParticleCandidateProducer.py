import FWCore.ParameterSet.Config as cms

def EcalIsolatedParticleCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalIsolatedParticleCandidateProducer',
    ECHitEnergyThreshold = cms.double(0.05),
    L1eTauJetsSource = cms.InputTag('l1extraParticles', 'Tau'),
    L1GTSeedLabel = cms.InputTag('l1sIsolTrack'),
    EBrecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EErecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    ECHitCountEnergyThreshold = cms.double(0.5),
    EcalInnerConeSize = cms.double(0.3),
    EcalOuterConeSize = cms.double(0.7),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
