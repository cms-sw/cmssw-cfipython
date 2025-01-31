import FWCore.ParameterSet.Config as cms

def HeavyIonCSVESProducer(*args, **kwargs):
  mod = cms.ESProducer('HeavyIonCSVESProducer',
    useCondDB = cms.bool(False),
    useAdaBoost = cms.bool(False),
    useGBRForest = cms.bool(True),
    mvaName = cms.string(''),
    gbrForestLabel = cms.string(''),
    weightFile = cms.FileInPath(''),
    sv_cfg = cms.PSet(),
    variables = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
