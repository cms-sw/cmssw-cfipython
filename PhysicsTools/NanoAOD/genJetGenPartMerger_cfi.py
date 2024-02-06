import FWCore.ParameterSet.Config as cms

genJetGenPartMerger = cms.EDProducer('GenJetGenPartMerger',
  srcJet = cms.required.InputTag,
  srcPart = cms.required.InputTag,
  cut = cms.required.string,
  hasTauAnc = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
