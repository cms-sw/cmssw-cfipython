import FWCore.ParameterSet.Config as cms

def OnlineBeamSpotESProducer(**kwargs):
  mod = cms.ESProducer('OnlineBeamSpotESProducer',
    timeThreshold = cms.int32(48),
    sigmaZThreshold = cms.double(2),
    sigmaXYThreshold = cms.double(4),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
