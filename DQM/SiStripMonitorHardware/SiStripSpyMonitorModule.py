import FWCore.ParameterSet.Config as cms

def SiStripSpyMonitorModule(**kwargs):
  mod = cms.EDProducer('SiStripSpyMonitorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
