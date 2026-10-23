import FWCore.ParameterSet.Config as cms

def SiStripMonitorHLT(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorHLT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
