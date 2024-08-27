import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitSoAToLegacy(**kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitSoAToLegacy',
    uncalibRecHitsPortableEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
    recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
    isPhase2 = cms.bool(False),
    uncalibRecHitsPortableEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
    recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
