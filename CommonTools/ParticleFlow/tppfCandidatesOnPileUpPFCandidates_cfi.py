import FWCore.ParameterSet.Config as cms

tppfCandidatesOnPileUpPFCandidates = cms.EDProducer('TPPFCandidatesOnPileUpPFCandidates',
  enable = cms.required.bool,
  name = cms.untracked.string('No Name'),
  topCollection = cms.required.InputTag,
  bottomCollection = cms.required.InputTag,
  matchByPtrDirect = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
