import FWCore.ParameterSet.Config as cms

def SiStripMonitorDigi(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
