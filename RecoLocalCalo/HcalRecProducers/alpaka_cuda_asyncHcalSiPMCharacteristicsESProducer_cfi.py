import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncHcalSiPMCharacteristicsESProducer = cms.ESProducer('alpaka_cuda_async::HcalSiPMCharacteristicsESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
