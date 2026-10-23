import FWCore.ParameterSet.Config as cms

def L1TCaloRCTToUpgradeConverter(*args, **kwargs):
  mod = cms.EDProducer('L1TCaloRCTToUpgradeConverter',
    regionTag = cms.required.InputTag,
    emTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
