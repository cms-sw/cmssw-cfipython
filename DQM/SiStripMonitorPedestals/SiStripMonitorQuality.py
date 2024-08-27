import FWCore.ParameterSet.Config as cms

def SiStripMonitorQuality(**kwargs):
  mod = cms.EDProducer('SiStripMonitorQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
