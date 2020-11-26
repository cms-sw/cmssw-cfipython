import FWCore.ParameterSet.Config as cms

BasicToPFJet = cms.EDProducer('BasicToPFJet',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
