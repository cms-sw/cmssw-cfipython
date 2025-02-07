import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitSoAToLegacy(*args, **kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitSoAToLegacy',
    inputCollectionEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
    outputLabelEB = cms.string('EcalUncalibRecHitsEB'),
    isPhase2 = cms.bool(False),
    inputCollectionEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
    outputLabelEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
