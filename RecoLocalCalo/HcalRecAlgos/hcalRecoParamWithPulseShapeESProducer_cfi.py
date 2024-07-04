import FWCore.ParameterSet.Config as cms

hcalRecoParamWithPulseShapeESProducer = cms.ESProducer('HcalRecoParamWithPulseShapeESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
