import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitSoAToLegacy(*args, **kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitSoAToLegacy',
    uncalibRecHitsPortableEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
    recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
    isPhase2 = cms.bool(False),
    uncalibRecHitsPortableEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
    recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
