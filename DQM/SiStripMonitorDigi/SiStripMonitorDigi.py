import FWCore.ParameterSet.Config as cms

def SiStripMonitorDigi(**kwargs):
  mod = cms.EDProducer('SiStripMonitorDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
