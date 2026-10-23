import FWCore.ParameterSet.Config as cms

def SiStripMonitorTrack(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
