import FWCore.ParameterSet.Config as cms

QGTagger = cms.EDProducer('QGTagger',
  srcJets = cms.required.InputTag,
  srcRho = cms.required.InputTag,
  jetsLabel = cms.required.string,
  systematicsLabel = cms.string(''),
  useQualityCuts = cms.required.bool,
  jec = cms.InputTag(''),
  srcVertexCollection = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
