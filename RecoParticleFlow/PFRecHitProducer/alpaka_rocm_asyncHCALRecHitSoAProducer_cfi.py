import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncHCALRecHitSoAProducer = cms.EDProducer('alpaka_rocm_async::HCALRecHitSoAProducer',
  src = cms.required.InputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
