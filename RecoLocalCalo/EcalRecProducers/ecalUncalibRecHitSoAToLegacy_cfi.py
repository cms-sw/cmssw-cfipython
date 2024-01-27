import FWCore.ParameterSet.Config as cms

ecalUncalibRecHitSoAToLegacy = cms.EDProducer('EcalUncalibRecHitSoAToLegacy',
  uncalibRecHitsPortableEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
  recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
  isPhase2 = cms.bool(False),
  uncalibRecHitsPortableEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
  recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)
