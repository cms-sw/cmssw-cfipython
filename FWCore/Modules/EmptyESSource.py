import FWCore.ParameterSet.Config as cms

def EmptyESSource(*args, **kwargs):
  mod = cms.ESSource('EmptyESSource',
    recordName = cms.required.string,
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.required.vuint32
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
