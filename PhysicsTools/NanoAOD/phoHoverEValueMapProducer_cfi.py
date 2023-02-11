import FWCore.ParameterSet.Config as cms

phoHoverEValueMapProducer = cms.EDProducer('PhoHoverEValueMapProducer',
  src = cms.required.InputTag,
  relative = cms.required.bool,
  QuadraticEAFile_HoverE = cms.required.FileInPath,
  rho = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
