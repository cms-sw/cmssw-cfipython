import FWCore.ParameterSet.Config as cms

def HGCalConcentratorProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalConcentratorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
