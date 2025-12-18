import FWCore.ParameterSet.Config as cms

def HcalOnlineHarvesting(*args, **kwargs):
  mod = cms.EDProducer('HcalOnlineHarvesting',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
