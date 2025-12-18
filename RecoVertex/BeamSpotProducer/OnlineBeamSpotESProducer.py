import FWCore.ParameterSet.Config as cms

def OnlineBeamSpotESProducer(*args, **kwargs):
  mod = cms.ESProducer('OnlineBeamSpotESProducer',
    timeThreshold = cms.int32(48),
    sigmaZThreshold = cms.double(2),
    sigmaXYThreshold = cms.double(4),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
