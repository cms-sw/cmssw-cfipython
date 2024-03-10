import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncPFRecHitSoAProducerHCAL = cms.EDProducer('alpaka_cuda_async::PFRecHitSoAProducerHCAL',
  producers = cms.VPSet(
    cms.PSet(
      params = cms.ESInputTag('', ''),
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
