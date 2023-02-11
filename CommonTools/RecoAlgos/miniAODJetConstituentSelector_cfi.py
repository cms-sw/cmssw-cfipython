import FWCore.ParameterSet.Config as cms

miniAODJetConstituentSelector = cms.EDProducer('MiniAODJetConstituentSelector',
  src = cms.InputTag(''),
  cut = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
