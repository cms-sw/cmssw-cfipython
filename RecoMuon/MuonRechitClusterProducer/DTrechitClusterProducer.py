import FWCore.ParameterSet.Config as cms

def DTrechitClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('DTrechitClusterProducer',
    nRechitMin = cms.int32(50),
    rParam = cms.double(0.4),
    nStationThres = cms.int32(10),
    recHitLabel = cms.InputTag('dt1DRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
