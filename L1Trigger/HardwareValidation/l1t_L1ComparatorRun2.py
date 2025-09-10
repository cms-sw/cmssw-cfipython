import FWCore.ParameterSet.Config as cms

def l1t_L1ComparatorRun2(*args, **kwargs):
  mod = cms.EDProducer('l1t::L1ComparatorRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
