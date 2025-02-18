import FWCore.ParameterSet.Config as cms

def CharmTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('CharmTaggerESProducer',
    useCondDB = cms.bool(False),
    defaultValueNoTracks = cms.bool(False),
    useAdaBoost = cms.bool(False),
    useGBRForest = cms.bool(True),
    mvaName = cms.string('BTD'),
    gbrForestLabel = cms.string(''),
    weightFile = cms.FileInPath(''),
    slComputerCfg = cms.PSet(),
    variables = cms.VPSet(
      template = cms.PSetTemplate(
        idx = cms.int32(0),
        default = cms.double(1),
        name = cms.string(''),
        taggingVarName = cms.string('')
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
