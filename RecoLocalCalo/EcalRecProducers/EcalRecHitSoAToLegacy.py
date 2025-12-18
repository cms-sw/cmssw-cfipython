import FWCore.ParameterSet.Config as cms

def EcalRecHitSoAToLegacy(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitSoAToLegacy',
    inputCollectionEB = cms.InputTag('ecalRecHitPortable', 'EcalRecHitsEB'),
    outputLabelEB = cms.string('EcalRecHitsEB'),
    isPhase2 = cms.bool(False),
    inputCollectionEE = cms.InputTag('ecalRecHitPortable', 'EcalRecHitsEE'),
    outputLabelEE = cms.string('EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
