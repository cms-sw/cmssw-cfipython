import FWCore.ParameterSet.Config as cms

def ProtonProducer(*args, **kwargs):
  mod = cms.EDProducer('ProtonProducer',
    tagRecoProtonsMulti = cms.required.InputTag,
    tagRecoProtonsSingle = cms.required.InputTag,
    tagTrackLite = cms.required.InputTag,
    storeSingleRPProtons = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
