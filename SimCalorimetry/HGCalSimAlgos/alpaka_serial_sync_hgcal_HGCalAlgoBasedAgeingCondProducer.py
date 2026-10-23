import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_hgcal_HGCalAlgoBasedAgeingCondProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::hgcal::HGCalAlgoBasedAgeingCondProducer',
    denseIndexer = cms.ESInputTag('', ''),
    cellMappingSource = cms.ESInputTag('', ''),
    doseMapURL = cms.required.FileInPath,
    doseMapAlgo = cms.required.uint32,
    scaleByDoseFactor = cms.required.double,
    ileakParam = cms.required.vdouble,
    cceParams = cms.PSet(
      cceParam120 = cms.required.vdouble,
      cceParam200 = cms.required.vdouble,
      cceParam300 = cms.required.vdouble
    ),
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
