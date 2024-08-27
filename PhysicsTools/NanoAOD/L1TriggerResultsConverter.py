import FWCore.ParameterSet.Config as cms

def L1TriggerResultsConverter(**kwargs):
  mod = cms.EDProducer('L1TriggerResultsConverter',
    legacyL1 = cms.required.bool,
    src = cms.required.InputTag,
    storeUnprefireableBits = cms.bool(False),
    src_ext = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
