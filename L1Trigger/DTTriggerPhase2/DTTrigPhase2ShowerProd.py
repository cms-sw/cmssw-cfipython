import FWCore.ParameterSet.Config as cms

def DTTrigPhase2ShowerProd(*args, **kwargs):
  mod = cms.EDProducer('DTTrigPhase2ShowerProd',
    digiTag = cms.InputTag('CalibratedDigis'),
    showerTaggingAlgo = cms.int32(1),
    threshold_for_shower = cms.int32(6),
    nHits_per_bx_phi = cms.int32(8),
    nHits_per_bx_z = cms.int32(8),
    obdt_hits_bxpersistence_phi = cms.int32(4),
    obdt_hits_bxpersistence_z = cms.int32(4),
    obdt_wire_relaxing_time = cms.int32(2),
    bmtl1_hits_bxpersistence = cms.int32(16),
    scenario = cms.int32(0),
    debug = cms.untracked.bool(False),
    dump_digis = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
