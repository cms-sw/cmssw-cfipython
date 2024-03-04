import FWCore.ParameterSet.Config as cms

def SiStripCMMonitorPlugin(**kwargs):
  mod = cms.EDProducer('SiStripCMMonitorPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
