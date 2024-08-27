import FWCore.ParameterSet.Config as cms

def L1TCaloRCTToUpgradeConverter(**kwargs):
  mod = cms.EDProducer('L1TCaloRCTToUpgradeConverter',
    regionTag = cms.required.InputTag,
    emTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
