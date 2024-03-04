import FWCore.ParameterSet.Config as cms

def BusyWaitIntLimitedProducer(**kwargs):
  mod = cms.EDProducer('BusyWaitIntLimitedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
