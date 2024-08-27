import FWCore.ParameterSet.Config as cms

def VolumeBasedMagneticFieldESProducerFromDB(**kwargs):
  mod = cms.ESProducer('VolumeBasedMagneticFieldESProducerFromDB',
    debugBuilder = cms.untracked.bool(False),
    valueOverride = cms.int32(-1),
    label = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
