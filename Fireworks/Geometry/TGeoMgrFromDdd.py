import FWCore.ParameterSet.Config as cms

def TGeoMgrFromDdd(*args, **kwargs):
  mod = cms.ESProducer('TGeoMgrFromDdd',
    level = cms.untracked.int32(10),
    verbose = cms.untracked.bool(False),
    fullName = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
