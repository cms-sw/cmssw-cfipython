import FWCore.ParameterSet.Config as cms

def DDDetectorESProducer(*args, **kwargs):
  mod = cms.ESSource('DDDetectorESProducer',
    confGeomXMLFiles = cms.optional.FileInPath,
    rootDDName = cms.string('cms:OCMS'),
    label = cms.string(''),
    fromDB = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
