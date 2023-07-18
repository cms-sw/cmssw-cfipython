import FWCore.ParameterSet.Config as cms

pfMetPuppi = cms.EDProducer('PFMETProducer',
  src = cms.InputTag('particleFlow'),
  globalThreshold = cms.double(0),
  alias = cms.string('@module_label'),
  calculateSignificance = cms.bool(False),
  srcJets = cms.optional.InputTag,
  srcLeptons = cms.optional.VInputTag,
  srcJetSF = cms.optional.string,
  srcJetResPt = cms.optional.string,
  srcJetResPhi = cms.optional.string,
  srcRho = cms.optional.InputTag,
  parameters = cms.PSet(),
  applyWeight = cms.bool(True),
  srcWeights = cms.InputTag('puppiNoLep'),
  mightGet = cms.optional.untracked.vstring
)
