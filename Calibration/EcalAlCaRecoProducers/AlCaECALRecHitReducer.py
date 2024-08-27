import FWCore.ParameterSet.Config as cms

def AlCaECALRecHitReducer(**kwargs):
  mod = cms.EDProducer('AlCaECALRecHitReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
