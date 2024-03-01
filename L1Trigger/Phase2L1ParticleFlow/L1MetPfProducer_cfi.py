import FWCore.ParameterSet.Config as cms

L1MetPfProducer = cms.EDProducer('L1MetPfProducer',
  L1PFObjects = cms.InputTag('L1PFProducer', 'l1pfCandidates'),
  maxCands = cms.int32(128),
  modelVersion = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
