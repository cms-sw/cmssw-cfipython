import FWCore.ParameterSet.Config as cms

def GEMDQMHarvester(**kwargs):
  mod = cms.EDProducer('GEMDQMHarvester',
    cutErr = cms.double(0.05),
    cutLowErr = cms.double(0),
    cutWarn = cms.double(0.05),
    resolutionLumi = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
