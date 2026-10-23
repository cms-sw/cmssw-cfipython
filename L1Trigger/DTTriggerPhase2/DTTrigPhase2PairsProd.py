import FWCore.ParameterSet.Config as cms

def DTTrigPhase2PairsProd(*args, **kwargs):
  mod = cms.EDProducer('DTTrigPhase2PairsProd',
    digiPhTag = cms.InputTag('dtTriggerPhase2PrimitiveDigis'),
    digiThTag = cms.InputTag('dtTriggerPhase2PrimitiveDigis'),
    scenario = cms.int32(0),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
