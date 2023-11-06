import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncPFRecHitECALParamsESProducer = cms.ESProducer('alpaka_rocm_async::PFRecHitECALParamsESProducer',
  cleaningThreshold = cms.double(2),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
