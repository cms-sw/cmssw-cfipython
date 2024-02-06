import FWCore.ParameterSet.Config as cms

ProtonProducer = cms.EDProducer('ProtonProducer',
  tagRecoProtonsMulti = cms.required.InputTag,
  tagRecoProtonsSingle = cms.required.InputTag,
  tagTrackLite = cms.required.InputTag,
  storeSingleRPProtons = cms.required.bool,
  mightGet = cms.optional.untracked.vstring
)
