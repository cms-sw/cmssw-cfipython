import FWCore.ParameterSet.Config as cms

def CombinedMVAV2JetTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('CombinedMVAV2JetTagESProducer',
    useCondDB = cms.bool(False),
    gbrForestLabel = cms.string(''),
    jetTagComputers = cms.vstring(),
    mvaName = cms.string(''),
    variables = cms.vstring(),
    spectators = cms.vstring(),
    weightFile = cms.FileInPath(''),
    useGBRForest = cms.bool(False),
    useAdaBoost = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
