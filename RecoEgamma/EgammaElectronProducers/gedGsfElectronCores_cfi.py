import FWCore.ParameterSet.Config as cms

gedGsfElectronCores = cms.EDProducer('GEDGsfElectronCoreProducer',
  ctfTracks = cms.InputTag('generalTracks'),
  GEDEMUnbiased = cms.InputTag('particleFlowEGamma'),
  mightGet = cms.optional.untracked.vstring
)
