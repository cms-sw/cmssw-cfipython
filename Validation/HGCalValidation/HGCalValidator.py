import FWCore.ParameterSet.Config as cms

def HGCalValidator(*args, **kwargs):
  mod = cms.EDProducer('HGCalValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
