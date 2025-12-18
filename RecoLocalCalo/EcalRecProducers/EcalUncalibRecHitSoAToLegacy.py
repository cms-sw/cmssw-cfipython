import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitSoAToLegacy(*args, **kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitSoAToLegacy',
    outputLabelEB = cms.string('EcalUncalibRecHitsEB'),
    isPhase2 = cms.bool(False),
    inputCollectionEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
    inputCollectionEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
    outputLabelEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
