import FWCore.ParameterSet.Config as cms

def l1t_L1ComparatorRun2(**kwargs):
  mod = cms.EDProducer('l1t::L1ComparatorRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
