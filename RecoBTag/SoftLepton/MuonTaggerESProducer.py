import FWCore.ParameterSet.Config as cms

def MuonTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('MuonTaggerESProducer',
    ipSign = cms.string('any'),
    leptonId = cms.string(''),
    qualityCut = cms.double(0.5),
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
