import FWCore.ParameterSet.Config as cms

def VolumeBasedMagneticFieldESProducerFromDB(*args, **kwargs):
  mod = cms.ESProducer('VolumeBasedMagneticFieldESProducerFromDB',
    debugBuilder = cms.untracked.bool(False),
    valueOverride = cms.int32(-1),
    label = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
