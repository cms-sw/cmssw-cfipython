import FWCore.ParameterSet.Config as cms

def HGCalHitClient(*args, **kwargs):
  mod = cms.EDProducer('HGCalHitClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
