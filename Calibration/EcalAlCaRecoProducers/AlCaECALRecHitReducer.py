import FWCore.ParameterSet.Config as cms

def AlCaECALRecHitReducer(*args, **kwargs):
  mod = cms.EDProducer('AlCaECALRecHitReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
