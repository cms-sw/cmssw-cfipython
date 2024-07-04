import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncHcalMahiConditionsESProducer = cms.ESProducer('alpaka_rocm_async::HcalMahiConditionsESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
