import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncEcalMultifitConditionsHostESProducer = cms.ESProducer('alpaka_cuda_async::EcalMultifitConditionsHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
