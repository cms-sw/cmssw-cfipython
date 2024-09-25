import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingCellESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingCellESProducer@alpaka',
    filelist = cms.vstring(),
    cellindexer = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
