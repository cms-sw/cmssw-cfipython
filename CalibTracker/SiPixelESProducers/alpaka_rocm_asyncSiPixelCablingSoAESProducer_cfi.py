import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncSiPixelCablingSoAESProducer = cms.ESProducer('alpaka_rocm_async::SiPixelCablingSoAESProducer',
  CablingMapLabel = cms.string(''),
  UseQualityInfo = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
