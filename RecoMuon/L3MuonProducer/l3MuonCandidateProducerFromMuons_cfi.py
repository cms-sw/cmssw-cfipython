import FWCore.ParameterSet.Config as cms

l3MuonCandidateProducerFromMuons = cms.EDProducer('L3MuonCandidateProducerFromMuons',
  InputObjects = cms.InputTag('hltL3Muons'),
  DisplacedReconstruction = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
