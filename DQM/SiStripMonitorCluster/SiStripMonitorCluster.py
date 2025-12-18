import FWCore.ParameterSet.Config as cms

def SiStripMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorCluster',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
