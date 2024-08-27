import FWCore.ParameterSet.Config as cms

def ClusterChargeMasker(**kwargs):
  mod = cms.EDProducer('ClusterChargeMasker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
