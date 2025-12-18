import FWCore.ParameterSet.Config as cms

def SiPixelROCsStatusAndMappingWrapperESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelROCsStatusAndMappingWrapperESProducer',
    ComponentName = cms.string(''),
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
