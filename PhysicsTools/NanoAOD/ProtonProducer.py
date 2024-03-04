import FWCore.ParameterSet.Config as cms

def ProtonProducer(**kwargs):
  mod = cms.EDProducer('ProtonProducer',
    tagRecoProtonsMulti = cms.required.InputTag,
    tagRecoProtonsSingle = cms.required.InputTag,
    tagTrackLite = cms.required.InputTag,
    storeSingleRPProtons = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
