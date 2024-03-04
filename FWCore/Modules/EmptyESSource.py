import FWCore.ParameterSet.Config as cms

def EmptyESSource(**kwargs):
  mod = cms.ESSource('EmptyESSource',
    recordName = cms.required.string,
    iovIsRunNotTime = cms.bool(True),
    firstValid = cms.required.vuint32
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
