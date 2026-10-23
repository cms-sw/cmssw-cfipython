import FWCore.ParameterSet.Config as cms

def HcalDigiSortedTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalDigiSortedTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
