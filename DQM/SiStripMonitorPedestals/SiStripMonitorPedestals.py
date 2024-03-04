import FWCore.ParameterSet.Config as cms

def SiStripMonitorPedestals(**kwargs):
  mod = cms.EDProducer('SiStripMonitorPedestals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
