import FWCore.ParameterSet.Config as cms

def DD4hep_VolumeBasedMagneticFieldESProducerFromDB(**kwargs):
  mod = cms.ESProducer('DD4hep_VolumeBasedMagneticFieldESProducerFromDB',
    debugBuilder = cms.untracked.bool(False),
    useMergeFileIfAvailable = cms.bool(True),
    valueOverride = cms.int32(-1),
    label = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
