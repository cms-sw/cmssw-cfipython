import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_hgcal_HGCalMappingCellESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::hgcal::HGCalMappingCellESProducer',
    filelist = cms.vstring(),
    cellindexer = cms.ESInputTag('', ''),
    moduleindexer = cms.ESInputTag('', ''),
    offsetfile = cms.FileInPath('Geometry/HGCalMapping/data/CellMaps/calibration_to_surrounding_offsetMap.txt'),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
