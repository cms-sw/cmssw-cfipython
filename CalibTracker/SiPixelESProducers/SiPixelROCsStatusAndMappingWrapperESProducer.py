import FWCore.ParameterSet.Config as cms

def SiPixelROCsStatusAndMappingWrapperESProducer(**kwargs):
  mod = cms.ESProducer('SiPixelROCsStatusAndMappingWrapperESProducer',
    ComponentName = cms.string(''),
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
