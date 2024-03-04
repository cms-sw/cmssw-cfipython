import FWCore.ParameterSet.Config as cms

def CSCrechitClusterProducer(**kwargs):
  mod = cms.EDProducer('CSCrechitClusterProducer',
    nRechitMin = cms.int32(50),
    rParam = cms.double(0.4),
    nStationThres = cms.int32(10),
    recHitLabel = cms.InputTag('csc2DRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
