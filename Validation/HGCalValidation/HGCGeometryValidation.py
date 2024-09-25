import FWCore.ParameterSet.Config as cms

def HGCGeometryValidation(*args, **kwargs):
  mod = cms.EDProducer('HGCGeometryValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
