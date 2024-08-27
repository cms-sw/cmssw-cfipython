import FWCore.ParameterSet.Config as cms

def SiStripMonitorRawData(**kwargs):
  mod = cms.EDProducer('SiStripMonitorRawData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
