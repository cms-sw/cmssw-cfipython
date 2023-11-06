import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncHCALRecHitSoAProducer = cms.EDProducer('alpaka_cuda_async::HCALRecHitSoAProducer',
  src = cms.required.InputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
