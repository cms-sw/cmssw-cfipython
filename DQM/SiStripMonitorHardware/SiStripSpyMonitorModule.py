import FWCore.ParameterSet.Config as cms

def SiStripSpyMonitorModule(*args, **kwargs):
  mod = cms.EDProducer('SiStripSpyMonitorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
