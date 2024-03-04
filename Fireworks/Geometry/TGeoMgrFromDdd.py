import FWCore.ParameterSet.Config as cms

def TGeoMgrFromDdd(**kwargs):
  mod = cms.ESProducer('TGeoMgrFromDdd',
    level = cms.untracked.int32(10),
    verbose = cms.untracked.bool(False),
    fullName = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
