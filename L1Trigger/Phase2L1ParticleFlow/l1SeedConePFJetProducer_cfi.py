import FWCore.ParameterSet.Config as cms

l1SeedConePFJetProducer = cms.EDProducer('L1SeedConePFJetProducer',
  L1PFObjects = cms.InputTag('l1tLayer1', 'Puppi'),
  nJets = cms.uint32(16),
  coneSize = cms.double(0.4),
  HW = cms.bool(False),
  debug = cms.bool(False),
  doCorrections = cms.bool(False),
  correctorFile = cms.string(''),
  correctorDir = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
