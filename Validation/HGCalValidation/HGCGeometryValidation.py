import FWCore.ParameterSet.Config as cms

def HGCGeometryValidation(**kwargs):
  mod = cms.EDProducer('HGCGeometryValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
