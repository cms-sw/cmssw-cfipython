import FWCore.ParameterSet.Config as cms

def CandidateBoostedDoubleSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateBoostedDoubleSecondaryVertexESProducer',
    useCondDB = cms.bool(False),
    gbrForestLabel = cms.string(''),
    weightFile = cms.FileInPath(''),
    useGBRForest = cms.bool(False),
    useAdaBoost = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
