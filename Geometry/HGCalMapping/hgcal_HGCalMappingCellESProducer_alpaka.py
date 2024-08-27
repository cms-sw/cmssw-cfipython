import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingCellESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingCellESProducer@alpaka',
    filelist = cms.vstring(),
    cellindexer = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
