import FWCore.ParameterSet.Config as cms

def ZDCQIE10Task(**kwargs):
  mod = cms.EDProducer('ZDCQIE10Task',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
