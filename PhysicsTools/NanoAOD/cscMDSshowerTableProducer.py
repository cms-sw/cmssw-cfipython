import FWCore.ParameterSet.Config as cms

def cscMDSshowerTableProducer(*args, **kwargs):
  mod = cms.EDProducer('cscMDSshowerTableProducer',
    recHitLabel = cms.required.InputTag,
    dtSegmentLabel = cms.required.InputTag,
    rpcLabel = cms.required.InputTag,
    rParam = cms.double(0.4),
    nRechitMin = cms.int32(50),
    nStationThres = cms.int32(10),
    stripErr = cms.double(7),
    wireError = cms.double(8.6),
    pruneCut = cms.double(9),
    name = cms.string('cscRechits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
