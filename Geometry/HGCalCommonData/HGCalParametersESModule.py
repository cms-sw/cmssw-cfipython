import FWCore.ParameterSet.Config as cms

def HGCalParametersESModule(**kwargs):
  mod = cms.ESProducer('HGCalParametersESModule',
    name = cms.string('HGCalEELayer'),
    name2 = cms.string('HGCalEESensitive'),
    nameW = cms.string('HGCalEEWafer'),
    nameC = cms.string('HGCalEESensitive'),
    nameT = cms.string('HGCal'),
    nameX = cms.string('HGCalEESensitive'),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
