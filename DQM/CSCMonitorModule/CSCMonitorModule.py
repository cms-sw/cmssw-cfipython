import FWCore.ParameterSet.Config as cms

def CSCMonitorModule(*args, **kwargs):
  mod = cms.EDProducer('CSCMonitorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
