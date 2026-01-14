import FWCore.ParameterSet.Config as cms

def StreamThingProducer(*args, **kwargs):
  mod = cms.EDProducer('StreamThingProducer',
    array_size = cms.required.int32,
    instance_count = cms.required.int32,
    start_count = cms.untracked.int32(0),
    apply_bit_mask = cms.untracked.bool(False),
    bit_mask = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
