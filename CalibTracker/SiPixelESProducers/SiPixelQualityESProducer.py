import FWCore.ParameterSet.Config as cms

def SiPixelQualityESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelQualityESProducer',
    siPixelQualityFromDbLabel = cms.string(''),
    ListOfRecordToMerge = cms.VPSet(
      cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
      ),
      cms.PSet(
        record = cms.string('SiPixelDetVOffRcd'),
        tag = cms.string('')
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
