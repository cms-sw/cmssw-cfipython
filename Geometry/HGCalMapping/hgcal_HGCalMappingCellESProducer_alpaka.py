import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingCellESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingCellESProducer@alpaka',
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
