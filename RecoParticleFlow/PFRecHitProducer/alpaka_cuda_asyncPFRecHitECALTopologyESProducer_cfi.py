import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncPFRecHitECALTopologyESProducer = cms.ESProducer('alpaka_cuda_async::PFRecHitECALTopologyESProducer',
  usePFThresholdsFromDB = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
