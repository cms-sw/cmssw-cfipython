import FWCore.ParameterSet.Config as cms

def L1GTAcceptFilter(*args, **kwargs):
  mod = cms.EDFilter('L1GTAcceptFilter',
    algoBlocksTag = cms.required.InputTag,
    triggerType = cms.int32(1),
    decision = cms.string('final'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
