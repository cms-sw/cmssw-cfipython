import FWCore.ParameterSet.Config as cms

def SiStripMonitorFilter(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
