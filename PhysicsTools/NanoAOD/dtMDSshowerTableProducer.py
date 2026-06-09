import FWCore.ParameterSet.Config as cms

def dtMDSshowerTableProducer(*args, **kwargs):
  mod = cms.EDProducer('dtMDSshowerTableProducer',
    recHitLabel = cms.required.InputTag,
    rpcLabel = cms.required.InputTag,
    rParam = cms.double(0.4),
    nRechitMin = cms.int32(50),
    nStationThres = cms.int32(10),
    name = cms.string('dt1DRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
