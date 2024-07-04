import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncHcalSiPMCharacteristicsESProducer = cms.ESProducer('alpaka_rocm_async::HcalSiPMCharacteristicsESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
