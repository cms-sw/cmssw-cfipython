import FWCore.ParameterSet.Config as cms

def CTPPSPixelRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('CTPPSPixelRecHitProducer',
    RPixVerbosity = cms.untracked.int32(0),
    RPixClusterTag = cms.InputTag('ctppsPixelClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
