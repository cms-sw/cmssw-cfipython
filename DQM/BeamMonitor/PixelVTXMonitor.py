import FWCore.ParameterSet.Config as cms

def PixelVTXMonitor(*args, **kwargs):
  mod = cms.EDProducer('PixelVTXMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
