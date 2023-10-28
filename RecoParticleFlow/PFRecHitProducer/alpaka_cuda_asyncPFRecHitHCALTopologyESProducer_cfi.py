import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncPFRecHitHCALTopologyESProducer = cms.ESProducer('alpaka_cuda_async::PFRecHitHCALTopologyESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
