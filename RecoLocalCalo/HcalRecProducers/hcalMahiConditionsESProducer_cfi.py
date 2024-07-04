import FWCore.ParameterSet.Config as cms

hcalMahiConditionsESProducer = cms.ESProducer('HcalMahiConditionsESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
