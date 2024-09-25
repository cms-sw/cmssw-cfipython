import FWCore.ParameterSet.Config as cms

def DD4hep_VolumeBasedMagneticFieldESProducer(*args, **kwargs):
  mod = cms.ESProducer('DD4hep_VolumeBasedMagneticFieldESProducer',
    debugBuilder = cms.untracked.bool(False),
    useMergeFileIfAvailable = cms.bool(True),
    useParametrizedTrackerField = cms.required.bool,
    label = cms.untracked.string(''),
    version = cms.required.string,
    paramLabel = cms.required.string,
    geometryVersion = cms.required.int32,
    gridFiles = cms.required.VPSet,
    scalingVolumes = cms.required.vint32,
    scalingFactors = cms.required.vdouble,
    paramData = cms.vdouble(),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
