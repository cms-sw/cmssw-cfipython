import FWCore.ParameterSet.Config as cms

def GEMDQMHarvester(*args, **kwargs):
  mod = cms.EDProducer('GEMDQMHarvester',
    cutErr = cms.double(0.05),
    cutLowErr = cms.double(0),
    cutWarn = cms.double(0.05),
    resolutionLumi = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
