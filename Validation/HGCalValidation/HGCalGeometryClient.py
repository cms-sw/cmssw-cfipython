import FWCore.ParameterSet.Config as cms

def HGCalGeometryClient(*args, **kwargs):
  mod = cms.EDProducer('HGCalGeometryClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
