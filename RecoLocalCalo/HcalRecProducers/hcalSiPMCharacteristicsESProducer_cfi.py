import FWCore.ParameterSet.Config as cms

hcalSiPMCharacteristicsESProducer = cms.ESProducer('HcalSiPMCharacteristicsESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
