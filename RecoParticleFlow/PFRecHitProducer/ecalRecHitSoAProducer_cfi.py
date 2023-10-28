import FWCore.ParameterSet.Config as cms

ecalRecHitSoAProducer = cms.EDProducer('ECALRecHitSoAProducer@alpaka',
  src = cms.required.InputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
