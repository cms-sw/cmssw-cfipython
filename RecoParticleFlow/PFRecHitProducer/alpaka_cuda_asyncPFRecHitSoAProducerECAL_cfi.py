import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncPFRecHitSoAProducerECAL = cms.EDProducer('alpaka_cuda_async::PFRecHitSoAProducerECAL',
  producers = cms.VPSet(
    cms.PSet(
      src = cms.InputTag('')
    )
  ),
  topology = cms.ESInputTag('', ''),
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
