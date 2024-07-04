import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncHcalMahiConditionsESProducer = cms.ESProducer('alpaka_cuda_async::HcalMahiConditionsESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
