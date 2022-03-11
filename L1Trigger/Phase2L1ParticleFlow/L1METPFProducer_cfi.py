import FWCore.ParameterSet.Config as cms

L1METPFProducer = cms.EDProducer('L1METPFProducer',
  maxCandidates = cms.int32(128),
  L1PFObjects = cms.InputTag('L1PFProducer', 'l1pfCandidates'),
  mightGet = cms.optional.untracked.vstring
)
