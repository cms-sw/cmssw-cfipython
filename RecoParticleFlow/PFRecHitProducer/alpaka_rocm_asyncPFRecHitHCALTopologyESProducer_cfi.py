import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncPFRecHitHCALTopologyESProducer = cms.ESProducer('alpaka_rocm_async::PFRecHitHCALTopologyESProducer',
  usePFThresholdsFromDB = cms.bool(True),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
