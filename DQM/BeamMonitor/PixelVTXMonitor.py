import FWCore.ParameterSet.Config as cms

def PixelVTXMonitor(**kwargs):
  mod = cms.EDProducer('PixelVTXMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
