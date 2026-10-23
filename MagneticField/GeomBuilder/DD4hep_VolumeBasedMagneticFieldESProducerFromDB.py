import FWCore.ParameterSet.Config as cms

def DD4hep_VolumeBasedMagneticFieldESProducerFromDB(*args, **kwargs):
  mod = cms.ESProducer('DD4hep_VolumeBasedMagneticFieldESProducerFromDB',
    debugBuilder = cms.untracked.bool(False),
    useMergeFileIfAvailable = cms.bool(True),
    valueOverride = cms.int32(-1),
    label = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
