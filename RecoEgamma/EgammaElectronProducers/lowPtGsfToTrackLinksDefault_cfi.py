import FWCore.ParameterSet.Config as cms

lowPtGsfToTrackLinksDefault = cms.EDProducer('LowPtGSFToTrackLinker',
  tracks = cms.InputTag('generalTracks'),
  gsfPreID = cms.InputTag('lowPtGsfElectronSeeds'),
  gsfTracks = cms.InputTag('lowPtGsfEleGsfTracks'),
  mightGet = cms.optional.untracked.vstring
)
