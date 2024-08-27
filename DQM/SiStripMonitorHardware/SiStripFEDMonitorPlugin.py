import FWCore.ParameterSet.Config as cms

def SiStripFEDMonitorPlugin(**kwargs):
  mod = cms.EDProducer('SiStripFEDMonitorPlugin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
