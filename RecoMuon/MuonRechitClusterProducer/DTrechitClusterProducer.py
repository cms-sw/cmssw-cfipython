import FWCore.ParameterSet.Config as cms

def DTrechitClusterProducer(**kwargs):
  mod = cms.EDProducer('DTrechitClusterProducer',
    nRechitMin = cms.int32(50),
    rParam = cms.double(0.4),
    nStationThres = cms.int32(10),
    recHitLabel = cms.InputTag('dt1DRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
