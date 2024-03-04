import FWCore.ParameterSet.Config as cms

def SiStripMonitorFilter(**kwargs):
  mod = cms.EDProducer('SiStripMonitorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
