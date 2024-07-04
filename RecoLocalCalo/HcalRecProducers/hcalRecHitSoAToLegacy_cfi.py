import FWCore.ParameterSet.Config as cms

hcalRecHitSoAToLegacy = cms.EDProducer('HcalRecHitSoAToLegacy',
  src = cms.InputTag('hbheRecHitProducerPortable'),
  mightGet = cms.optional.untracked.vstring
)
