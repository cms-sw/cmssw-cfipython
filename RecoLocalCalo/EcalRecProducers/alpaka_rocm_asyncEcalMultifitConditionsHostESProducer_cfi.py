import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncEcalMultifitConditionsHostESProducer = cms.ESProducer('alpaka_rocm_async::EcalMultifitConditionsHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
