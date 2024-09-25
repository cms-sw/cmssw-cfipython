import FWCore.ParameterSet.Config as cms

def OfflineToTransientBeamSpotESProducer(*args, **kwargs):
  mod = cms.ESProducer('OfflineToTransientBeamSpotESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
