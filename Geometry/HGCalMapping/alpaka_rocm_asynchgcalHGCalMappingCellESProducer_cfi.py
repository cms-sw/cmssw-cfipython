import FWCore.ParameterSet.Config as cms

alpaka_rocm_asynchgcalHGCalMappingCellESProducer = cms.ESProducer('alpaka_rocm_async::hgcal::HGCalMappingCellESProducer',
  filelist = cms.vstring(),
  cellindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
