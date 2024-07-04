import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncHcalRecoParamWithPulseShapeESProducer = cms.ESProducer('alpaka_cuda_async::HcalRecoParamWithPulseShapeESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
