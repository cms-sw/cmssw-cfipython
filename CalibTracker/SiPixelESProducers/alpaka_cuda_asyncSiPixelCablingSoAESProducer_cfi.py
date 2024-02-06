import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncSiPixelCablingSoAESProducer = cms.ESProducer('alpaka_cuda_async::SiPixelCablingSoAESProducer',
  CablingMapLabel = cms.string(''),
  UseQualityInfo = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
