import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncPFRecHitECALTopologyESProducer = cms.ESProducer('alpaka_rocm_async::PFRecHitECALTopologyESProducer',
  usePFThresholdsFromDB = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
