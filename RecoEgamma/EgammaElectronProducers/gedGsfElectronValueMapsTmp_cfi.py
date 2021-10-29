import FWCore.ParameterSet.Config as cms

gedGsfElectronValueMapsTmp = cms.EDProducer('GEDGsfElectronValueMapProducer',
  gedGsfElectrons = cms.InputTag('gedGsfElectronsTmp'),
  egmPFCandidatesTag = cms.InputTag('particleFlowEGamma'),
  mightGet = cms.optional.untracked.vstring
)
