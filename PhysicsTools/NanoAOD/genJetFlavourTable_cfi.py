import FWCore.ParameterSet.Config as cms

genJetFlavourTable = cms.EDProducer('GenJetFlavourTableProducer',
  src = cms.required.InputTag,
  jetFlavourInfos = cms.required.InputTag,
  name = cms.required.string,
  cut = cms.required.string,
  deltaR = cms.required.double,
  mightGet = cms.optional.untracked.vstring
)
