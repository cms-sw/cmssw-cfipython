import FWCore.ParameterSet.Config as cms

def CondHDF5ESSource(**kwargs):
  mod = cms.ESSource('CondHDF5ESSource',
    filename = cms.required.untracked.string,
    globalTag = cms.required.string,
    excludeRecords = cms.vstring(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
