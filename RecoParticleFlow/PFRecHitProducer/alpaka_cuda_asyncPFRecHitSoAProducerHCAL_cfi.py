import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncPFRecHitSoAProducerHCAL = cms.EDProducer('alpaka_cuda_async::PFRecHitSoAProducerHCAL',
  producers = cms.required.VPSet,
  topology = cms.required.ESInputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
