import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncHcalRecoParamWithPulseShapeESProducer = cms.ESProducer('alpaka_rocm_async::HcalRecoParamWithPulseShapeESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
