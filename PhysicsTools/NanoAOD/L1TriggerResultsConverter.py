import FWCore.ParameterSet.Config as cms

def L1TriggerResultsConverter(*args, **kwargs):
  mod = cms.EDProducer('L1TriggerResultsConverter',
    legacyL1 = cms.required.bool,
    src = cms.required.InputTag,
    storeUnprefireableBits = cms.bool(False),
    src_ext = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
