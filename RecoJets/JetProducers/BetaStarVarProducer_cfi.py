import FWCore.ParameterSet.Config as cms

BetaStarVarProducer = cms.EDProducer('BetaStarPackedCandidateVarProducer',
  srcJet = cms.required.InputTag,
  srcPF = cms.required.InputTag,
  maxDR = cms.required.double,
  mightGet = cms.optional.untracked.vstring
)
