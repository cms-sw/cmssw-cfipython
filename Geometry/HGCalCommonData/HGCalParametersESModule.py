import FWCore.ParameterSet.Config as cms

def HGCalParametersESModule(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
