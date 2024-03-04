import FWCore.ParameterSet.Config as cms

def CTPPSPixelRecHitProducer(**kwargs):
  mod = cms.EDProducer('CTPPSPixelRecHitProducer',
    RPixVerbosity = cms.untracked.int32(0),
    RPixClusterTag = cms.InputTag('ctppsPixelClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
